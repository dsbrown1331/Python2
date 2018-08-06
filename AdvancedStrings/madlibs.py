#Use the matlib.txt file in Data/ to create a class that plays madlibs.
#The program should read in a .ml file to create a madlibs game.
#.ml files have header information (commented lines at the beginning that specify what type of word is
#required to fill in the blank).
#Your program should work for any .ml file




class MadLibs():

    def __init__(self, filename):
        """initialize Madlib class with a madlibs file to read"""
        self.madlibs_file = filename
        self.replacements = dict()   #dictionary to hold fill in the blank info

    def parse_header(self):
        """
        write a function that reads the header into a dictionary
        Print the result to check. The dictionary should look something like this
        {''{nn}' : 'noun', '{plnn}' : 'plural noun', etc...}
        """
        #TODO: read from each file and find all header lines (lines that start with #)

        #Hint:maybe use startswith("#"), split(",") strip() and slicing

        #for debugging
        print(self.replacements)


    def replace_keys(self, text):
        """return a copy of text with all parts of speech replaced with user input
        """
        new_text = text[:]
        for key in self.replacements:
            while new_text.find(key) != -1:
                #TODO: comment out the break
                break
                #TODO your code here to replace the first occurance of key with some input from the user
                #Note that the value of the key is what you can ask the user to type in
                #use new_text = new_text.replace() filling in the appropriate arguments
        return new_text


    def fill_in_blanks(self):
        """store the story as a string and add each line by reading from the file"""
        mad_story = ""
        reader = open(self.madlibs_file)
        for line in reader:
            mad_story += self.replace_keys(line)

        return mad_story



    def run(self):
        #parse header
        d = self.parse_header()
        #get story text and fill in the blanks line by line
        story = self.fill_in_blanks()
        print("="*20)
        print(story)
        print("="*20)


if __name__=="__main__":
    story_gen = MadLibs("../Data/madlib.ml")
    story_gen.run()
