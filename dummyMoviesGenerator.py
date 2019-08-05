import os
from random import choices

FOLDERPATH = '/Users/SergeyChernayev/Documents/Coding/Projects/MoviesFolderPrettifier_movies_list'

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
