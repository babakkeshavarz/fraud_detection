import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv(r'data/creditcard.csv')

# Display the first few rows of the DataFrame
print(data.head())

print(list(data.columns))

print(data.describe())

# Calculate the skewness of each column
skewness = data.skew()

# Display the skewness of each column
print(skewness)


# Calculate the kurtosis of each column
kurtosis = data.kurt()

# Display the kurtosis of each column
print(kurtosis)

import matplotlib.pyplot as plt



# Plot boxplots for columns V26, V22, and V28 next to each other
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(20, 5))

data['V26'].plot(kind='box', ax=axes[0], title='V26')
data['V22'].plot(kind='box', ax=axes[1], title='V22')
data['V28'].plot(kind='box', ax=axes[2], title='V28')

plt.tight_layout()
plt.show()