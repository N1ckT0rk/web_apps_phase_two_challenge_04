{{ NAME }} Route Design Recipe
Copy this design recipe template to test-drive a plain-text Flask route.

1. Design the Route Signature
Include the HTTP method, the path, and any query or body parameters.

# EXAMPLE

# Show all albums route
GET /albums


# Add new albums route
POST /albums
  title: string
  release_year: int
  aritist_id: int

2. Create Examples as Tests
Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.

# EXAMPLE

# GET /albums
#  Expected response (200 OK):
"""
Album('Lateralus', 2000, 1)
"""

# POST /albums
title: "Voyage"
release_year: 2022
artist_id: 2
#  Expected response (200 OK):
"""
(No content)
"""
# GET /albums
#  Expected response (200 OK):
"""
Album('Lateralus', 2000, 1)
Album('Voyage', 2022, 2)
"""


# POST /albums
#  Expected response (400 Bad Request):
"""
You need to submit a title, release_year and artist_id
"""




{{ NAME }} Route Design Recipe
Copy this design recipe template to test-drive a plain-text Flask route.

1. Design the Route Signature
Include the HTTP method, the path, and any query or body parameters.

# EXAMPLE

# Show all albums route
GET /albums


# Add new albums route
POST /albums
  title: string
  release_year: int
  aritist_id: int

2. Create Examples as Tests
Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.

# EXAMPLE

# GET /artists
#  Expected response (200 OK):
"""
Pixies, ABBA, Taylor Swift, Nina Simone
"""

# POST /artists
name=Wild nothing
genre=Indie
#  Expected response (200 OK):
"""
(No content)
"""
# GET /albums
#  Expected response (200 OK):
"""
Pixies, ABBA, Taylor Swift, Nina Simone, Wild Nothing
"""


# POST /artists
#  Expected response (400 Bad Request):
"""
You need to submit a name and genre
"""