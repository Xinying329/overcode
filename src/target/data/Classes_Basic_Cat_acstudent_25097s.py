class Cat:
    def _init_ (self, name, age):
        self.name = name
        self.age = age
    def _str_(self):
        return "name: " + name + ", age: " + age
c = Cat("Fluffy", 3)
print(c)
print(c.make_sound())

