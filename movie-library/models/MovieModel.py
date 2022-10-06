from array import array
from ast import Num


class MovieModel:
    def __init__(self, paTitle:str, paDescription:str, paYear:Num, paGenre:array, paRating:Num) -> None:
        self.title:str = paTitle
        self.description:str = paDescription
        self.year:Num = paYear
        self.genre:array = paGenre
        self.rating:Num = paRating
        pass
    
    def genre_to_string(self):
        return '/'.join(self.genre)
    
    def to_string(self):
        return f"Title: {self.title:10} | Description: {self.description:20} | Year: {self.year} | Genre: {self.genre_to_string()} | Rating: {self.rating}%"