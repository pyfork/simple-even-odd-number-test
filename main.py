# Get number from user
number = input("\nEnter a number\n")

# Change input type to integer for boolean test
num_int = int(number)

# Use if else to customize reply based on even number test
if num_int % 2 == 0:
  print("That's an even number")
else: 
  print("That's an odd number")