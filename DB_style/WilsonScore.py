from sqlalchemy import create_engine
import pandas as pd
import math

db_user = 'root'
db_password = 'farabi68'
db_host = 'localhost'
db_port = 3306
db_name = 'board_games'

engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
connection = engine.connect()

rating_freq_df = pd.read_sql(sql="SELECT * FROM board_games.games_rounded_reviews_frequency ORDER BY name", con=connection)
# total_ratings_per_game = rating_freq_df.groupby('name')['frequency'].sum().reset_index()

data = {  
    'id': [151070] * 5,  
    'name': ['Gladiatoris'] * 5,  
    'rating': [10, 9, 8, 6, 5],  
    'frequency': [17, 10, 2, 1, 1]  
}  

df = pd.DataFrame(data)  

grouped = rating_freq_df.groupby(['id', 'name'])
# grouped = df.groupby(['id', 'name'])

def score_formula(p,n,z = 1.96):
    term1 = p + (z**2) / (10 * n)
    term2 = z * math.sqrt((p * (1 - p) + (z**2) / (100 * n)) / n)
    denominator = (1 + (z**2) / n)
    
    upper_bound = (term1 + term2) / denominator
    lower_bound = (term1 - term2) / denominator
    return (upper_bound, lower_bound)

# print(grouped)

# game_rating_freq_dictionary = game_rating_freq_dictionary[:1]

# def confidence_interval(games):
#     results = []
#     for row in rating_freq_df.itertuples(index=False): 
results = []
for (game_id, game_name), group in grouped:
    # Total ratings for the game
    n = group['frequency'].sum()
    
    # Initialize weighted scores
    weighted_upper_score = 0
    weighted_lower_score = 0
    
    # Loop through each rating-frequency pair in the group
    for _, row in group.iterrows():
        k = row['rating']  # Rating value
        v = row['frequency']  # Frequency count
        
        # Calculate the probability
        p = v / n
        
        # Calculate Wilson score bounds
        lower_bound, upper_bound = score_formula(p, n)
        
        # Calculate weighted scores
        weighted_upper_score += k * upper_bound
        weighted_lower_score += k * lower_bound
    
    # Calculate the average score
    average_score = (weighted_upper_score + weighted_lower_score) / 2
    
    # Append result for the game
    results.append((game_name, game_id, weighted_lower_score, weighted_upper_score, average_score))

# Convert results to a DataFrame
results_df = pd.DataFrame(results, columns=['name', 'id', 'upper_score','lower_score', 'average_score'])

# Display the results
sorted_results_df = results_df.sort_values(by='lower_score', ascending=False)

# Reset the index for better readability
sorted_results_df.reset_index(drop=True, inplace=True)

# Display the sorted DataFrame
print(sorted_results_df)

# print(sum_p)
