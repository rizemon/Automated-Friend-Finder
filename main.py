
from fileparser import pretty_print
import getfilepath
from os.path import isdir
from sys import exit


import yongjie
from yongjiefuncs import clear_shell, integer_input
import calluser
import ronghao
import kijoon
import jiale
import william

def read_profiles():
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
    # pretty_print(profiles)
    return profiles


    # Function 1,2,3 (Based on Project 1 Description.pdf)
def selected_user_menu(user_profile, profiles):
    #  show menu after user selected the profiles.
    # except for logged in user profile wont be visable in the options.
    while True:
        clear_shell()
        print("1- View all profile\n")
        print("2- View  profiles by countries \n")
        print("3- View profiles by likes \n")
        print("4- View profiles by dislikes\n")
        print("0- Logout")

        menu_number = integer_input("Enter menu number e.g 1 from menu 0 to quit")

        if menu_number == 0:
            # return to previous state when 0 is selected
            return
        elif menu_number == 1:
            yongjie.view_profiles(profiles)
        elif menu_number == 2:
            yongjie.matched_by_countries(user_profile=user_profile, profiles=profiles)
        elif menu_number == 3:
            yongjie.matched_likes(user_profile=user_profile, profiles=profiles)
        elif menu_number == 4:
            yongjie.matched_dislikes(user_profile=user_profile, profiles=profiles)

def menu():
    # Main function to start the application.
    while True:
        print("1- Select A User As\n")
        print("2- Register \n")
        menu_number = integer_input("Enter menu number e.g 1 from menu 0 to quit")
        if menu_number == 0:
            return
        elif menu_number == 1:
            profiles = read_profiles()
            user_profile = calluser.select_user(profiles)
            selected_user_menu(user_profile=user_profile, profiles=profiles)
        elif menu_number == 2:
            calluser.add_new_user()
        else:
            print("please enter again")
        clear_shell()

    # Function 4
    jiale.viewMatchesBooks(profiles)

    # Function 5
    ronghao.viewMatchesOverall(profiles)

    # Function 6
    william.storeCSV()

    # Open function
    kijoon.openFunction(profiles)



if __name__ == "__main__":
    menu()
