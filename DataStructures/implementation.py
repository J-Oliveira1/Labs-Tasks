# Task 1: Dictionary, Set and Tuple
# Given the following three scenarios, choose the best data structure (between a
# dictionary, set, or tuple) to efficiently store the data. Each scenario ties directly to
# one data structure. Each data structure will be used only once. You will need to
# determine which data structure is best for which scenario, and then implement the
# data structure in Python.

# 1- Store the months of the year as strings. Determine the month in the data
# structure in which National Pi Day exists and print that month to the console.
#     a) HINT: The number for Pi, when converted to an Integer, is related to the
#     stored location of the correct month.
# TUPLE
months_of_year = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
print(months_of_year[2])

# 2- Store five fruits or vegetables.
#     a) Add two of your favorite fruits and two of your favorite vegetables to the collection.
#     b) Iterate over the collection and print each one to the console.
# SET
fruits_and_veggies = {"apple", "orange", "pineapple", "mango", "peach"}
print(fruits_and_veggies)

new_fruits_and_veggies = {"fig", "watermelon", "carrots", "lettuce"}
fruits_and_veggies.update(new_fruits_and_veggies)
for fruit in fruits_and_veggies:
    print(fruit)

# 3- Store information about a user profile. Use literal string interpolation to
# print the user’s profile information to the console. The profile should
# consist of the following information:
# DICTIONARY

# a. First Name
# b. Last Name
# c. Email Address
# d. Phone Number

user_profile = {
    "first_name": "Joseph",
    "last_name": "Oliveira",
    "email_address": "J12090@gmail.com",
    "phone_number": "973-759-2628"
}
for key, value in user_profile.items():
    print(f"{key} : {value}")

# Task 2: List of Dictionaries
# Use a list to store the dictionary of your immediate family members, with each index
# of the list storing its own dictionary. Dictionary should contain the following keys:
# *First name
# *Last name
# *Relation to you
# Once you have stored the List of Dictionary items, write a function/method that will
# iterate over the List and print off the First Name and Relation of each person in the List.

imediate_family = [
    {
        "first_name": "Mirela",
        "last_name": "Kurspahic",
        "relation_to_me": "finace`"
    },
    {
        "first_name": "Luziann",
        "last_name": "Montero",
        "relation_to_me": "sister"
    },
    {
        "first_name": "Chris",
        "last_name": "Markle",
        "relation_to_me": "cousin"
    }
]

for person in imediate_family:
    print(person['first_name']+ " " + person["relation_to_me"])