# webbrowser is a module necessary for the show_trailer function
import webbrowser


# creates the main class with its attributes
class Movie():
    def __init__(self, movie_title, movie_year, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
