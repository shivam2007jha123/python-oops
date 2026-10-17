class animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class dog(animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks.")

class cat(animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        print(f"{self.name} meows.")

a=cat("tommy","white")
a.speak()
b=dog("rocky","german shepard")
b.speak()
c=animal("tiger")
c.speak()