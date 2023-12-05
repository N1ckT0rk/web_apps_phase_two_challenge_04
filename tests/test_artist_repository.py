from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# When we call ArtistRepository #all_artists
# We get a list of all the artists in the 
# database.
def test_all_artists(db_connection):
    db_connection.seed('seeds/records.sql')
    repository = ArtistRepository(db_connection)
    artists = repository.all_artists()
    assert artists == ["Pixies", "ABBA", "Taylor Swift", "Nina Simone"]

# When we call ArtistRepository #add_artist
# The artist is added to the table
def test_add_artist(db_connection):
    db_connection.seed('seeds/records.sql')
    repository = ArtistRepository(db_connection)
    fake_artist = Artist(None, 'Fake name', "Fake genre")
    repository.add_artist(fake_artist)
    assert repository.all_artists() == ["Pixies", "ABBA", "Taylor Swift", "Nina Simone", "Fake name"]