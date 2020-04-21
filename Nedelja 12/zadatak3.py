class Movie:
    def __init__(self, name, category,balance, max_num_of_actors):
        print("Movie has been created")
        self.__name = name
        self.__category = category
        self.__actors =[]
        self.__balance=balance
        self.__max_num_of_actors=max_num_of_actors
    
    def get_name(self):
        return self.__name
    
    def get_category(self):
        return self.__category
    
    def get_balance(self):
        return self.__balance
    
    def get_max_num_of_actors(self):
        return self.__max_num_of_actors

    def set_name(self, name):
        self.__name = name
    
    def set_category(self, category):
        self.__category = category
    
    def set_balance(self, balance):
        if balance>=0:
            self.__balance = balance
        else:
            print("Unesi vrijednost veci od 0")
    
    def set_max_num_of_actors(self, max_num_of_actors):
        if max_num_of_actors>=0:
            self.__max_num_of_actors = max_num_of_actors
        else:
            print("Unesi vrijednost veci od 0")
    
    def add_actor(self,actor):
        if len(self.__actors)<self.__max_num_of_actors:
            self.__actors.append(actor)
            
        else:
            print("Dostignut je maksimalan broj glumaca!")
    
    def remove_actor(self,actor_name,actor_surname):
        for act in self.__actors:
            if act["name"].title()==actor_name.title() and act["surname"].title()==actor_surname.title():
                self.__actors.remove(act)
                
    
    def __str__(self):
        return f"name: {self.__name}, category: {self.__category}, balance: {self.__balance}"
    
    def can_pay_actor(self):
        plate=0
        for act in self.__actors:
            plate+=act["salary"]
        
        if plate<=self.__balance:
            return True
        else:
            return False
    
    def __gt__(self,other):
        if len(self.__actors)<len(self.__actors):
            return True
        else:
            return False

film1= Movie("Into the wild","adventure",250000,250)
film2=Movie("21 grams","triler",5000000,300)

glumac1={"name":"Janko","surname":"Jankovic","salary":330}
glumac2={"name":"Dejan","surname":"Babic","salary":550}
glumac3={"name":"Ivan","surname":"Ivanovic","salary":250}
glumac4={"name":"Ivan","surname":"Jankovic","salary":850}

film1.add_actor(glumac1)
film2.add_actor(glumac2)
film2.add_actor(glumac3)
film2.add_actor(glumac4)

film2.remove_actor("Ivan","Jankovic")

print(film2>film1)
print(film1)
print(film2)
    

