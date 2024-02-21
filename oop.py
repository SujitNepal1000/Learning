# class

class Dog:
    def __init__(self, name):
        self.name = name
        
    def bark(self):
        print("bark bark")
        
    def get_name(self):
        return self.name
    

my_dog = Dog("doggy")
print("{} is my dog".format(my_dog.get_name()))
my_dog.bark()

# finding the area of rectangle creating class

class Rectangle:
    def __init__(self,width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
rect1 = Rectangle(5, 4)
print(rect1.area())

#inheritance

#single inheritance

class parent:
    def display(self):
        print(" this is parent class")
        
class child(parent):
    pass

child1 = child()
child1.display()

#multiple inheritance
class parent1:
    def display1(self):
        print("this is parent1")

class parent2:
    def display2(self):
        print("this is parent2")
        
class child(parent1, parent2):
    pass

child1 = child()
child1.display1()
child1.display2()

# multi level inheritance
class grandfather:
    def display(self):
        print("this is grandfather")
        
class father(grandfather):
    def display1(self):
        print("this is father")
        
class child(father):
    pass
        
child1 = child()
child1.display()
child1.display1()


# # que creating a class employee as a parent class and creating a subclass as a developer and manager with attributes such as name, id and salary.also calculating bonus for both the classes.

class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def bonus(self):
        return self.salary * 0.10

class developer(Employee):
    def bonus(self):
        return self.salary * 0.20
    
class manager(Employee):
    def bonus(self):
        return self.salary * 0.30

dev1 = developer("John", 123456, 50000)
mang1 = manager("Doe", 123457, 50000)

print("developer bonus is: ", dev1.bonus())
print("manager bonus is: ", mang1.bonus())

## polymorphism
class animal:
    def __init__(self,name):
        self.name = name
        
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        return "woof"
    
class cat(animal):
    def sound(self):
        return "meow"
    
dog1 = dog("doggy")
cat1 = cat("kitty")

print(dog1.name)
print(dog1.sound())
print(cat1.name)
print(cat1.sound())
        