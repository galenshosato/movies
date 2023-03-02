class Movie:
    def __init__(self, title):
        self.title = title
        self.reviews = []

    def get_title(self):
        return self.title

    def get_reviews(self):
        return self.reviews

    def get_viewers(self):
        movies = []
        for movie in self.reviews:
            movies.append(movie.viewer)
        return movies
            

    def average_rating(self):
        return sum([review.rating for review in self.reviews])

    def highest_review(self):
        highest_review = self.reviews[0]
        for review in self.reviews:
            if review.rating > highest_review.rating:
                highest_review = review
        return highest_review


class Viewer:
    def __init__(self, username):
        self.username = username
        self.reviews = []

    def get_username(self):
        return self.username

    def get_reviews(self):
        return self.reviews

    def get_movies(self):
        return [viewer.movie for viewer in self.reviews]

    def has_reviewed(self, movie):
        for review in self.reviews:
            if review.movie == movie:
                return True  

    def rate_movie(self, movie, rating):
        review = Review(self, movie, rating)
        self.reviews.append(review)


class Review:
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

    def get_rating(self):
        return self.rating 

    def get_viewer(self):
        return self.viewer

    def get_movie(self):
        return self.movie
