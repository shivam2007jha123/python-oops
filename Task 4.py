class animal:
    def speak(self):
        print("Animal makes a sound")

class dog(animal):
    def speak(self):
        print("Dog barks")
a=dog()
a.speak()
