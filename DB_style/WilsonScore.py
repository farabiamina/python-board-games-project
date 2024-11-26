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

def score_formula(p,n,z = 1.96):
    term1 = p + (z**2) / (10 * n)
    term2 = z * math.sqrt((p * (1 - p) + (z**2) / (100 * n)) / n)
    denominator = (1 + (z**2) / n)
    
    # upper_bound = (term1 + term2) / denominator
    lower_bound = (term1 - term2) / denominator
    return lower_bound
# print(grouped)

# game_rating_freq_dictionary = game_rating_freq_dictionary[:1]

# def confidence_interval(games):
#     results = []
#     for row in rating_freq_df.itertuples(index=False): 
results = []
for (game_id, game_name), group in grouped:
    n = group['frequency'].sum()
    
    # weighted_upper_score = 0
    weighted_lower_score = 0
    
    for _, row in group.iterrows():
        k = row['rating']
        v = row['frequency']
        
        p = v / n
        
        lower_bound = score_formula(p, n)
        
        # weighted_upper_score += k * upper_bound
        weighted_lower_score += k * lower_bound
    
    results.append((game_name, game_id, weighted_lower_score))

results_df = pd.DataFrame(results, columns=['name', 'id','lower_score'])

sorted_results_df = results_df.sort_values(by='lower_score', ascending=False)

sorted_results_df.reset_index(drop=True, inplace=True)

sorted_results_df['insertion_order'] = range(len(sorted_results_df))

# Display the sorted DataFrame
print(sorted_results_df)

# print(sum_p)

dtype_mapping = {
    'int64': 'INTEGER',
    'float64': 'REAL',
    'object': 'TEXT'
}

sql_parts = []
for column, dtype in zip(sorted_results_df.columns, sorted_results_df.dtypes):
    sql_type = dtype_mapping.get(str(dtype), 'VARCHAR(255)')  # Default to VARCHAR(255) if type is not mapped
    sql_parts.append(f"`{column}` {sql_type}")

sql_statement = (
    "CREATE TABLE IF NOT EXISTS sorted_games_reviews (\n    " +
    ",\n    ".join(sql_parts) +
    "\n);"
)

print(sql_statement)

try:
    connection.execute(sql_statement)
    print("Table `sorted_games_reviews` created successfully.")
except Exception as e:
    print("An error occurred:", e)
finally:
    connection.close()

results_df.to_sql("sorted_games_reviews", con=engine, if_exists='append', index=False)
