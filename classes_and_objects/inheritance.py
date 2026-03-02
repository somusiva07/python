class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print('Hello '+self.name) 

person1 = Person('Siva',43)
person1.greet()

# class Student(Person):
  #   pass

# stu1 = Student('Loke',13) 
# stu1.greet()

class Student(Person):
    def __init__(self,name, age, subject):
        super().__init__(name,age)
        self.subject = subject

    def welcome(self):
        print(f'Hello {self.name} : age : {self.age}  : fav subject : {self.subject}')    

stu1 = Student('Loke',12,"Maths") 
stu1.greet()
stu1.welcome()
