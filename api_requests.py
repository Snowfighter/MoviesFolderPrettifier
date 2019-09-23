import requests

url = 'https://api.themoviedb.org/3/search/movie'

payload = {
    'api_key': '...',
    'language': 'en-US',
    'page': 1,
    'include_adult': 'true',
}

genres = [
    {
      "id": 28,
      "name": "Action"
    },
    {
      "id": 12,
      "name": "Adventure"
    },
    {
      "id": 16,
      "name": "Animation"
    },
    {
      "id": 35,
      "name": "Comedy"
    },
    {
      "id": 80,
      "name": "Crime"
    },
    {
      "id": 99,
      "name": "Documentary"
    },
    {
      "id": 18,
      "name": "Drama"
    },
    {
      "id": 10751,
      "name": "Family"
    },
    {
      "id": 14,
      "name": "Fantasy"
    },
    {
      "id": 36,
      "name": "History"
    },
    {
      "id": 27,
      "name": "Horror"
    },
    {
      "id": 10402,
      "name": "Music"
    },
    {
      "id": 9648,
      "name": "Mystery"
    },
    {
      "id": 10749,
      "name": "Romance"
    },
    {
      "id": 878,
      "name": "Science Fiction"
    },
    {
      "id": 10770,
      "name": "TV Movie"
    },
    {
      "id": 53,
      "name": "Thriller"
    },
    {
      "id": 10752,
      "name": "War"
    },
    {
      "id": 37,
      "name": "Western"
    }
  ]


def movie_genre_finder(title):
    #print('Title:' + title)
    payload['query'] = title
    r = requests.get(url, params=payload)
    json_res = r.json()
    #print(json_res)
    if json_res['results']:
        genre_id = json_res['results'][0]['genre_ids']
        if 878 in genre_id:
            return "Science Fiction"
        elif 14 in genre_id:
            return "Fantasy"
        else:
            for item in genres:
                if item['id'] == genre_id[0]:
                    return item['name']
    else:
        return '!MOV'


