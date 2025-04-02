import pandas as pd
import sqlite3

conn = sqlite3.connect('chinook.db')
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print(customers_df.head(10))

iris_df = pd.read_json('iris.json')
print(iris_df.shape)
print(iris_df.columns)

titanic_df = pd.read_excel('titanic.xlsx')
print(titanic_df.head(5))

flights_df = pd.read_parquet('flights.parquet')
print(flights_df.info())

movie_df = pd.read_csv('movie.csv')
print(movie_df.sample(10))

iris_df.columns = iris_df.columns.str.lower()
print(iris_df[['sepal_length', 'sepal_width']])

filtered_titanic = titanic_df[titanic_df['age'] > 30]
print(filtered_titanic)
print(titanic_df['sex'].value_counts())

print(flights_df[['origin', 'dest', 'carrier']])
print(flights_df['dest'].nunique())

filtered_movies = movie_df[movie_df['duration'] > 120]
sorted_movies = filtered_movies.sort_values(by='director_facebook_likes', ascending=False)
print(sorted_movies)

print(iris_df.describe())

print(titanic_df['age'].agg(['min', 'max', 'sum']))

print(movie_df.groupby('director_name')['director_facebook_likes'].sum().idxmax())
print(movie_df.nlargest(5, 'duration')[['duration', 'director_name']])

print(flights_df.isnull().sum())
flights_df.fillna(flights_df.mean(), inplace=True)
