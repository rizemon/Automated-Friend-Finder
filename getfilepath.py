from os import listdir
from os.path import join
import fileparser


def get_profiles(file_path):

    # Takes in the directory path, read the profiles in them and
    # return all the profiles

    profiles = {}
    files = listdir(file_path)
    for filename in files:
        with open(join(file_path, filename), "r") as f:
            name, profile = fileparser.parse(f)
            profiles[name] = profile
            f.close()
    return profiles


def get_file_path():
    # Try to check if path.txt is present if not it will create
    # the path for them in the current directory and will ask for
    # the path for the profiles folder which will write to path.txt
    # which can be used in future initializations
    _filePath = ""
    try:
        # Tries to open path.txt that is inside the folder if not on first load
        _file = open("path.txt", "r")
        _filePath = _file.read()
        _file.close()
    except IOError:
        # Creates path.txt for the user and asks to input where the profiles folder are
        f = open("path.txt", 'w')
        print "Path to profiles not set yet."
        _filePath = raw_input('File directory has not been set up yet,'\
            'please choose the folder with profile data:')
        print "File path set to: %s" % _filePath
        f.write(_filePath)
        f.close()
    return _filePath
