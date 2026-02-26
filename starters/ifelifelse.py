num1 = 5
num2 = 10

if (num1 > num2):
    print('num 1 is greater')
elif(num2 > num1):
    print('num 2 is greater')       
else:
    print('num1 and num2 are equal')

username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")         
