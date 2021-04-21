from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id] # in this schema, artist must exist before album
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    run_sql("DELETE FROM albums")

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = (%s)"
    values = [id]
    result = run_sql(sql, values)[0] # remember, we only need to return the first index (the list should be length=1)
    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], result['genre'], artist, result['id'])
    return album

def select_all():
    albums = []
    results = run_sql("SELECT * FROM albums")
    if results is not None:
        for row in results:
            artist = artist_repository.select(row['artist_id'])
            albums.append( Album(row['title'], row['genre'], artist, row['id']) )
    return albums

def delete(id):
    run_sql("DELETE FROM albums WHERE id = (%s)", [id])

def display_albums(albums):
    print("  id  |          title         |   genre   | artist_name ")
    for album in albums:
        print(f"  {album.id}\t{album.title}\t{album.genre}\t{album.artist.name}")
