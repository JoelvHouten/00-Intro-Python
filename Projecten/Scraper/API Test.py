import requests

api_key = ""
url = f"https://api.themoviedb.org/3/movie/550?api_key={api_key}"

response = requests.get(url)
if response.status_code == 200:
    print("API request successful!")
else:
    print(f"Request failed with status code: {response.status_code}")

