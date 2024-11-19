from DataParse import game_rating_freq_dictionary
from WilsonScore import confidence_interval

# for game in game_rating_freq_dictionary:
unsorted_games = confidence_interval(game_rating_freq_dictionary)
# print(confidence_interval(game_rating_freq_dictionary))
sorted_games = sorted(unsorted_games, key=lambda x: x[1][2], reverse=True)

# Print the sorted list
for game in sorted_games[:10]:
    print(game)