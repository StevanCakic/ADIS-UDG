class Post:
    def __init__(self, name, description="Default Description", author="Admin", id=1):
        self.__name = name
        self.__description = description
        self.__author = author
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name[0].istitle():
            self.__name = name
        else:
            print("Potrebno je da naslov clanka ima prvo veliko slovo u nazivu!")

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

post_a = Post("Clanak 1", "Probni clanak", "Marko Markovic", 2)
post_b = Post(name="Clanak 2", author="Ivan Ivanovic")
# post_c = Post() # moze li ovo?
print(post_a) # zasto ovako stampa
print(type(post_a))
print(post_a.get_name())

post_a.set_name("Novi opis")
print(post_a.get_name())
