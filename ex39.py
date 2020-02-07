# Dictionaries, Oh Lovely Dictionaries
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = "New York"
cities['OR'] = 'Portland'

print('-' * 10)
print("NY state has : ", cities['NY'])
print("OR state has : ", cities['OR'])

print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} is abbreviated {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev} ,", end = ' ')
    print(f"and has city {cities[abbrev]} !")

print('-' * 10)
state = states.get("Texas")
if not state:
    print("Sorry, no Texas !")

print('-' * 10)
city =cities.get('TX','Does Not Exist')
print(f"The city for the state TX is : {city}")


# Study Drills

# What is the difference between a list and a dictionary? 
#     A list is for an ordered list of items. 
#     A dictio- nary (or dict) is for matching some items (called “keys”) to other items (called “values”).