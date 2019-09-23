<img src='./media/logo.png' alt='Movie Prettifier Logo' title='Movie Prettifier' height='200'/>

# Movies Folder Prettifier

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
![GitHub last commit](https://img.shields.io/github/last-commit/Snowfighter/MoviesFolderPrettifier)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

:star: Star me on GitHub — just for fun and motivation :grinning:

Do you have a LOAD of movies on your hard drive ? I have :laughing: 

I am huge fan of movies from 90s, 80s, 70s, 60, ... up to the old school black and white ones. Unfortunately, they were scattered around `Movie` folder on my Seagate external hard drive.  

So one day I have decided to beautify the folder by classifying and moving all the movies into the right **Genre** folders. Being a lazy person I have decide to use **Python** to do all the hard work :blush:

## Table of contents

-   [Idea](#idea)
-   [dummyMoviesGenerator.py](#dummyMoviesGenerator.py) 
-   [API](#api)

## Idea

The idea behind this little project was to find API that is going to determine based on the title of the movie which genre it belongs to. If the folder with the genre name exists,the script will put it into it, otherwise it will create the needed folder and move the video file. 

This was a little outline of what I wanted to do, so let's now look at the implementation.

## dummyMoviesGenerator.py

This script creates dummy MKV movie files for testing purposes.

I create a `FOLDERPATH` variable with a path to the test folder. In order to make the most accurate tests, I have decided to make a dictionary `movies_db` where keys will be four genres (*westerns*, *horrors*, *dramas*, *fantasies*) and corresponding values will be lists with the most iconic titles. 

```python
import os
from random import choices

FOLDERPATH = '.../MoviesFolderPrettifier_movies_list'

movies_db = {
    'westerns': ['Once Upon a Time in the West', 'Unforgiven',  'The Wild Bunch',
            'No Country for Old Men',  'They Died with Their Boots On',  'Will Penny',
            'The Treasure of the Sierra Madre', 'Butch Cassidy and the Sundance Kid',  'The Ox-Bow Incident',
            'The Man Who Shot Liberty Valance', 'Monte Walsh'],

    'horrors': ['HELLRAISER', 'Phantasm', 'Scream',
          '28 Days Later...', 'The Conjuring', "WES CRAVEN'S NEW NIGHTMARE ",
          'Pitch Black', 'The Descent', 'Saw',
          'Split', '1408', 'Jeepers Creepers'],

    'dramas': ['Titanic', 'American Beauty', 'Gran Torino',
         "One Flew Over the Cuckoo's Nest", 'Green Book', 'Gone with the Wind',
         '12 Angry Men', 'Wonder', 'The Book of Henry',
         'The Pursuit of Happyness', 'The Last Samurai', 'The Bucket List'],

    'fantasies': ['The Lord of the Rings: The Fellowship of the Ring', 'Avatar', 'Hugo',
             'Groundhog Day', 'Star Wars: Episode IV - A New Hope', 'Harry Potter and the Deathly Hallows: Part 1',
             'Midnight in Paris', 'The Mummy', 'Constantine',
             'Doctor Strange', 'Dead Man', 'Wonder Woman', 'Thor: Ragnarok'],
}
```

In the `generate_dummy_movies()` function I populate `movies_local_list` with 4 random titles of every genre from `movies_db` using `choice()` function.

After that for every item in the `movies_local_list` I append '.mkv' extension and then create this file by opening it and then closing. 

```python
def generate_dummy_movies():
    movies_local_list = []
    for key in movies_db:
        movies_local_list.extend(choices(movies_db[key], k=4))

    print(movies_local_list)
    for item in movies_local_list:
        filename = item + '.mkv'
        filepath = os.path.join(FOLDERPATH, filename)
        f = open(filepath, 'a').close()


generate_dummy_movies()

```
<a href='https://www.themoviedb.org'>
    <img src='./media/themoviedb_logo.png' alt='The Movie Database' title='The Movie Database (TMDb)' align='right' height='80'/>
</a>

# API