# Problem Solving 1-
# Task 1- 
favorite_number = 20

# Task 2-
import random
random_number = random.randint(0,100)
difference_number = random_number - favorite_number
print(difference_number)


# Task 3-
count = 1
random_number = random.randint(0,100)

while random_number != favorite_number:
    random_number = random.randint(0,100)
    count += 1 

print(f"It took the computer {count} guesses to find your favorite number!")