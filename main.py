from uzivatel import Uzivatel


print("Hello")
user1 = Uzivatel("Adrian", "Toman", 20)
user2 = Uzivatel("Fero", "Svarny",12)
user1.print_info()
user1= user2
user1.print_info()