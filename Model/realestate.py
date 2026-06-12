import pandas as pd
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