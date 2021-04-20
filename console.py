import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

# create artists
metallica = Artist('Metallica')
weird_al = Artist('"Weird Al" Yankovic')

# save artists
artist_repository.save(metallica)
artist_repository.save(weird_al)

# create albums
album_1 = Album('The Black Album', 'Metal', metallica)
album_2 = Album('Master of Puppets', 'Metal', metallica)
album_3 = Album('Running with Scissors', 'Parody', weird_al)

# save albums
album_repository.save(album_1)
album_repository.save(album_2)
album_repository.save(album_3)

# queries:
# 1: Find artist/album by id
valid_id = album_1.id


# 3: delete all albums / artists
album_repository.delete_all()
artist_repository.delete_all()



pdb.set_trace()
