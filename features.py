import pandas as pd
import sys

# Load datasets
books_df = pd.read_csv('Books.csv')
ratings_df = pd.read_csv('Ratings.csv')
users_df = pd.read_csv('Users.csv')

# Merge Ratings and Books data
ratings_books_df = pd.merge(ratings_df, books_df, on='ISBN')

# Merge User data
merged_df = pd.merge(ratings_books_df, users_df, on='User-ID')

# Now merged_df contains the combined information from all three datasets
print(len(merged_df))
# print(merged_df.head(10))



# Extracting relevant features
features_df = merged_df[['User-ID', 'ISBN', 'Year-Of-Publication', 'Book-Author', 'Book-Rating']]

before_dropping_rows = len(features_df)

features_df.dropna(inplace=True)

after_dropping_rows = len(features_df)
rows_dopped = before_dropping_rows - after_dropping_rows


# Group by User-ID and ISBN to aggregate features
grouped_df = features_df.groupby(['User-ID', 'ISBN']).agg({
    'Year-Of-Publication': 'first',  # Year of publication of the book
    'Book-Author': 'first',  # Author of the book
    'Book-Rating': 'mean'  # Average rating given by the user for the book
}).reset_index()

# Now grouped_df contains the relevant features extracted from the merged dataset

print(grouped_df.head(5))

grouped_df.to_csv('grouped-data.csv')

sys.exit()
