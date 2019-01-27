from fileparser import pretty_print
import getfilepath
from os.path import isdir
from sys import exit

directory = getfilepath.getFilePath()

#def viewMatchesOverall(profiles):
def viewMatchesOverall(profiles):
    # Function 5: List the top 3 best matched students based on the overall
    # profiles information which may include all the personal information for
    # ranking. Note that you can define our own ranking metric. However, the
    # ranking metric must be reasonable
    viewIndividual(profiles)
    f = open(filename, "r")
    print (f.read())
    return



#Function: viewIndividual
#is to translate input from "profile name (Michael Jackson)" to "filename (1)"

print directory
def viewIndividual(profiles):
    global filename
    
    if profiles == "Michael Jackson":
        filename = (directory + "\\1.txt")
    elif profiles == "Carol":
        filename = (directory + "\\2.txt")
    elif profiles == "Kevin":
        filename = (directory + "\\3.txt")
    elif profiles == "Rose":
        filename = (directory + "\\4.txt")
    elif profiles == "Shelley":
        filename = (directory + "\\5.txt")
    #elif profiles == "Michael Jackson":
    #    filename = (directory + "\\6.txt")
    elif profiles == "Joel Jackson":
        filename = (directory + "\\7.txt")
    elif profiles == "Jenny Wang":
        filename = (directory + "\\8.txt")
    elif profiles == "Angela Little":
        filename = (directory + "\\9.txt")
    elif profiles == "Lisa Marie":
        filename = (directory + "\\10.txt")
    elif profiles == "Teresa":
        filename = (directory + "\\11.txt")

    #print filename
    return filename

profiles=str(raw_input("Enter name of the person you wish to view: "))
viewMatchesOverall(profiles)

