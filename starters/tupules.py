# simple tupules
fruits = ('Apple', 'Banana', 'Orange')
print(fruits)

# tupules with Duplicates
fruitsBasket = ('Apple', 'Banana', 'Orange','Banana','Apple','Orange','Banana')
print(fruitsBasket)

# numbers tupules
numbers = (23, 45,12,65,3)
print (numbers)

# length using len
print(len(fruitsBasket))
print(len(numbers))

# type of tupules
print(type(fruits))
print(type(numbers))

# access the tupules
print(fruitsBasket[3])
print(fruitsBasket[3:6])
print(fruitsBasket[-4:-2])
print(fruitsBasket[-4])
print(fruitsBasket[-4:])

# change the tupules - cannot change the tuple as it is read only
# numbers[2] = 21 # replace the elements
# print(numbers)

# numbers.insert(3,56) # insert a new element in tupules
print(numbers)

# append - cannot append the tupule as it immutable so convert it to List then append it
# fruitsBasket.append("Mango")
# print(fruitsBasket)

fruitList = list(fruitsBasket)
fruitList.append("Kiwi")
print(fruitList)

# remove and pop
# fruitsBasket.remove("Banana")
# print(fruitsBasket)

# fruitsBasket.pop(3)
print(fruitsBasket)

# iterate tupules
for fruit in fruits:
     print(fruit)

# list comprehension
[print(fruit) for fruit in fruits]

# list comprehension with condition
[print(fruit) for fruit in fruits if 'O' in fruit]
[print(fruit) for fruit in fruits if 'Apple' in fruit]

# combine two tupules

mixed = fruits + numbers
print(mixed)