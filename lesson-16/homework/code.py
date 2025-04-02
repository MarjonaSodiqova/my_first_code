import sqlite3
import pandas as pd

conn = sqlite3.connect('chinook.db')
customers_df = pd.read_sql_query("SELECT * FROM customers LIMIT 10", conn)
print(customers_df)
conn.close()

iris_df = pd.read_json('iris.json')
print(iris_df.shape)
print(iris_df.columns.tolist())

titanic_df = pd.read_excel('titanic.xlsx')
print(titanic_df.head())

flights_df = pd.read_parquet('flights.parquet')
print(flights_df.info())

movie_df = pd.read_csv('movie.csv')
print(movie_df.sample(10))

iris_df.columns = iris_df.columns.str.lower()
iris_selected = iris_df[['sepal_length', 'sepal_width']]
print(iris_selected.head())

titanic_over_30 = titanic_df[titanic_df['Age'] > 30]
print(titanic_over_30.head())
gender_counts = titanic_df['Sex'].value_counts()
print(gender_counts)

flight_subset = flights_df[['origin', 'dest', 'carrier']]
print(flight_subset.head())
unique_dests = flights_df['dest'].nunique()
print(unique_dests)

long_movies = movie_df[movie_df['duration'] > 120]
sorted_long_movies = long_movies.sort_values('director_facebook_likes', ascending=False)
print(sorted_long_movies.head())

iris_stats = iris_df.agg(['mean', 'median', 'std'])
print(iris_stats)

age_stats = {
    'min_age': titanic_df['Age'].min(),
    'max_age': titanic_df['Age'].max(),
    'sum_age': titanic_df['Age'].sum()
}
print(age_stats)

top_director = movie_df.groupby('director_name')['director_facebook_likes'].sum().idxmax()
print(top_director)
longest_movies = movie_df.nlargest(5, 'duration')[['movie_title', 'director_name', 'duration']]
print(longest_movies)

missing_values = flights_df.isnull().sum()
print(missing_values)
numeric_col = flights_df.select_dtypes(include='number').columns[0]
flights_df[numeric_col] = flights_df[numeric_col].fillna(flights_df[numeric_col].mean())
print(flights_df[numeric_col].isnull().sum())