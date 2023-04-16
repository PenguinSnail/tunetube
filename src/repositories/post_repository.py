# # PlaceHolder

# from src.models import Movie, db


# class MovieRepository:

#     def get_all_movies(self):
#         movies = Movie.query.all()
#         # print(movies)
#         return movies

#     def get_movie_by_id(self, ID):
#         # TODO get a single movie from the DB using the ID
#         movie = Movie.query.filter_by(movie_id = ID).first()
#         return movie

#     def create_movie(self, title, director, rating):
#         new_movie = Movie(title,director,rating)
#         db.session.add(new_movie)
#         db.session.commit()
#         return new_movie

#     def search_movies(self, t):
#         movie = Movie.query.filter(Movie.title.contains(t)).all()
#         return movie

# # Singleton to be used in other modules
# movie_repository_singleton = MovieRepository()
