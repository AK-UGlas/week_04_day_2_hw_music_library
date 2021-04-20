class Album:
    def __init__(self, title, genre, artist, id=None):
        self.title = title
        self.genre = genre
        self.artist = artist # this is an object of class Artist
        self.id = id