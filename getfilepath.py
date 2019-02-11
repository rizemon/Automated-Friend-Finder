from os import listdir
from os.path import join
import fileparser


def getProfiles(fileDirec):

<<<<<<< HEAD
    # Takes in the directory path, read the profiles in them and return all the profiles
=======
    # Takes in the directory path, read the profiles in them and
    # return all the profiles
>>>>>>> 5398629a56f1780be80f1783f39953654aef11a0

    profiles = {}
    files = listdir(fileDirec)
    for filename in files:
        with open(join(fileDirec, filename), "r") as f:
            name, profile = fileparser.parse(f)
            profiles[name] = profile
            f.close()
    return profiles


def getFilePath():
    # Try to check if path.txt is present if not it will create
    # the path for them in the current directory and will ask for
    # the path for the profiles folder which will write to path.txt
    # which can be used in future initializations
    pathDirec = ""
    try:
        file = open("path.txt", "r")
        pathDirec = file.read()
        file.close()
    except IOError:
        f = open("path.txt", 'w')
        print "Path to profiles not set yet."
<<<<<<< HEAD
        pathDirec = raw_input(
            "File directory has not been set up yet, please choose the folder with profile data:")
=======
        pathDirec = raw_input('File directory has not been set up yet,'\
            'please choose the folder with profile data:')
>>>>>>> 5398629a56f1780be80f1783f39953654aef11a0
        print "File path set to: %s" % pathDirec
        f.write(pathDirec)
        f.close()
    return pathDirec
<<<<<<< HEAD


=======
>>>>>>> 5398629a56f1780be80f1783f39953654aef11a0
