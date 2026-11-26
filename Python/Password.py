p = input("Enter a password to check: ")

length = len(p) >=8
upper = False
lower = False
digit = False
special = False



for char in p:
  if char.isupper():
    upper = True
  elif char.islower():
    lower = True
  elif char.isdigit():
    digit = True
  else:
    special = True

if length and upper and lower and digit and special :
  print("Success! Your password has passed")
else:
  print("Password is too weak! It must contain:")
  if not length:
    print("At least 8 characters")
  if not upper:
    print("At least 1 uppercase letter")
  if not lower:
      print('At least 1 lowercase letter')
  if not digit:
      print("At least 1 digit")
  if not special:
      print("At least 1 special character")

      