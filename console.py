import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

# create artists
metallica = Artist('Metallica')
weird_al = Artist('"Weird Al" Yankovic')

# save artists

# create albums
album_1 = Album('The Black Album', 'Metal', metallica)
album_2 = Album('Master of Puppets', 'Metal', metallica)
album_3 = Album('Running with Scissors', 'Parody', weird_al)

# save albums

# queries:




pdb.set_trace()
