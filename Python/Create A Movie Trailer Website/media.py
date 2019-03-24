import webbrowser
"""import the web browser module"""

class Movie():
    """This class provides a way to store movie related information. Which contains movie title , movie story line etc"""
    def __init__(self, valid_ratings, movie_title, movie_storyline, poster_image, trailer_youtube, writer, language, country):
        """Define a __init__method. self is the first argument. put other parameters named valid_ratings, movie_title etc in init method """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.writer = writer
        self.language = language
        self.country = country
        self.valid_ratings = valid_ratings
    def show_trailer(self):
        """To open the browser and play youtube trailer.show_trailer is name of the method.self is the first argument"""
        webbrowser.open(self.trailer_youtube_url)

class Tvshow():
    """This class provides a way to store tvshow related information. Which contains tvshow title , tvshow story line etc"""
    def __init__(self, valid_ratings, tvshow_title, tvshow_storyline, tvshow_image, tvshow_trailer, writer, language, country):      
        self.title = tvshow_title
        self.storyline = tvshow_storyline
        self.poster_image_url = tvshow_image
        self.trailer_youtube_url = tvshow_trailer
        self.writer = writer
        self.language = language
        self.country = country
        self.valid_ratings = valid_ratings
    def tvshow_trailer(self):
        """To open the browser and play youtube trailer.Tvshow_trailer is name of the method.self is the first argument"""
        webbrowser.open(self.trailer_youtube_url)





        
        
        
            
            
    
