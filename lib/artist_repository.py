from lib.artist import Artist

class ArtistRepository:
    
    def __init__(self, connection):
        self.connection = connection

    def all_artists(self):
        rows = self.connection.execute('SELECT * FROM artists')
        artists = []
        for row in rows:
            item = row['artist_name']
            artists.append(item)
        return artists

    def add_artist(self, artist):
        self.connection.execute('INSERT INTO artists (artist_name, genre) VALUES (%s, %s)', [
            artist.artist_name, artist.genre])
        return None