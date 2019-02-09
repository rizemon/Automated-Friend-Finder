from fileparser import pretty_print
import getfilepath
from os.path import isdir
from sys import exit

import yongjie
import ronghao
import kijoon
import jiale
import william

if __name__ == "__main__":
    # Get directory of profiles
    directory = getfilepath.getFilePath()

    # If directory does not exist, exit the program
    if not isdir(directory):
        print "Invalid directory!"
        exit(0)
    print "Reading profiles from %s now..." % directory

    # Read the profiles and store in profiles dictionary
    profiles = getfilepath.getProfiles(directory)
    # For debugging purposes
    pretty_print(profiles)

    # Function 1,2,3 (Based on Project 1 Description.pdf)
    yongjie.viewProfiles(profiles)
    yongjie.viewMatchesCountry(profiles)
    yongjie.viewMatchesLikesDislikes(profiles)

    # Function 4
    # jiale.viewMatchesBooks(profiles)
    matches_books = jiale.getMatchesBooks(profiles)
    # Print top three for each person based on books
    for name in profiles:
        print "%s's top three based on books: %s" % (name, jiale.getTopThree(name, matches_books))

    # Function 5
    ronghao.viewMatchesOverall(profiles)

    # Function 6
    william.storeCSV()

    # Open function
    kijoon.openFunction(profiles)









