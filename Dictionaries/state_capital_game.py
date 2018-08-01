def get_state_capitals(filename):
    reader = open(filename)
    for line in reader:
        words = line.split(",")
        capital = words[0].strip()
        state = words[1].strip()
        #debug print line
        print("The capital of {} is {}".format(state, capital))
    #TODO: return a dictionary mapping from states to capitals
    #return put_your_dict_here

state_cap_dict = get_state_capitals("../Data/state_capitals.csv")
#TODO: use the dictionary to create a state capital
#guessing game where the game asks you to name the capital of a state
#simply iterate through the items in the dictionary


#pick a random key value to get a state and ask user for capital
#write code to check if answer is correct
#output whether they are right or what the correct answer is


#Bonus: use a while True: so you can quiz someone until they want to quit


#Bonus: randomly decide whether to ask for the capital of a state or the
#to ask for the State given a capital
