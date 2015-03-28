import webbrowser
import os
import re

# Styles and scripting for the page
# Added a style for description and simple JS to handle the slide based carousel.
# The basis for the slide based carousel came from a CodeAcademy project I did with lots of customization to make it work here
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer.modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 50px;
            padding-top: 50px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .description {
            margin-bottom: 20px;
            padding-top: 20px;
        }
		
		    .slider {
            position: relative;
            width: 100%;
            height: 90%;
            margin-bottom: 20px;
            border-bottom: 1px solid #ddd;
        }

        .slide {
            display: none;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }

        .active-slide {
            display: block;
        }
        
        .slider-nav {
          text-align: center;
          margin-top: 20px;
        }

        .arrow-prev {
          margin-right: 45px;
          display: inline-block;
          vertical-align: top;
          margin-top: 9px;
        }

        .arrow-next {
          margin-left: 45px;
          display: inline-block;
          vertical-align: top;
          margin-top: 9px;
        }

        .slider-dots {
          list-style: none;
          display: inline-block;
          padding-left: 0;
          margin-bottom: 0;
        }

        .slider-dots li {
          color: #bbbcbc;
          display: inline;
          font-size: 30px;
          margin-right: 5px;
        }

        .slider-dots li.active-dot {
          color: #363636;
        }

    </style>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="slider">
      {movie_tiles}
    </div>
	<div class="slider-nav">
      <a href="#" class="arrow-prev"><img src="http://s3.amazonaws.com/codecademy-content/courses/ltp2/img/flipboard/arrow-prev.png"></a>
      <ul class="slider-dots">
        <li class="dot active-dot">&bull;</li>
        <li class="dot">&bull;</li>
        <li class="dot">&bull;</li>
        <li class="dot">&bull;</li>
        <li class="dot">&bull;</li>
        <li class="dot">&bull;</li>
      </ul>
      <a href="#" class="arrow-next"><img src="http://s3.amazonaws.com/codecademy-content/courses/ltp2/img/flipboard/arrow-next.png"></a>
    </div> 
  </body>
  <script src="app.js"></script>
</html>
'''

# A single movie entry html template
#Added to template to get the additional info in the description
movie_tile_content = '''
<div class="slide {additional_class}" data-trailer-youtube-id="{trailer_youtube_id}">
	<div class="container">
		<div class="row">
			<div class="text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
				<img src="{poster_image_url}" width="220" height="342">
				<h2 class="title">{movie_title}</h2>
				<div class="description">
					<div class="storyline">{movie_storyline}</div>
					<div class="imdb_url"><a href="{imdb_url}">IMDB Page</a></div>
				</div>
			</div>
		</div>
	</div>	
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
		if(movies.index(movie) == 0):
			additional_classes="active-slide"
		else:
			additional_classes=""

		#print additional_classes
        # Extract the youtube ID from the url
        
		trailer_youtube_id = movie.trailer_youtube_url
		#print trailer_youtube_id

        # Append the tile for the movie with its content filled in
		#Added the storyline and imdb_url to add to the description
		content += movie_tile_content.format(
			additional_class=additional_classes,
			trailer_youtube_id=trailer_youtube_id,
			movie_title=movie.title,
			poster_image_url=movie.poster_image_url,
			movie_storyline = movie.storyline,
			imdb_url=movie.imdb_url
		)
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
