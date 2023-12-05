# Tests for your routes go here

# === Example Code Below ===

# """
# GET /emoji
# """
# def test_get_emoji(web_client):
#     response = web_client.get("/emoji")
#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == ":)"


# When I make a GET request to /albums
# I should get a 200 ok response with the one
# album in the table returned
def test_get_albums(web_client, db_connection):
    db_connection.seed('seeds/records.sql')
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Album(1, Lateralus, 2000, 1)"

# When I POST a new album to the database 
# I get a 200 ok reponse with nothing returned
# And then when i get all albums it is reflected there
def test_post_albums(db_connection, web_client):
    db_connection.seed('seeds/records.sql')
    response = web_client.post('/albums', data={'title': 'Voyage', 'release_year': '2022', 'artist_id': '2'})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ''

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "" \
        "Album(1, Lateralus, 2000, 1)\n" \
        "Album(2, Voyage, 2022, 2)"

# When I try to POST an album without all the
# correct parameters, I get 400 bad response
# and a message
def test_post_albums_with_error(db_connection, web_client):
    db_connection.seed('seeds/records.sql')
    response = web_client.post('/albums')
    assert response.status_code == 400
    assert response.data.decode("utf-8") == 'You need to submit a title, release_year and artist_id'

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "" \
        "Album(1, Lateralus, 2000, 1)"



# When I make a GET request to /artists
# I should get a 200 ok response with the a
# formatted string on artists
def test_get_artists(web_client, db_connection):
    db_connection.seed('seeds/records.sql')
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Pixies, ABBA, Taylor Swift, Nina Simone"

# When I make a POST request to /artists
# I get a 200 ok response and the artist
# no content and it is then reflected 
# in #get_artists
def test_post_artists(web_client, db_connection):
    db_connection.seed('seeds/records.sql')
    post_response = web_client.post("/artists", data={'artist_name': 'Wild nothing', 'genre': 'Indie'})
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "" \
        "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"

# When I try to POST an artist without the parameters
# I get a 400 bad reponse and a message
def test_post_artists_with_error(web_client, db_connection):
    db_connection.seed('seeds/records.sql')
    post_response = web_client.post("/artists")
    assert post_response.status_code == 400
    assert post_response.data.decode("utf-8") == "You need to submit an artist_name and a genre"

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "" \
        "Pixies, ABBA, Taylor Swift, Nina Simone"