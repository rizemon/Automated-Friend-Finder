import os
import main

# This method gets the file directory and prints them with main.py


def printData(fileDirec):
    files = os.listdir(fileDirec)
    for filename in files:
        with open(os.path.join(fileDirec, files[0]), "r") as f:
            main.parse(f)
            f.close()


# Try to check if path.txt is present if not it will create
# the path for them in the current directory and will ask for
# the path for the profiles folder which will write to path.txt
# which can be used in future intializations
try:
    file = open("path.txt", "r")
    pathDirec = file.read()
    printData(pathDirec)
except IOError:
    f = open(os.path.join('path.txt'), 'w')
    print("Path to profiles not set yet.")
    fileDirec = raw_input(
        "File directory has not been set up yet, please choose the folder with profile data:")
    print("File path set to: {}".format(fileDirec))
    f.write(fileDirec)
    f.close()
    file = open("path.txt", "r")
    pathSelected = file.read()
    printData(pathSelected)
    f.close()
