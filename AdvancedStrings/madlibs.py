#Use the matlib.txt file in Data/ to create a class that plays madlibs.
#The program should read in a .ml file to create a madlibs game.
#.ml files have header information (commented lines at the beginning that specify what type of word is
#required to fill in the blank).
#Your program should work for any .ml file




class MadLibs():
    #TODO edit the init method so it takes a file as input when creating a MadLibs object
    def __init__(self):
        """initialize Madlib class with a madlibs file to read"""


    def parse_header(self):
        """
        write a function that reads the header into a dictionary
        Print the result to check. The dictionary should look something like this
        {''{nn}' : 'noun', '{plnn}' : 'plural noun', etc...}
        """
        header_dict = dict()

        #TODO: code here

        return header_dict

    def get_story(self):
        """store the story as a string by reading from the file"""
        story = ""

        #TODO: code here to read file

        return story

    def 

    def build_story(self):
        #parse header
        d = self.parse_header()
        #get story text
        story = get_story()
        #fill in the blanks
