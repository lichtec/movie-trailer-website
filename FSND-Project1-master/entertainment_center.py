import media, fresh_tomatoes, urllib2, json
from xml.dom import minidom
import trailerLookUp

'''Entertainment_center holds the initial data of IMDB_IDs for favorite movies. Those IDs are then used to query the omdbapi and retrieve 
	the necessary data except the trailer url. I then use the title plus 'trailer' to query youtube's api for the first result. The dict of
	movies is then placed in a list that is passed to fresh_tomatoes
'''
moviesCollection = {'tt0114709':media.Movie(), 'tt2015381':media.Movie(), 'tt0091042':media.Movie(), 'tt0082971':media.Movie(), 'tt1049413':media.Movie(), 'tt0076759':media.Movie()}

movies=[]

for imdbID in moviesCollection:
	req = urllib2.Request('http://www.omdbapi.com/?i={0}&plot=short&r=json'.format(imdbID))
	response = urllib2.urlopen(req)
	movie_data = json.load(response)
	moviesCollection[imdbID].title = movie_data["Title"]
	moviesCollection[imdbID].storyline = movie_data["Plot"]
	moviesCollection[imdbID].poster_image_url = str(movie_data["Poster"])
	moviesCollection[imdbID].imdb_url = "http://www.imdb.com/title/{0}/".format(imdbID)
	
for imdbID in moviesCollection:
	titleWords = str(moviesCollection[imdbID].title).split()
	query=""
	#Build the query for youtube by splitting the words of the title, adding +, and tacking on the trailer keyword to pull the proper results. 
	for word in titleWords:
		if('-' in titleWords):
			titleWords.remove('-')
                        
	for word in titleWords:
		query = query+"+" + word
	query=query[1:] + "+trailer"
	
	#trailer lookup will return a list of video id results. Right now trailerLookUp limits to one result returned to keep things simple.
	trailerID = trailerLookUp.trailer(query)
	#print trailerID
	#The youtube url is then just the basic url plus the id returned from trailerlookup
	moviesCollection[imdbID].trailer_youtube_url = trailerID[0]

for imdbID in moviesCollection:
	movies.append(moviesCollection[imdbID])
	#print moviesCollection[imdbID].trailer_youtube_url
	
fresh_tomatoes.open_movies_page(movies)
