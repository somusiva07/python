# simple lists
fruits = ['Apple', 'Banana', 'Orange']
print(fruits)

# lists with Duplicates
fruitsBasket = ['Apple', 'Banana', 'Orange','Banana','Apple','Orange','Banana']
print(fruitsBasket)

# numbers list
numbers = [23, 45,12,65,3]
print (numbers)

# length using len
# print(len(fruitsBasket))
# print(len(numbers))

# type of lists
# print(type(fruits))
# print(type(numbers))

# access the lists
# print(fruitsBasket[3])
# print(fruitsBasket[3:6])
# print(fruitsBasket[-4:-2])
# print(fruitsBasket[-4])
# print(fruitsBasket[-4:])

# change the lists
numbers[2] = 21 # replace the elements
print(numbers)

numbers.insert(3,56) # insert a new element in lists
print(numbers)

# append
fruitsBasket.append("Mango")
print(fruitsBasket)

# remove and pop
# fruitsBasket.remove("Banana")
# print(fruitsBasket)

# fruitsBasket.pop(3)
# print(fruitsBasket)

# iterate lists
# for fruit in fruits:
#     print(fruit)

# list comprehension
# [print(fruit) for fruit in fruits]

# list comprehension with condition
# [print(fruit) for fruit in fruits if 'O' in fruit]
# [print(fruit) for fruit in fruits if 'Apple' in fruit]

# Sort order
thislist = ["Orange", "mango", "Kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

fruitsBasket.sort()
print(fruitsBasket)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# combine two lists

mixed = fruits + numbers
print(mixed)