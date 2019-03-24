import webbrowser
import os
import re

# Styles and scripting for the page
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
        #trailer .modal-dialog {
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
            margin-bottom: 20px;
            padding-top: 20px;
        }
         .tvshow-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .tvshow-tile:hover {
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
        .storyline{        
        font-size: x-small;
        font-family: 'Lato', sans-serif;
        
        }
        .title {
            font-size:large;
            font-family: 'Lato', sans-serif;
            font-weight: bold;
            
        }
        .rating{
            font-family: 'Lato', sans-serif;
            font-size:medium;
            font-weight: 100;
            text-align:center;
            
        }
        .writer{
            font-family: 'Lato', sans-serif;
            font-size:large;
            font-weight: 100;
            text-align: center;
            
        }
        .language{
            font-size:small;
            font-family: SanFran;
            text-align: center;
        }
        .country{
            font-size:small;
            font-family: 'Lato', sans-serif;
            text-align: center;
        }
        div {
            font-family: 'Lato', sans-serif;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));

        });
        // Start playing the tvshow video whenever the trailer modal is opened
        $(document).on('click', '.tvshow-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        // Animate in the tvshows when the page loads
        $(document).ready(function () {
          $('.tvshow-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
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
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie And Tvshow Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}      
    </div>
    <div class="container">
      {tvshow_tiles}      
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
    <div><p class="storyline">{movie_storyline}</p></div>
    <div><p class="writer">Writer : {writer}</p></div>
    <div><p class="rating">Rating : {valid_ratings}</p></div>     
    <div><p class="country">Country : {country}</p></div>      
    <div><p class="language">Language : {language}</p></div>    
</div>
'''

# A single tvshow entry html template
tvshow_tile_content = '''
<div class="col-md-6 col-lg-4 tvshow-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{tvshow_title}</h2>
    <div><p class="storyline">{tvshow_storyline}</p></div>
    <div><p class="writer">Writer : {writer}</p></div>
    <div><p class="rating">Rating : {valid_ratings}</p></div>
    <div><p class="country">Country : {country}</p></div>    
    <div><p class="language">Language : {language}</p></div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            valid_ratings=movie.valid_ratings,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            writer =  movie.writer,
            language = movie.language,
            country = movie.country
        )
    return content
def create_tvshow_tiles_content(tvshows):
    # The HTML content for this section of the page
    content = ''
    for tvshow in tvshows:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', tvshow.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', tvshow.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the tvshow with its content filled in
        content += tvshow_tile_content.format(
            tvshow_title=tvshow.title,
            tvshow_storyline=tvshow.storyline,
            valid_ratings=tvshow.valid_ratings,
            poster_image_url=tvshow.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            writer =  tvshow.writer,
            language = tvshow.language,
            country = tvshow.country
        )
    return content

def open_movies_page(movies, tvshows):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies), tvshow_tiles=create_tvshow_tiles_content(tvshows))
  #rendered_content1 = main_page_content.format(tvshow_tiles=create_tvshow_tiles_content(tvshows))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
