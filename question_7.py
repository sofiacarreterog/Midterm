import random

# Create a list and fill it with 10 random numbers between 1 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

print("Original list:", random_numbers)
modified_list = [] # Create a new list to store modified values
# Iterate over the list and modify values
for num in random_numbers:
    if num % 2 == 0:  # Check if the number is even
        modified_list.append(num * 2)  # Double the even numbers
    # If the number is odd, it gets removed

print("Modified list:", modified_list)
