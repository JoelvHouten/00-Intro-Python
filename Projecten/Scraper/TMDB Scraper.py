import requests

def get_tmdb_info(title, year, api_key):
    search_url = f"https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": api_key,
        "query": title,
        "year": year
    }
    
    search_response = requests.get(search_url, params=params).json()

    if not search_response['results']:
        print("No results found.")
        return

    movie = next((m for m in search_response['results'] if m.get('release_date', '').startswith(year)), None)

    if not movie:
        print(f"No movie found for {title} ({year})")
        return

    movie_id = movie['id']
    title = movie['title']
    year = movie.get('release_date', 'N/A')[:4]
    overview = movie.get('overview', 'N/A')
    poster_path = movie.get('poster_path')
    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else 'N/A'

    details_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    images_url = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    videos_url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos"

    details = requests.get(details_url, params={"api_key": api_key}).json()
    images = requests.get(images_url, params={"api_key": api_key}).json()
    videos = requests.get(videos_url, params={"api_key": api_key}).json()

    backdrops = images.get('backdrops', [])[:3]
    image_urls = [f"https://image.tmdb.org/t/p/w780{img['file_path']}" for img in backdrops]

    trailer_url = 'N/A'
    for video in videos.get('results', []):
        if video['type'] == 'Trailer' and video['site'] == 'YouTube':
            trailer_url = f"https://www.youtube.com/watch?v={video['key']}"
            break

    print(f"Title: {title}")
    print(f"Year: {year}")
    print(f"Overview: {overview}")
    print(f"Poster: {poster_url}")
    print(f"Images: {image_urls}")
    print(f"Trailer: {trailer_url}")

api_key = ""
get_tmdb_info("Payback", "1999", api_key)

