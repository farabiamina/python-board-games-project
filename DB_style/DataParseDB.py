# import pandas as pd
from sqlalchemy import create_engine, text

db_user = 'root'
db_password = 'farabi68'
db_host = 'localhost'
db_port = 3306
db_name = 'board_games'

engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# with engine.connect() as connection:
#     connection.execute(text("""
#         CREATE TABLE games_reviews_frequency AS
#         SELECT
#             id,
#             name,
#             rating,
#             COUNT(*) AS frequency

#         FROM games_reviews
#         GROUP BY rating, id, name;
#     """))
# print('Table created successfully!')

with engine.connect() as connection:
    connection.execute(text("""
        CREATE TABLE board_games.games_rounded_reviews_frequency AS
        SELECT
            id,
            name,
            rating,
            COUNT(*) AS frequency
        FROM board_games.rounded_games_reviews
        GROUP BY rating, id, name;
    """))
print('Table created successfully!')

