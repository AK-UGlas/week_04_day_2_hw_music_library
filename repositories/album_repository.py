from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id] # in this schema, artist must exist before album
    results = run_sql(sql, values)
    album.id = results[0]['id']
    return album

def delete_all():
    run_sql("DELETE FROM albums")

def make_album(row):
    artist = artist_repository.select(row['artist_id'])
    return Album(row['title'], row['genre'], artist, row['id'])

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = (%s)"
    result = run_sql(sql, [id])
    if result:
        album = make_album(result[0])
    return album

def select_all():
    results = run_sql("SELECT * FROM albums")
    return [make_album(row) for row in results]

def delete(id):
    run_sql("DELETE FROM albums WHERE id = (%s)", [id])

def display_albums(albums):
    print("  id  |          title         |   genre   | artist_name ")
    for album in albums:
        print(f"  {album.id}\t{album.title}\t{album.genre}\t{album.artist.name}")
