import getfilepath
from os.path import isdir
from fileparser import pretty_print
import ronghao

directory = getfilepath.getFilePath()
profiles = getfilepath.getProfiles(directory)

#list all name
def listAllName():
   return profiles.keys()
        
a = "Carol"
#Return Person X country
def country(x):
    return profiles[str(x)]["country"]

#If country is someone else acceptable country, give 25 points to that person
def countryCompatibility(x):
    CC = {}
    for each in profiles.keys():
        CC[each] = 0
        if each != str(x):
            for each2 in profiles[each]['acceptable_country']:
                if (profiles[str(x)]["country"] ==  each2) :
                    CC[each] = 25
            
    return CC

#Return Person X age
def age(x):
    return profiles[str(x)]["age"]

#If age is someone else Acceptable age range, give 25 points to that person
def ageCompatibility(x):
    AC = {}
    for each in profiles.keys():
        AC[each] = 0
        if each != str(x):
            for each2 in (range((profiles[each]['acceptable_age_range']['start']),(profiles[each]['acceptable_age_range']['end']))):
                if (profiles[str(x)]["age"] ==  each2) :
                    AC[each] = 25

    return AC
            
#Return Person X likes
def likes(x):
    return profiles[str(x)]["likes"]

#If likes is someone else likes, give 5 points to that person
def likesCompatibility(x):
    LC = {}
    for each in profiles.keys():
        LC[each] = 0
        if each != str(x):
            for each2 in profiles[each]['likes']:
                for each3 in profiles[str(x)]["likes"]:
                    if each3 ==  each2 :
                        LC[each] = (int(LC[each]) + 5)

    return LC


#Return Person X dislikes
def dislikes(x):
    return profiles[str(x)]["dislikes"]

#If dislikes is someone else dislikes, give 5 points to that person
def dislikesCompatibility(x):
    DC = {}
    for each in profiles.keys():
        DC[each] = 0
        if each != str(x):
            for each2 in profiles[each]['dislikes']:
                for each3 in profiles[str(x)]["dislikes"]:
                    if each3 ==  each2 :
                        DC[each] = (int(DC[each]) + 5)

    return DC


#If someone else dislikes is your likes or their likes is your disklikes, take away 5 points each conflicts
def bothLikesDislikesCompatibility(x):
    DL = {}
    OO = {}
    for each in profiles.keys():
        DL[each] = 0
        if each != str(x):
            for each2 in profiles[each]['dislikes']:
                for each3 in profiles[str(x)]["likes"]:
                    if each3 ==  each2 :
                        DL[each] = (int(DL[each]) - 5)


    LD={}
    for each in profiles.keys():
        LD[each] = 0
        if each != str(x):
            for each2 in profiles[each]['likes']:
                for each3 in profiles[str(x)]["dislikes"]:
                    if each3 ==  each2 :
                        LD[each] = (int(LD[each]) - 5)
        
    OO = dict(DL.items() + LD.items() + [(k, DL[k] + LD[k]) for k in set(LD) & set(DL)])
    return OO

#Add up on the points
def overallCompatibility(x):
    OC = {}
    OC1= {}
    OC2= {}
    OC3= {}

    sortedOC=[]

    OC3 = dict((countryCompatibility(x)).items() + (ageCompatibility(x)).items() + [(k, (countryCompatibility(x))[k] + (ageCompatibility(x))[k]) for k in set(ageCompatibility(x)) & set(countryCompatibility(x))])
    OC2 = dict(OC3.items() + (likesCompatibility(x)).items() + [(k, (OC3)[k] + (likesCompatibility(x))[k]) for k in set(likesCompatibility(x)) & set(OC3)])
    OC1 = dict(OC2.items() + (dislikesCompatibility(x)).items() + [(k, (OC2)[k] + (dislikesCompatibility(x))[k]) for k in set(dislikesCompatibility(x)) & set(OC2)])
    OC = dict(OC1.items() + (bothLikesDislikesCompatibility(x)).items() + [(k, (OC1)[k] + (bothLikesDislikesCompatibility(x))[k]) for k in set(bothLikesDislikesCompatibility(x)) & set(OC1)])
    
    for key, value in sorted(OC.iteritems(),reverse =True, key=lambda (k,v): (v,k)):
       k =(key, value)
       sortedOC.append(k)
    first = sortedOC[0][0]
    second = sortedOC[1][0]
    third = sortedOC[2][0]

    return '''
=======================================
The top three matches in are:

Third:  %s
Second: %s
First:  %s''' %(third,second,first)
    
