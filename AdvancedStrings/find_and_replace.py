song = "The ants go marching one by one. Hurrah! Hurrah!"

#find the location of ants
i = song.find("ants")
print("'ants' starts at index ", i)
#use index from find to print' ants'
print(song[i:i + len("ants")])

#what is the default index if the string can't be found?
j = song.find("taco")
print("taco starts at index", j)

#replace all occurances of one by two
second_verse = song.replace("one", "two")
print(second_verse)

#replace first occurance of Hurrah
messed_up = second_verse.replace("Hurrah", "Boohoo", 1)
print(messed_up)

#check if a string starts with something
if song.startswith("The ants"):
    print("Do we have to sing this song again?")
