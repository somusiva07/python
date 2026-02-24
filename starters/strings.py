name = 'Hello World'

print(name)

# print(name[3])

# print(len(name))

# for n in name:
#    print(n)

# Get the characters from position 2 to position 5 (not included):    
print(name[2:5])

# Get the characters from the start to position 5 (not included):
print(name[:5])

# Get the characters from the start to end:
print(name[2:])

# Use negative indexes to start the slice from the end of the string:
print(name[-5:-2])

# Upper
print(name.upper())

# Lower
print(name.lower())

# Upper
print(name.split())

# replace
print(name.replace('o','s'))

# concat
hai = "Hai"

print(name + hai)

print(name +" "+ hai)

# Create an f-string:
age = 36
txt = f"My name is John, I am {age}"
print(txt)