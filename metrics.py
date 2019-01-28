import viewIndividual
import getfilepath
from os.path import isdir
from sys import exit
import fileparser
import ronghao
compatibility = None


def calculator(gender):
    global compatibility
    compatibility = 0
    if (gender == "M" or gender == "m"):
        compatibility = compatibility + 50
    else:
        compatibility = compatibility - 50

    print ("compatibility: " + str(compatibility))
    return compatibility



