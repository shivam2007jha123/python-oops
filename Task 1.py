class Vehicle:
    def __init__(self, name, model, year): #explaination :- it work as a initializer of each thing
        self.name = name
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.name} {self.model}"

a=Vehicle("BMW","M5",2015)
print(a.display_info())
b=Vehicle("audi","A5",2010)
print(b.display_info())  

