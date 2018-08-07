some_guy = 'Fred'

first_names = []
first_names.append(some_guy)

#check object equality
print(some_guy is first_names[0])

#doesn't create a new object
another_list_of_names = first_names
another_list_of_names.append('George')
some_guy = 'Bill'

print (some_guy, first_names, another_list_of_names)
