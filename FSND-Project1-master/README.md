# FSND-Project1
# Description:
Simple project to create a static website featuring favorite movies.
-- entertainment_center holds the list of movies (actually IMDB_IDs) that are used to search the OMDB using their API and then uses the title from OMDB to query Youtube for the trailer's youtube video id. Once all of that is placed in the instance of the movie class. 
-- A list of the instances is passed to fresh_tomatoes that displays it as a webpage. 
-- There's some customization there to show additional info, provide an IMDB link, and make it just a bit more interactive with a slide based carousel.

#Requirements:
-- It should be noted to actually use this, you will need to modify the trailerLookup file to include your developer API key
Its best if I don't dump that into Github for the world to use.

#Build Dependencies: 
-- This code requires python 2.7. To run the application you'll need to have entertainment_center.py, media.py, trailerlookup.py, fresh_tomatoes.py, and app.js saved to the same directory. Then build/run entertainment_center.py. You also need to have an internet connection to let the application do the look ups for the movie data and youtube trailer.
--You will also need to install the google-apiclient to run this code locally.
