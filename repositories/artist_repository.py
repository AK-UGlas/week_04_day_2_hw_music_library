from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    artist.id = results[0]['id']
    return artist

def delete_all():
    run_sql("DELETE FROM artists")

def make_artist(row):
    return Artist(row['name'], row['id'])

def select(id):
    artist = None
    results = run_sql("SELECT * FROM artists WHERE id = (%s)", [id])
    if results:
        result = results[0]
        artist = make_artist(result)
    return artist

def select_all():
    results = run_sql("SELECT * FROM artists")
    return [make_artist(row) for row in results]

def albums(artist):
    albums = [] # must return something, so set up return value here
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)
    
    for row in results:
        albums.append( Album(row['title'], row['genre'], artist, row['id']) )

    return albums

def display_artists(artists):
    print("  id  |     name    ")
    for artist in artists:
        print(f"  {artist.id}\t {artist.name}")
