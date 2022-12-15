# Task 1 - Five Hellos
# -Write a for loop that will run five times and print
# “hello!” to the console five times.

counter = 0
while(counter <5):
    print("Hello")
    counter += 1

# # Task 2- Counting
# # - Write a for loop that counts from 0 to 10, with each 
# # number being print to the console one at a time

for number in range(11):
    print(number)

#  Task 3- Counting Backwards
# - Write a for loop that counts from 10 to 0, with each
# number being printed to the console one at a time.
# HINT: When calling the range function provide three
# arguments “range(start number, stop number, step number)”

for number in range(10, -1, -1):
    print(number)

# Task 4- Prompted Output
# - Write a for loop that will run as many times as a
# user wants, with each iteration printing 
# “devCodeCamp” to the console. 
# HINT: you will need to use the Python input() function to gather user input

print()
number_of_loops = input("How many times do you want to loop? ")
(number_of_loops) = int(number_of_loops)
for num in range(number_of_loops):
    print("DevCodeCamp")


# Task 5- Packers Split-Up
# - Write a for loop that will print each character of the string “Packers” to the console. 

nfl_team = "Packers"

for char in nfl_team:
    print(char)

# Task 7- Five Hellos (again)
# - Write a while loop that will run five times and print
# “hello!” to the console five times

counter = 0
while(counter <5):
    print("Hello")
    counter += 1

# Task 8- Validation
# - Write a while loop that will prompt a user for 
# their password and will continue to prompt the
# user until the typed in password is correct. If
# correct, print to the console “User Validated”

while True:
    password = input("Password please! ")
    if password == "DevCode":
        print("User validated! ")
        break


    














