def my_function():
  print("Hello from a function")

my_function()

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

def get_greeting():
  return "Hello from a function"

print(get_greeting())

def my_fname(fname):
  print(fname + " Refsnes")

my_fname("Emil")
my_fname("Tobias")
my_fname("Linus")

# can assign default values to parameters. If the function is called without an argument, it uses the default value:
def my_country(country = "Norway"):
  print("I am from", country)

my_country("Sweden")
my_country("India")
my_country()
my_country("Brazil")


def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

# lambda
def lambdafunc(n):
  return lambda a : a * n

mydoubler = lambdafunc(2)
mytripler = lambdafunc(3)

print(mydoubler(11))
print(mytripler(11))