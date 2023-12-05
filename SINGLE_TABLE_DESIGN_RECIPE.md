Single Table Design Recipe Template
Copy this recipe template to design and create a database table from a specification.

1. Extract nouns from the user stories or specification

# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

albums, title, release_year, artist_id

# Expected response (200 OK)
(No content)

2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

Record	Properties
album	title, release year, artist_id

Name of the table (always plural): albums

Column names: title, release_year, artist_id

3. Decide the column types
Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:

id: SERIAL
title: text
release_year: int
artist_id: int

4. Write the SQL
-- EXAMPLE
-- file: records.sql

-- Replace the table name, columm names and types.

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int
  artist_id: int 
);
5. Create the table
psql -h 127.0.0.1 database_name < albums_table.sql







Single Table Design Recipe Template
Copy this recipe template to design and create a database table from a specification.

Test-drive a route GET /artists, which returns the list of artists:

# Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone

Test-drive a route POST /artists, which creates a new artist in the database. Your test should verify the new artist is returned in the response of GET /artists.
# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing




1. Extract nouns from the user stories or specification

# Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone


# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing


2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.


Record	Properties
artist	title, genre

Name of the table (always plural): artists

Column names: title, genre

3. Decide the column types
Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:

id: SERIAL
name: text
genre: text

4. Write the SQL
-- EXAMPLE
-- file: records.sql

-- Replace the table name, columm names and types.

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name text,
  genre int
);
5. Create the table
psql -h 127.0.0.1 database_name < albums_table.sql