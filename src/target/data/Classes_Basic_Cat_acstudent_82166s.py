class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "name: " + self.name + ", age: " + str(self.age)

def main():
    c = Cat("Fluffy", 3)
    print(c)
    print(c.make_sound())

main()


