def print_line():
    print('- ' * 10)

# create a mapping of state to abbreviation
states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}
# create a basic set of states and some cities in them
cities = {
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
}
# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print_line()
print("{} is in NY State: ".format(cities['NY']))

# print some states

print("Michigan's abbreviation is: ", states['Michigan'])

# do it by using the state then cities dict
print_line()
print("{} is in Florida".format(cities[states['Florida']]))

# print every state abbreviation
print_line()
for state, abbrev in states.items():
    print("{} is abbreviated as {}".format(state, abbrev))

# print every city in state
print_line()
for abbrev, city in cities.items():
    print("{} has the city {}".format(abbrev, city))

# now do both at the same time
print_line()
for state, abbrev in states.items():
    print("{} state is abbreviated {} and has city {}".format(
state, abbrev, cities[abbrev]))

#here is how you delete from a dictionary
del states['Oregon']
#now we can print out the dictionary and the "Oregon" key is gone
print(states)

print_line()
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)
if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is {}".format(city))
