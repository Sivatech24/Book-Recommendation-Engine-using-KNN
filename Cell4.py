def get_recommends(book_title):
    # Find index of book title in the dataset
    book_index = books[books['Book-Title'] == book_title].index[0]
    
    # Get distances and indices of nearest neighbors
    distances, indices = model.kneighbors(pivot_table.iloc[book_index, :].values.reshape(1, -1), n_neighbors=6)
    
    # List of recommended books with their distances
    recommended_books = []
    for i in range(1, len(distances.flatten())):
        recommended_books.append([books.iloc[indices.flatten()[i]]['Book-Title'], distances.flatten()[i]])
    
    return [book_title, recommended_books]
