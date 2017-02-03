import webbrowser

#Create a class named movie that instances in entertainment_center.py will use
class Movie():
    """This class provides a way to store movie related information"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    #define required __init__ method with arguments related to Movies
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #self refers to the instances of movies that can be made
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #define show_trailer method to open the web browser and play the youtube link given
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
