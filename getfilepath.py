import sys
import os
import glob
import main


def restart_program():
    # Restarts the current program.
    # Note: this function does not return. Any cleanup action (like
    # saving data) must be done before calling this function.
    python = sys.executable
    os.execl(python, python, * sys.argv)


# Opens path.txt to check if path has been setup, if not then prompt user
# for path leading to folder storing all the profiles
file = open("path.txt", "r")
pathSelected = file.read()
file.close()

# If it is false, prompt user to enter folder path

if(pathSelected == "false"):
    print('Path is not intialized yet')
    fileDirec = raw_input(
        "File directory has not been set up yet, please choose the folder with profile data:")
    file = open("path.txt", "w")
    file.truncate(0)
    file.write(fileDirec)
    file.close()
    file = open("path.txt", "r")
    print("File path set to: {}".format(fileDirec))
    file.close()
    restart_program()
else:
    print("Path file detected, attempting to open now. Please wait for awhile")
    try:
        if(os.path.isdir(pathSelected)):
            files = glob.glob(pathSelected + '\\*')
            for name in files:
                try:
                    with open(name) as f:
                        main.parse(f)
                except Exception as e:
                    print(e)
            main.pretty_print(main.profiles)
    except Exception as e:
        print(e)
