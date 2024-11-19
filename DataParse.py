import pandas as pd
data = pd.read_csv("bgg-19m-reviews/bgg-19m-reviews.csv", usecols=['user', 'rating', 'ID', 'name'])

all_reviews = data
games_rating_list = all_reviews.groupby('name')['rating'].apply(list).reset_index()
games_rating_list['num_reviews'] = games_rating_list['rating'].apply(len)
# Find the game with the largest number of reviews
most_reviews_game = games_rating_list.loc[games_rating_list['num_reviews'].idxmax()]
# print(f"Game with the largest number of reviews:\nName: {most_reviews_game['name']}\nNumber of Reviews: {most_reviews_game['num_reviews']}")

game_rating_freq_dictionary = []
max_rating_count = 0
for game in games_rating_list.itertuples(index=False):
    frequency = {}
    for rating_value in game.rating:
        if rating_value in frequency:
            frequency[rating_value] += 1
        else:
            frequency[rating_value] = 1
    game_rating_freq_dictionary.append((game.name, frequency))

    num_ratings = len(game.rating)  # Get the number of ratings for the current game
    if num_ratings > max_rating_count:
        max_rating_count = num_ratings
        game_with_max_ratings = (game.name, frequency)

# print(game_rating_freq_dictionary[0])
