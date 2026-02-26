# simple sets
fruits = {'Apple', 'Banana', 'Orange'}
print(fruits)

# sets with Duplicates is not possible
# fruitsBasket = {'Apple', 'Banana', 'Orange','Banana','Apple','Orange','Banana'}
# print(fruitsBasket)

# numbers set
numbers = {23, 45,12,65,3}
print (numbers)

# length using len
print(len(fruits))
print(len(numbers))

# type of sets
print(type(fruits))
print(type(numbers))

# cannot access the sets by referring its index
# print(fruitsBasket{3})
# print(fruitsBasket{3:6})

# But it is possible with iterate for loop
for x in fruits:
    print(x)

# change the sets is not possible
# numbers{2} = 21 # replace the elements
# print(numbers)

numbers.add(82) # insert a new element in sets
print(numbers)

# remove
numbers.remove(82)
print(numbers)

# remove and pop
# fruitsBasket.remove("Banana")
# print(fruitsBasket)

# fruitsBasket.pop(3)
# print(fruitsBasket)

# iterate sets
# for fruit in fruits:
#     print(fruit)

# list comprehension
# {print(fruit) for fruit in fruits}

# list comprehension with condition
# {print(fruit) for fruit in fruits if 'O' in fruit}
# {print(fruit) for fruit in fruits if 'Apple' in fruit}

# Sort order
# thislist = {"Orange", "mango", "Kiwi", "pineapple", "banana"}
# thislist.sort()
# print(thislist)

# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

# combine two sets

# mixed = fruits + numbers
# print(mixed)