car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car)

print(car["model"])

# key value pair
# duplicates are not allowed
# ordered from 3.7

print(len(car))

key = car.keys()

print(key) #before the change

car["color"] = "white"

print(key) #after the change

val = car.values()

print(val) #before the change

car["year"] = 2020

print(val) #after the change

car.update({"year": 2020})

print(car)

for x in car:
  print(x)
  print(car[x])

# Loop through both keys and values, by using the items() method:
for x, y in car.items():
  print(x, y)  