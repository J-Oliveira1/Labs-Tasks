from implementation import months_of_year
print(months_of_year[2])

from implementation import fruits_and_veggies
new_fruits_and_veggies = {"fig", "watermelon", "carrots", "lettuce"}
fruits_and_veggies.update(new_fruits_and_veggies)
for fruit in fruits_and_veggies:
    print(fruit)

from implementation import imediate_family

for person in imediate_family:
    print(person['first_name']+ " : " + person["relation_to_me"])