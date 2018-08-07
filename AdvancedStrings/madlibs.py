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
        reader = open(self.madlibs_file)
        for line in reader:
            if line.startswith("#"):
                if line.startswith("#-"):
                    continue
                else:
                    words = line.split(",")
                    key = words[0][1:]
                    value = words[1].strip()
                    self.replacements[key] = value

        #for debugging
        print(self.replacements)


    def replace_keys(self, text):
        """return a copy of text with all parts of speech replaced with user input
        """
        new_text = text[:]
        for key in self.replacements:
            while new_text.find(key) != -1:
                words = input("Type a " + self.replacements[key] + ": ")
                new_text = new_text.replace(key, words, 1)
        return new_text


    def fill_in_blanks(self):
        """store the story as a string and add each line by reading from the file"""
        mad_story = ""
        reader = open(self.madlibs_file)
        for line in reader:
            if not line.startswith("#"):
                mad_story += self.replace_keys(line)

        return mad_story



    def run(self):
        #parse header
        self.parse_header()
        #get story text and fill in the blanks line by line
        story = self.fill_in_blanks()
        print("="*20)
        print(story)
        print("="*20)


if __name__=="__main__":
    story_gen = MadLibs("../Data/madlib.ml")
    story_gen.run()
