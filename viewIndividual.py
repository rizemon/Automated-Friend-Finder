#Function: viewIndividual
#is to translate input from "profile name (Michael Jackson)" to "filename (1)"
import getfilepath
import sys
import fileparser
import ronghao
import metrics


def viewIndividual(profiles):
    global filename1
    global gender
    data=[]
    gender = None
    directory = getfilepath.getFilePath()
    
 
    if profiles == "Michael Jackson":
        filename1 = (directory + "\\1.txt")
    elif profiles == "Carol":
        filename1 = (directory + "\\2.txt")
    elif profiles == "Kevin":
        filename1 = (directory + "\\3.txt")
    elif profiles == "Rose":
        filename1 = (directory + "\\4.txt")
    elif profiles == "Shelley":
        filename1 = (directory + "\\5.txt")
    elif profiles == "Joel Jackson":
        filename1 = (directory + "\\7.txt")
    elif profiles == "Jenny Wang":
        filename1 = (directory + "\\8.txt")
    elif profiles == "Angela Little":
        filename1 = (directory + "\\9.txt")
    elif profiles == "Lisa Marie":
        filename1 = (directory + "\\10.txt")
    elif profiles == "Teresa":
        filename1 = (directory + "\\11.txt")
    else:
        print ("No such person found in the list of profile. Please enter the exact name (Case Sensetive)\n")
        ronghao.top3profiles()

    f = open(filename1, "r")
    #print ("\n\n\n" + f.read())

    #storing profiles in list
    for line in f:
        lines=line.split(' ')
        data.append(lines)

    #obtaining gender information from list
    gender = data[1][1][0]
    print ("Gender: " + gender)
    
    metrics.calculator(gender)
    
    return
