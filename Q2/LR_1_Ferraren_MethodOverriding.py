class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

    def eat(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return self.name + " roars loudly!"

    def eat(self):
        return self.name + " eats fresh meat."


class Elephant(Animal):
    def make_sound(self):
        return self.name + " trumpets!"

    def eat(self):
        return self.name + " eats grass and fruits."


class Monkey(Animal):
    def make_sound(self):
        return self.name + " chatters!"

    def eat(self):
        return self.name + " eats bananas."


lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())
print(lion.eat())
print("-----")

print(elephant.make_sound())
print(elephant.eat())
print("-----")

print(monkey.make_sound())
print(monkey.eat())
print("-----")
