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

## Idea

The idea behind this little project was to find API that is going to determine based on the title of the movie which genre it belongs to. If the folder with the genre name exists,the script will put it into it, otherwise it will create the needed folder and move the video file. 

This was a little outline of what I wanted to do, so let's now look at the implementation.

## dummyMoviesGenerator.py