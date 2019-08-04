import requests

url = 'https://api.themoviedb.org/3/search/movie'

payload = {
    'api_key': '',
    'language': 'en-US',
    'page': 1,
    'include_adult': 'true',
}


def movie_finder(title):
    payload['query'] = title
    r = requests.get(url, params=payload)
    json_res = r.json()
    print(json_res)
    if json_res['results']:
        return json_res['results'][0]['title']
    else:
        return False


print(movie_finder('Mars Needs Moms'))

