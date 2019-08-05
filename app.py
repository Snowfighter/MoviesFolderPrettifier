import os
import shutil
from api_requests import movie_genre_finder

FOLDERPATH = '/Volumes/Seagate Expansion Drive/Movies/Thrilers, Action movies and so on/'

url = 'https://api.themoviedb.org/3/search/movie'

def main():
    for file in os.listdir(FOLDERPATH):
        print(file)
        try:
            if not file == '.DS_Store' and not os.path.isdir(FOLDERPATH + file):
                genre = movie_genre_finder(file.split('(')[-2])
                if (genre != '!MOV') and (not os.path.exists(os.path.join(FOLDERPATH, genre))):
                    os.makedirs(os.path.join(FOLDERPATH, genre))

                if os.path.exists(os.path.join(FOLDERPATH, genre)):
                    file_path = FOLDERPATH + file
                    shutil.move(file_path, os.path.join(FOLDERPATH, genre))
        except IndexError:
            if not file == '.DS_Store':
                genre = movie_genre_finder(file.split('.')[0])
                if (genre != '!MOV') and (not os.path.exists(os.path.join(FOLDERPATH, genre))):
                    os.makedirs(os.path.join(FOLDERPATH, genre))

                if os.path.exists(os.path.join(FOLDERPATH, genre)):
                    file_path = FOLDERPATH + file
                    shutil.move(file_path, os.path.join(FOLDERPATH, genre))


if __name__ == "__main__":
    main()

