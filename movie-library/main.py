from view.MenuView import MenuView
from constants.MenuActionEnum import MenuActionEnum

from services.MovieLibraryService import MovieLibraryService
from models.MovieModel import MovieModel

she_hulk = MovieModel("She-Hulk: Neuvěřitelná právnička",
                   "V seriáli She-Hulk: Neuveriteľná právnička od štúdia Marvel musí Jennifer Waltersová - právnička zaoberajúca sa právnymi prípadmi spojenými so superľuďmi - žiť komplikovaným životom single ženy po tridsiatke, ktorá je zhodou náhod tiež zelená, dvojmetrová a supersilná obryňa.",
                   2022,
                   ["Akční","Dobrodružný", "Sci-Fi", "Komedie", "Drama"],
                   50
                   )

movie_library = MovieLibraryService()
movie_library.addMovie(she_hulk)
movie_library.addMovie(she_hulk)
movie_library.to_string()
movie_library.removeMovie(0)
movie_library.to_string()

# print(she_hulk.to_string())
menu_view = MenuView()


while True:
    match menu_view.menu():
        case MenuActionEnum.ADD_MOVIE.value:
            movie_library.addMovie(menu_view.add_movie())
            pass
        case MenuActionEnum.REMOVE_MOVIE.value:
            pass
        case MenuActionEnum.SHOW_LIBRARY.value:
            movie_library.to_string()
            pass
        case MenuActionEnum.QUIT.value:
            menu_view.quite_option()
            pass
    