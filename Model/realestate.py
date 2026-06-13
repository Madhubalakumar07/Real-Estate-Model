import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"D:\Codes\Realestate model\Model\bengaluru_house_prices.csv")
print(df.head())
print(df.shape)

# Data Cleaning
# Drop the 'area_type', 'society', 'balcony', and 'availability' columns
df.drop(['area_type', 'society', 'balcony', 'availability'], axis=1, inplace=True)

# Handle missing values by dropping rows with NaN values
df.dropna(inplace=True)

# Convert 'size' column to numeric by extracting the number of bedrooms
df['bhk'] = df['size'].apply(lambda x: int(x.split(' ')[0]))

# Convert 'total_sqft' to numeric, handling cases where it is a range
def convert_sqft_to_num(x):
    tok = x.split('-')
    if len(tok) == 2:
        return (float(tok[0]) + float(tok[1])) / 2
    try:
        return float(x)
    except:
        return None

df['total_sqft'] = df['total_sqft'].apply(convert_sqft_to_num)

# Create a new column for price per square foot
df['price_per_sqft'] = df['price'] * 100000 / df['total_sqft']

# Reduce the number of locations by grouping less frequent locations into 'other'
location_counts = df['location'].value_counts()
locations_less_than_10 = location_counts[location_counts <= 10]
df['location'] = df['location'].apply(lambda x: 'other' if x in locations_less_than_10 else x)

print(df.head(20))

# Outlier Removal
# Remove properties with price per square foot
def remove_pps_outliers(df):
    df_res = pd.DataFrame()
    for key, loc_df in df.groupby('location'):
        m = np.mean(loc_df['price_per_sqft'])
        std = np.std(loc_df['price_per_sqft'])
        reduced_df = loc_df[(loc_df['price_per_sqft'] > (m - std)) & (loc_df['price_per_sqft'] <= (m + std))]
        df_res = pd.concat([df_res, reduced_df], ignore_index=True)
    return df_res
df = remove_pps_outliers(df)
print(df.shape)

# Plot 2bhk and 3bhk properties to visualize outliers
def plot_scatter_chart(df, location):
    bhk2 = df[(df['location'] == location) & (df['bhk'] == 2)]
    bhk3 = df[(df['location'] == location) & (df['bhk'] == 3)]
    plt.scatter(bhk2['total_sqft'], bhk2['price'], color='blue', label='2 BHK', s=50)
    plt.scatter(bhk3['total_sqft'], bhk3['price'], color='green', label='3 BHK', s=50)
    plt.xlabel('Total Square Feet')
    plt.ylabel('Price')
    plt.title(f'Price vs Total Square Feet in {location}')
    plt.legend()
    plt.show()
plot_scatter_chart(df, 'Rajaji Nagar')

# Remove Bhk outliers
def remove_bhk_outliers(df):
    exclude_indices = np.array([])
    for location, loc_df in df.groupby('location'):
        bhk_stats = {}
        for bhk, bhk_df in loc_df.groupby('bhk'):
            bhk_stats[bhk] = {
                'mean': np.mean(bhk_df['price_per_sqft']),
                'std': np.std(bhk_df['price_per_sqft']),
                'count': bhk_df.shape[0]
            }
        for bhk, bhk_df in loc_df.groupby('bhk'):
            stats = bhk_stats.get(bhk - 1)
            if stats and stats['count'] > 5:
                exclude_indices = np.append(exclude_indices, bhk_df[bhk_df['price_per_sqft'] < (stats['mean'])].index.values)
    return df.drop(exclude_indices, axis='index')
df = remove_bhk_outliers(df)
print(df.shape)

plot_scatter_chart(df, 'Rajaji Nagar')

# Plot histogram to visualize bathroom outliers
plt.rcParams['figure.figsize'] = (20, 10)
plt.hist(df['bath'], bins=50)
plt.xlabel('Number of Bathrooms')
plt.ylabel('Count')
plt.title('Distribution of Bathrooms')
plt.show()

# Remove bathroom outliers
df = df[df['bath'] < df['bhk'] + 2]
print(df.shape) 
df.drop(['size', 'price_per_sqft'], axis=1, inplace=True)