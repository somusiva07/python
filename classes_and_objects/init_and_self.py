
# All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

# The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # The self parameter is a reference to the current instance of the class.
    def greet(self):
        print('Hello '+self.name)


stu1 = Student('Siva',13); 
stu2 = Student('Pri',12);
stu3 = Student('Loke',6); 

print(stu1.name, stu1.age)
print(stu2.name, stu2.age)
print(stu3.name, stu3.age)

stu1.greet()

# Access multiple properties using self:
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()