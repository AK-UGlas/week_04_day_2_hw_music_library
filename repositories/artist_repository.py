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

def select(id):
    artist = None
    # remember, we only need to return the first index (the list should be length=1)
    result = run_sql("SELECT * FROM artists WHERE id = (%s)", [id])[0] 
    if result is not None:
        artist = Artist(result['name'], result['id'])
    return artist

def select_all():
    artists = []
    results = run_sql("SELECT * FROM artists")
    if results is not None:
        for row in results:
            artists.append( Artist(row['name'], row['id']))
    return artists

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
