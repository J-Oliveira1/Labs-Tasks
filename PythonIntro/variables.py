# Task 1- Age
# -Declare a variable and store your age in that variable. 
# -Use string interpolation to format a message to the console utilizing the
# previously declared variable. Print to the console “I am XX years old”, where
# XX represents the value of your age. You cannot *hard-code the value of your
# age in the string. 

age = 32

print(f'I am {age} years old!')

# Task 2- First Name
# - Declare a variable to store the string value of your first name.
# - Use the built-in Python input() function to retrieve the first name value via
# user input. 
# - The input () function allows a user to input a value before executing the
# next line of code. After inputting a value and pressing 'enter’, the value 
# will be returned to wherever the input() function was called.

firstname = input("What is your first name?")
print(firstname)

# Task 3- Last Name
# - Declare a variable to store the string value of your last name.
# - Use the built-in Python input() function to retrieve the last name value via 
# user input.

lastname = input("What is your last name?")
print(lastname)

# Task 4- Full Name
# - Use string concatenation to take the value stored in your first name 
# variable (Question 2) and the value stored in your last name variable 
# (Question 3) and “combine” them together to be stored in a new variable.
#     *Example expected out: “Michael Terrill”
# - Use string interpolation to format a message to the console utilizing the
# previously declared variables. Print to the console “My first name is FF
# and my last name is LL, which means my full name is FN”, where FF 
# represents your first name value, LL represents your last name value, and 
# FN represents the concatenated full name value. You cannot hard-code 
# the values in the string.
#     *Example expected output: “My first name is Michael and my last
#     name is Terrill, which means my full name is Michael Terrill”

full_name = firstname + ' ' + lastname
print(full_name)


print(f" My first name is {firstname} and my last name is {lastname}, which means my full name is {full_name}.")

# Task 5- Temperature Converter
# - Declare a variable to store a Fahrenheit temperature.
# - Convert the stored Fahrenheit temperature to Celsius and store the
# converted temperature in a variable.
#     * Research is a big part of being a developer. A good search term to
#     use: “Fahrenheit to Celsius formula”. 
#     * HINT: You will need to use a few arithmetic operators to make the
#     conversion, and your VALUES will be numbers, not strings.
#     * The reason this is a good search term for your research is because it 
#     will give you the formula you need to put in your code to achieve 
#     your goal, opposed to doing the conversion for you.
# - Print to the console “FF degrees Fahrenheit is CC degrees Celsius”, 
# where FF represents the degrees in Fahrenheit and CC represents the
# degrees in Celsius. You cannot hard-code the values in the string.

fahrenheit = 80
print(fahrenheit)

celsius = fahrenheit - 32 * 5/9
print(celsius)

print(f"{fahrenheit} degrees Fahrenheit is {celsius} degrees Celsius.")

# Extra Tasks-

age = input("How old are you?")

if age == 18:
    print("You cna get on this ride!")

else:
    print("Sorry you can not get on this ride!")








