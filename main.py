from fileparser import pretty_print
import getfilepath
from os.path import isdir
from sys import exit
import metrics

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
    #pretty_print(profiles)

    #========================================
    
    
    def main():
        menu = raw_input('''Welcome to automatic friend finder. Press 5 to find top 3 profiles
Enter input: ''')
        if menu == '1':
            yongjie.viewProfiles(profiles)
        elif menu == '2':
            # Function 2
            yongjie.viewMatchesCountry(profiles)
        elif menu == '3':
            # Function 3
            yongjie.viewMatchesLikesDislikes(profiles)
        elif menu == '4':
            # Function 4
            jiale.viewMatchesBooks(profiles)
        elif menu == '5':
            # Function 5
            ronghao.top3()
        elif menu == '6':
            # Function 6
            william.storeCSV()
        else:
            print("Invalid input")

    main()
            
            

    # Function 1,2,3 (Based on Project 1 Description.pdf)
    #yongjie.viewProfiles(profiles)
    #yongjie.viewMatchesCountry(profiles)
    #yongjie.viewMatchesLikesDislikes(profiles)

    # Function 4
    #jiale.viewMatchesBooks(profiles)

    

    # Function 6
    #william.storeCSV()

    # Open function
    #kijoon.openFunction(profiles)




