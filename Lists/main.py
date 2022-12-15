# Task 1: Accessing a Value
# - Create a list with the following items: “JavaScript”, “Python”, “Java”, “Django”, “React”
# Then print the second item in the list.

programs = [ ' JavaScript', 'Python', 'java', 'Django', 'React'] 
print(programs[1])

# Task 2: Adding and Changing Values
# - Create a list with the following instructors: “Nevin”, “Mike”, “Jake”, “Dan”, “Megan”.
# Now add three more instructors: “Dan”, “James”, “John-Boy”
# Since we now have two “Dan’s” change one of them to “Danimal” then print the results. 

instructors = ['Nevin', 'Mike', 'Jake', 'Dan', 'Megan']
print(instructors)
instructors.append("Dan")
instructors.append("James")
instructors.append('John-Boy')
print(instructors)
instructors[3] = 'Danimal'
print(instructors)

# Task 3: Popping a Value
# - Using the combined list of the instructors from the previous exercise, John-Boy 
# decided that teaching isn’t for him, so we need to “pop” him off of the list and print 
# the results.

eliminate_one = instructors.pop()
print(instructors)

# Task 4: Removing a Value
# - Mike was recently promoted to a new managing role! We need to remove him from 
# the list of instructors. Then print the results

instructors.remove('Mike')
print(instructors)

# Task 5: Looping over a List
# Create two lists:
# List 1: “fan”, “bull-”, “high-“, “barrel-o-“, “slap”
# List 2: “dango”, “rider”, “horse”, “monkeys”, “stick”
# Loop over the first list and take the corresponding element from the second list and
# concatenate the two elements into a new string and print the result for each new string.
# e.g.: “fandango”, “bull-rider”, etc.

words = ['fan', 'bull-', 'high-', 'barrel-o-', 'slap']
characters = ['dango', 'rider', 'horse', 'monkeys', 'stick']

new_line = len(words)

for element in range(new_line):
    word = words[element]
    character = characters[element]
    print(word + character)

# Task 6: List Function
# - Given the list of instructors so far, we realized that we may have missed adding a few
# instructors. Since the List will allow duplicate entries, but we want to have unique
# names for each of our instructors, we need to write code that makes sure we are not
# adding duplicate entries.
# Create two variables, a List and a string first name that you want to add to the List.
# Create a boolean variable that you can check to see if a duplicate entry has been found.
# Loop over the list and compare each element with the provided name.
# At the end of the loop, if no duplicate entry has been found, then append the new 
# name to the list, then print out the list and print the length of the list.
# If a duplicate entry was found, print out the message: “Sorry that name has been
# taken, please provide a nickname”.
# Run this code three times, once to add “Brett”, once to add “Pascal” and finally to add “James”.

















