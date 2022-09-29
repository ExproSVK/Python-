from ast import Num
from asyncio.proactor_events import _ProactorBasePipeTransport
from msilib.schema import MoveFile
from multiprocessing.dummy import Array
from MovieModel import MovieModel
from constants.MenuActionEnum import MenuActionEnum

class MenuView:
    def __init__(self) -> None:
        pass

    def menu(self):
        print("Welcome in Movie Library")
        print("Add movie : ({MenuActionEnum.ADD_MOVIE})")
        print("Remove movie ({MenuActionEnum.REMOVE_MOVIE})")
        print("Show Library ({MenuActionEnum.SHOW_MOVIE})")
        print("Quit ({MenuActionEnum.QUIT})")
        user_input = input("Select option from the menu > ")
        return user_input

    def add_movie(self) -> MoveFile:
        title:str = input("Enter movie Title: ")
        description:str = input("Enter Movie description: ")
        year:Num = input("Enter Year of Movie: ")
        genre:str = input("Enter Movie Genres: ")
        rating:Num = input("Enter Movie Rating: ")
        return MovieModel(title,description,year,[genre],rating)



    def quit_option(self):
        print("Bye")
        exit(0)
       