from ast import Num
from MovieModel import MovieModel
from models.MovieModel import MovieModels

class MovieLibraryService:
    def __init__(self) -> None:
        self.movies:list(MovieModel) = list()
        pass

    def addMovie(self, movie:MovieModel):
        self.movies.append(movie)
        pass

    def removeMovie(self, paIMovieIndex:Num):
        self.movies.pop(paIMovieIndex)
        pass

    def to_string(self):
        print("*******************MOVIE LIBRARY*******************")
        print("\n")
        for movie in self.movies:
            print(movie.to_string())
            print("")
        print("")