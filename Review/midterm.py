##################
#Lists and loops
##################

fruits = ["apples", "oranges", "grapes"]
for fruit in fruits:
    print(fruit)


#1. use a for loop to print out each fruit in fruits

name = "Daniel"


#2. use a for loop to print out each character in name
for i in name:
    print(i)

sentence = "The ants go marching one by one"


#3. use a for loop to print out each word in sentence
for word in sentence.split():
    print(word)


###############
#Dictionaries
##############

d = {"a":1,"b":2,"c":3}

###################################
#Without editing the above code:

#1. add the key "d" with value 4 and
d["d"] = 4
#2. delete the key "b" from the dictionary
del d["b"]
#d.pop("b")

#3. use a for loop to print all the keys
for key in d:
    print(key)

#4. use a for loop to print all the values
for key in d:
    print(d[key])

#5. create an empty dictionary d_rev and use a for loop
#to store put the reverse of d in d_rev (i.e., make 1 map to "a", etc. )
d_rev = dict()
for key in d:
    value = d[key]
    d_rev[value] = key
print(d_rev)


#############################
d_l = {"file1.txt":["See", "spot"],
       "file2.txt": ["Jack", "and", "Jill"]}
#############################
#without editing the above code

#1. append "run" to the value for key "file1.txt"
d_l["file1.txt"].append("run")
print(d_l)

#2. append "ran up the hill" to the value of for the key "file2.txt"
d_l["file2.txt"].append("ran up the hill")


#3. print(d_l)
# you should get something like
#{"file1.txt":["See", "spot", "run"], "file2.txt": ["Jack", "and", "Jill", "ran up the hill"]}
print(d_l)

##############################
char_cnt = dict()
word_cnt = dict()
song = "the ants go marching one by one"
##############################

#1. write code to store in char_cnt how many times each character
# in song occurs
for char in song:
    #char_cnt[char] = char_cnt.get(char, 0) + 1
    if char not in char_cnt:
        char_cnt[char] = 1
    else:
        char_cnt[char] += 1

print(char_cnt)

#2. write code to store in word_cnt how many times each word appears in song
for word in song.split():
    word_cnt[word] = word_cnt.get(word, 0) + 1
print(word_cnt)
