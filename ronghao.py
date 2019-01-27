from fileparser import pretty_print
import viewIndividual
import getfilepath
from os.path import isdir
from sys import exit
import fileparser
import metrics

#def viewMatchesOverall(profiles):

def top3profiles():
    profiles=str(raw_input("Enter name of the person you wish to view: "))
    viewIndividual.viewIndividual(profiles)
    

    return
    # Function 5: List the top 3 best matched students based on the overall
    # profiles information which may include all the personal information for
    # ranking. Note that you can define our own ranking metric. However, the
    # ranking metric must be reasonable
    




