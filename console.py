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
valid_album_id = album_1.id
found_album = album_repository.select(valid_album_id)

invalid_album_id = 12312
empty_album = album_repository.select(invalid_album_id) # should return None


valid_artist_id = metallica.id
# find artist
found_artist = artist_repository.select(valid_artist_id)
# # find all albums by that artist
metallica_albums = artist_repository.albums(metallica)

# 3: List all albums
albums = album_repository.select_all()
album_repository.display_albums(albums)

# 4: list all artists
artists = artist_repository.select_all()
artist_repository.display_artists(artists)
# 5: delete all albums / artists
# album_repository.delete_all()
# artist_repository.delete_all()

#pdb.set_trace()
