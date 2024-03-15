# Create a pivot table for collaborative filtering
pivot_table = ratings.pivot(index='User-ID', columns='ISBN', values='Book-Rating')

# Remove NaN values to avoid issues with NearestNeighbors
pivot_table = pivot_table.fillna(0)

# Filter users and books based on rating counts
# This step involves removing users/books with insufficient ratings

# Instantiate and fit the NearestNeighbors model
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(pivot_table.values)
