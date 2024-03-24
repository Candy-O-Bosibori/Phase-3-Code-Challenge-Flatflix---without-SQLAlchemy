class Movie:
    def __init__(self, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if len(title) == 0:
            raise ValueError("Title must be longer than 0 characters")
        
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            raise ValueError("Title must be a string")
        if len(new_title) == 0:
            raise ValueError("Title must be longer than 0 characters")
        
        self._title = new_title

    def reviews(self):
        pass

    def reviewers(self):
        pass

    def average_rating(self):
        pass

    @classmethod
    def highest_rated(cls):
        pass
    
class Review:
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        
class Viewer:
    def __init__(self, username):
        self.username = username

    def reviews(self):
        pass

    def reviewed_movies(self):
        pass

    def has_reviewed_movie(self, movie):
        pass

    def add_review(self, movie, rating):
        pass