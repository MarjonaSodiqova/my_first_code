import requests
import random

def get_genres(api_key):
    url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    return response.json()['genres'] if response.status_code == 200 else None

def get_movies_by_genre(api_key, genre_id, page=1):
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {"api_key": api_key, "with_genres": genre_id, "page": page}
    response = requests.get(url, params=params)
    return response.json() if response.status_code == 200 else None

def main():
    api_key = "bf23ae9aef98f9b961730e026f4030c8ey"  # Replace with your actual TMDb API key
    genre_input = input("Enter a movie genre: ").strip().lower()
    genres = get_genres(api_key)
    if not genres:
        print("Failed to fetch genres.")
        return

    genre_id = None
    for genre in genres:
        if genre_input == genre['name'].lower():
            genre_id = genre['id']
            break
    if not genre_id:
        print("Genre not found.")
        return

    movies_data = get_movies_by_genre(api_key, genre_id)
    if not movies_data or not movies_data.get('results'):
        print("Failed to fetch movies.")
        return

    total_pages = movies_data.get('total_pages', 1)
    if total_pages > 1:
        random_page = random.randint(1, total_pages)
        movies_data = get_movies_by_genre(api_key, genre_id, random_page)
        if not movies_data or not movies_data.get('results'):
            print(f"Failed to fetch movies on page {random_page}.")
            return
    
    movies = movies_data.get('results', [])
    if not movies:
        print("No movies found for this genre.")
        return

    movie = random.choice(movies)
    print("Recommended Movie:")
    print("Title:", movie.get('title', 'N/A'))
    print("Release Date:", movie.get('release_date', 'N/A'))
    print("Overview:", movie.get('overview', 'N/A'))

if __name__ == "__main__":
    main()
