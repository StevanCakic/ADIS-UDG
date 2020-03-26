def valid(boja):
    return boja >= 0 and boja <= 255

class Color:

    def __init__(self, red, green, blue):
        self.__red = red
        self.__green = green
        self.__blue = blue

    def get_red(self):
        return self.__red

    def get_green(self):
        return self.__green

    def get_blue(self):
        return self.__blue

    def set_red(self,new_red):
        if valid(new_red):
            self.__red = new_red
        else:
            print("Pogresan unos")

    def set_green(self, new_green):
        if valid(new_green):
            self.__green = new_green
        else:
            print("Pogresan unos")

    def set_blue(self, new_blue):
        if valid(new_blue):
            self.__blue = new_blue
        else:
            print("Pogresan unos")

    def add_red(self, change):
        if (self.__red + change) < 0 or (self.__red + change) > 255:
            print("Boja izlazi iz opsega vrijednosti")
        else:
            self.__red = self.__red + change

    def add_blue(self, change):
        if (self.__blue + change) < 0 or (self.__blue + change) > 255:
            print("Boja izlazi iz opsega vrijednosti")
        else:
            self.__blue = self.__blue + change

    def add_green(self, change):
        if (self.__green + change) < 0 or (self.__green + change) > 255:
            print("Boja izlazi iz opsega vrijednosti")
        else:
            self.__green = self.__green+change

    def __lt__(self, other):
        return self.__blue < other.__blue and self.__green < other.__green and self.__red < other.__red

    def __eq__(self, other):
        return self.__blue == other.__blue and self.__green == other.__green and self.__red == other.__red

    def __str__(self):
        return f"red:{self.__red}, green:{self.__green}, blue:{self.__blue}"

color1 = Color(150, 123, 134)
color2 = Color(20,30,50)
color3 = Color(20,30,50)

print(color1 == color2)
print(color2 == color3)
print(color1)
print(color2 < color1)
print(color1 < color2)
color1.set_blue(140)
print(color1)
print(color1.get_blue())
color1.add_blue(140)
print(color1.get_blue())
color1.add_blue(100)
print(color1)
color2.set_green(25)
print(color2)
print(color3)
color3.add_green(-5)
print(color2 == color3)