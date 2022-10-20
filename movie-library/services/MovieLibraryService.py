from ast import Num
from models.MovieModel import MovieModel


class MovieLibraryService():
    def __init__(self) -> None:
        self.movies:list(MovieModel) = list()
        pass
    
    
    def addMovie(self, paMovie:MovieModel):
        self.movies.append(paMovie)
        pass
    
    def removeMovie(self, paMovieIndex:Num):
        self.movies.pop(paMovieIndex)
        pass
    
    def to_string(self):
        print("**************** MOVIE LIBRARY ****************")
        for movie in self.movies:
            print(movie.to_string())
            print("")
        print("")
        
        
        