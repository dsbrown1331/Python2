def get_state_capitals(filename):
    reader = open(filename)
    for line in reader:
        words = line.split(",")
        capital = words[0].strip()
        state = words[1].strip()
        #debug print line
        print("The capital of {} is {}".format(state, capital))
    #TODO: return a dictionary


get_state_capitals("../Data/state_capitals.csv")
#TODO: use the dictionary to create a state capital
#guessing game
