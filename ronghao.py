import getfilepath
from os.path import isdir
from fileparser import pretty_print

#This function is the first function to be call from the main and 
def viewMatchesOverall(profile):
    #query is to take in name input by the user 
    query = raw_input("Write the name of the person you want to know for the top 3 matches: ")

    #profiles will be used as a variable for easier identification
    profiles = profile
    
    #global profiles allow all the functions in the module to use profiles.
    global profiles
    print overallCompatibility(query)

#list all name
def listAllName():
   return profiles.keys()
        

#Return Person country
def country(person):
    return profiles[str(person)]["country"]

#If country is someone else acceptable country, give 25 points to that person
def countryCompatibility(x):
    
    #initialise countryCompat as a dictionary
    Country_compat_dict = {}
    
    #For each individual profiles dictionary with name as the key
    for name in profiles.keys():

        #Give everyone a starting points of 0 by using a dict whereby "name": points
        Country_compat_dict[each] = 0

        #if the person input by the user is found in the list of profile, do nothing so as to avoid giving himself points
        if name != str(x):

            #Compare everyone country with the person input by the user acceptable country
            for acc_country in profiles[name]['acceptable_country']:

                #if their country is also the person acceptable country, add 25 points to that individual
                if (profiles[str(x)]["country"] ==  acc_country) :
                    Country_compat_dict[name] = 25
            
    return CC

#Return Person X age
def age(x):
    return profiles[str(x)]["age"]

#If age is someone else Acceptable age range, give 25 points to that person
def ageCompatibility(x):

    #initialise Age_comp as a dictionary
    Age_comp_dict = {}

    #For each individual profiles dictionary with name as the key
    for name in profiles.keys():

        #Give everyone a starting points of 0 by using a dict whereby "name": points
        Age_comp_dict[name] = 0

        #if the person input by the user is found in the list of profile, do nothing so as to avoid giving himself points
        if name != str(x):

            #Compare everyone's age with the person's acceptable age range
            for acc_Age_Range in (range((profiles[name]['acceptable_age_range']['start']),(profiles[name]['acceptable_age_range']['end']))):

                #if their age is in the person acceptable age range, add 25 points to that individual
                if (profiles[str(x)]["age"] ==  acc_Age_Range) :
                    Age_comp_dict[name] = 25

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
The top three matches for %s are:

Third:  %s
Second: %s
First:  %s''' %(x,third,second,first)
    
