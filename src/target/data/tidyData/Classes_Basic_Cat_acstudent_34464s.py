class Cat:
    def __init__(c,name,age):
        c.name=name
        c.age=age
    def __str__(c):
        return "name: "+c.name+", age: "+c.age
    def make_sound():
        return "Meow"
c=Cat("Fluffy",3)
