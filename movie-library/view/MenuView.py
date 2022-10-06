from ast import Num

from models.MovieModel import MovieModel
from constants.MenuActionEnum import MenuActionEnum


class MenuView:
    
    def __init__(self) -> None:
        pass
    
    def menu(self):
        print("Welcom to Movie Library")
        print(f"Add Movie ({MenuActionEnum.ADD_MOVIE.value})")
        print(f"Remove Movie ({MenuActionEnum.REMOVE_MOVIE.value})")
        print(f"Show library ({MenuActionEnum.SHOW_LIBRARY.value})")
        print(f"Quit ({MenuActionEnum.QUIT.value})")
        user_input = input("Select an option from the menu: ")
        return user_input
    
    def add_movie(self)-> MovieModel:
        title:str = input("Enter movie title: ")
        description:str = input("Enter movie description: ")
        year:Num = input("Enter year: ")
        genre:str = input("Enter movie genre: ")
        rating:Num = input("Enter ratin in %: ")
        return MovieModel(title,description,year,[genre], rating)
    
    def quite_option(self):
        print("Bye!!")
        exit(0)
        

    
    
    

            