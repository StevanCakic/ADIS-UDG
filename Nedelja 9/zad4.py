from zad3 import Color, valid

class AlphaColor(Color):
    def __init__(self, red, green, blue, alpha):
        super().__init__(red, green, blue)
        self.__alpha = alpha

    def get_alpha(self):
        return self.__alpha

    def set_alpha(self, new_alpha):
        if new_alpha>=0 and new_alpha<=1:
            self.__alpha = new_alpha
        else:
            print("Pogresan unos")

    def update_color_by_alpha(self, alpha):
        alpha_red = self.get_red() - self.get_red() * alpha
        alpha_green = self.get_green()-self.get_green()*alpha
        alpha_blue = self.get_blue()-self.get_blue()*alpha

        if valid(alpha_red) and valid(alpha_green) and valid(alpha_blue):
            self.set_red(alpha_red)
            self.set_green(alpha_green)
            self.set_blue(alpha_blue)
        else:
            print("Pogresan unos")

    def __str__(self):
        return f"red:{self.get_red()}, green:{self.get_green()}, blue:{self.get_blue()}, alpha:{self.__alpha}"

ac1 = AlphaColor(120,130,140,0.5)
ac2 = AlphaColor(23, 25, 44, 0.2)
ac3 = AlphaColor(23, 25, 44, 0.2)

print(ac1)
ac1.set_green(35)
print(ac1.get_green())
print(ac2 == ac3)
ac1.set_blue(20)
print(ac1.get_blue())

print(ac2.get_red())
ac2.update_color_by_alpha(0.3)
print(ac2.get_red())

ac3.set_alpha(0.45)
print(ac3.get_alpha())

ac2.update_color_by_alpha(15)
print(ac2.get_red())
ac2.add_red(-7)
print(ac2.get_red())

def get_from_csv():
    import csv

    with open("color.csv", "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        print(header)
        lista = []
        for i in reader: # next(reader)
            instanca = AlphaColor(i[0], i[1], i[2], i[3])
            lista.append(instanca)
        return lista

lista = get_from_csv()
for elem in lista:
    print(elem)
