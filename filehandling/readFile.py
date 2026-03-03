# f = open('demo.txt')
# print(f.read())
# f.close() #good practice to close

# with no need to close
# with open("demo.txt") as f:
#   #print(f.readline())
#     for x in f:
#         print(x)

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content        


# with open('demo.txt','a') as f:
#     f.write('This will the last line')
# with open('demo.txt','r') as f:    
#     for x in f:
#         print(x)

import os
if os.path.exists("demoFile.txt"):
  os.remove("demoFile.txt")
else:
  print("The file does not exist")            