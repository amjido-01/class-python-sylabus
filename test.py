class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
        
    def my_age(self):
        print(f'my age is {self.age}')


p1 = Person('john', 40)
p1.myfunc()