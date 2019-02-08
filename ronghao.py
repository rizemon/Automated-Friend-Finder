import getfilepath
from os.path import isdir
from fileparser import pretty_print

#This function is the first function to be call from the main
def viewMatchesOverall(profile, name):
    profiles = profile #profiles will be used as a variable for easier identification
    global profiles #global profiles allow all the functions in the module to use profiles.
    return overallCompatibility(name)

#list all name
def listAllName():
   return profiles.keys()



#Return person's country (person need to be input as string)
def country(person):
    return profiles[person]["country"]



#If country is someone else acceptable country, give 25 points to that person
def countryCompatibility(PersonInputed2):  
    Country_compat_dict = {} #initialise countryCompat as a dictionary

    #For each individual profiles
    for name in profiles.keys():
        #Only opposite gender
        if profiles[name]['gender'] != profiles[PersonInputed2]['gender']:
            
            Country_compat_dict[name] = 0 #Give everyone a starting points of 0 by using a dict whereby "name": points
            
            #if the person input by the user is found in the list of profile, do nothing. This is to avoid giving himself points
            if name != PersonInputed2:

                #Compare everyone country with the person input by the user acceptable country
                    for acc_country in profiles[name]['acceptable_country']:

                    #if their country is also the person acceptable country, add 25 points to that individual
                        if (profiles[name]["country"] ==  acc_country) :
                            Country_compat_dict[name] = 25
            
    return Country_compat_dict



#Return Person's age (person need to be input as string)
def age(input_Person):
    return profiles[input_Person]["age"]



#If age is someone else Acceptable age range, give 25 points to that person
def ageCompatibility(inputName):
    Age_comp_dict = {} #initialise Age_comp as a dictionary

    #For each individual profiles
    for name in profiles.keys():

        #Only opposite gender
        if profiles[name]['gender'] != profiles[inputName]['gender']:
            Age_comp_dict[name] = 0 #Give everyone a starting points of 0 by using a dict whereby "name": points

            #if the person input by the user is found in the list of profile, do nothing. This is to avoid giving himself points
            if name != inputName:
                    
                    #Compare everyone's age with the person's acceptable age range
                    for acc_Age_Range in (range((profiles[name]['acceptable_age_range']['start']),(profiles[name]['acceptable_age_range']['end']))):

                        #if their age is in the person acceptable age range, add 25 points to that individual
                        if (profiles[inputName]["age"] ==  acc_Age_Range) :
                            Age_comp_dict[name] = 25

    return Age_comp_dict


            
#Return Person's likes
def likes(nameOfInput):
    return profiles[str(nameOfInput)]["likes"]

#If person inputed likes has similar likes to other people in the profile list, give 5 points to that person for every likes they share
def likesCompatibility(nameOfInput2): 
    Likes_comp_dict = {} #initialise Likes_comp_dict as a dictionary

    #For each individual profiles
    for name in profiles.keys():
        
        #Only opposite gender
        if profiles[name]['gender'] != profiles[nameOfInput2]['gender']:
            
            Likes_comp_dict[name] = 0 #Give everyone a starting points of 0 by using a dict whereby "name": points

            #if the person input by the user is found in the list of profile, do nothing. This is to avoid giving himself points
            if name != str(nameOfInput2):

                    #For each likes in other people in the profile list, compare them to each likes of inputed user
                    for othersLikes in profiles[name]['likes']:
                        for inputedUserLikes in profiles[nameOfInput2]["likes"]:

                            #Give 5 points for each like that matches to that person
                            if inputedUserLikes ==  othersLikes :
                                Likes_comp_dict[name] = (int(Likes_comp_dict[name]) + 5)

    return Likes_comp_dict


#Return Person X dislikes
def dislikes(inputPersonName):
    return profiles[inputPersonName]["dislikes"]

#If person inputed dislikes has similar dislikes to other people in the profile list, give 5 points to that person for every dislikes they share
def dislikesCompatibility(inputPerson_Name):
    Dislikes_comp_dict = {} #initialise Dislikes_comp_dict as a dictionary

    #For each individual profiles
    for name in profiles.keys():

        #Only opposite gender
        if profiles[name]['gender'] != profiles[inputPerson_Name]['gender']:
            
            Dislikes_comp_dict[name] = 0 #Give everyone a starting points of 0 by using a dict whereby "name": points

            #if the person input by the user is found in the list of profile, do nothing. This is to avoid giving himself points
            if name != str(inputPerson_Name):
                
                #For each dislikes in other people in the profile list, compare them to each dislikes of inputed user
                for othersDislikes in profiles[name]['dislikes']:
                    for inputedUserDislikes in profiles[str(inputPerson_Name)]["dislikes"]:

                        #Give 5 points for each dislike that matches to that person
                        if inputedUserDislikes ==  othersDislikes :
                            Dislikes_comp_dict[name] = (int(Dislikes_comp_dict[name]) + 5)

    return Dislikes_comp_dict


#If someone else dislikes is your likes or their likes is your disklikes, take away 5 points each conflicts
def bothLikesDislikesCompatibility(inputedPersonName):
    dislikesToLikes = {} #initialise dislikesToLikes as a dictionary
    bothLikesDislikes = {} #initialise bothLikesDislikes as a dictionary

    #For each individual profiles
    for name in profiles.keys():

        #Only opposite gender
        if profiles[name]['gender'] != profiles[inputedPersonName]['gender']:
            
            dislikesToLikes[name] = 0 #Give everyone a starting points of 0 by using a dict whereby "name": points

            #if the person input by the user is found in the list of profile, do nothing. This is to avoid giving himself points
            if name != str(inputedPersonName):
             
                #For each dislikes in other people in the profile list, compare them to each likes of inputed user
                for othersDislikes in profiles[name]['dislikes']:
                    for inputedUserLikes in profiles[str(inputedPersonName)]["likes"]:

                        #Take away 5 points for each dislike and likes that matches
                        if inputedUserLikes ==  othersDislikes :
                            dislikesToLikes[name] = (int(dislikesToLikes[name]) - 5)


    likesToDislikes ={} #initialise likesToDislikes as a dictionary

    #For each individual profiles
    for name in profiles.keys():

        #Only opposite gender
        if profiles[name]['gender'] != profiles[inputedPersonName]['gender']:
            
            likesToDislikes[name] = 0 #Give everyone a starting points of 0 by using a dict whereby "name": points

            #if the person input by the user is found in the list of profile, do nothing. This is to avoid giving himself points
            if name != str(inputedPersonName):
                
                #For each likes in other people in the profile list, compare them to each dislikes of inputed user
                for othersLikes in profiles[name]['likes']:
                    for inputedUserDislikes in profiles[str(inputedPersonName)]["dislikes"]:

                        #Take away 5 points for each dislike and likes that matches
                        if inputedUserDislikes ==  othersLikes :
                            likesToDislikes[name] = (int(likesToDislikes[name]) - 5)

    #Sum up the total number of points taken away for Likes and Dislikes that matches
    bothLikesDislikes = dict(dislikesToLikes.items() + likesToDislikes.items() + [(k, dislikesToLikes[k] + likesToDislikes[k]) for k in set(likesToDislikes) & set(dislikesToLikes)])
    return bothLikesDislikes

#Total up all the points from country Compatibility,age Compatibility,likes Compatibility,dislikes Compatibility and both Likes Dislikes Compatibility
def overallCompatibility(name):

    #initialise 3 Temp dictionary to do workings
    Temp1= {}
    Temp2= {}
    Temp3= {}
    
    #initialise overallCompatibility dictionary
    overallCompatibility = {}

    #initialise sortedoverallCompatibility list
    sortedoverallCompatibility=[]

    #To combind all the dictionary into one dictionary called overallCompatibility with all their points sum up
    Temp1 = dict((countryCompatibility(name)).items() + (ageCompatibility(name)).items() + [(k, (countryCompatibility(name))[k] + (ageCompatibility(name))[k]) for k in set(ageCompatibility(name)) & set(countryCompatibility(name))])
    Temp2 = dict(Temp1.items() + (likesCompatibility(name)).items() + [(k, (Temp1)[k] + (likesCompatibility(name))[k]) for k in set(likesCompatibility(name)) & set(Temp1)])
    Temp3 = dict(Temp2.items() + (dislikesCompatibility(name)).items() + [(k, (Temp2)[k] + (dislikesCompatibility(name))[k]) for k in set(dislikesCompatibility(name)) & set(Temp2)])
    overallCompatibility = dict(Temp3.items() + (bothLikesDislikesCompatibility(name)).items() + [(k, (Temp3)[k] + (bothLikesDislikesCompatibility(name))[k]) for k in set(bothLikesDislikesCompatibility(name)) & set(Temp3)])

    #To sort each person name whereby first is most compatible and third is second runner up
    #If there are at least 3 people that are the opposite gender in the dictionary
    if len(overallCompatibility) == 3:
        
        for key, value in sorted(overallCompatibility.iteritems(),reverse =True, key=lambda (k,v): (v,k)):
           k =(key, value)
           sortedoverallCompatibility.append(k)
        first = sortedoverallCompatibility[0][0]
        second = sortedoverallCompatibility[1][0]
        third = sortedoverallCompatibility[2][0]

        #To create a new list to store the top 3 profiles
        listOutput=[]

        #To create a new dict to store most compatible person profile
        profile1={}

        #To create a new dict to store first runner up person profile
        profile2={}

        #To create a new dict to store second runner up person profile
        profile3={}

        profile1["gender"]=profiles[first]["gender"] #storing gender into profile1
        profile1["age"]=profiles[first]["age"] #storing age into profile1
        profile1["name"]=first #storing name into profile1
        profile1["country"]=profiles[first]["country"] #storing country into profile1


        profile2["gender"]=profiles[second]["gender"] #storing gender into profile1
        profile2["age"]=profiles[second]["age"] #storing age into profile1
        profile2["name"]=second #storing name into profile1
        profile2["country"]=profiles[second]["country"] #storing country into profile1


        profile3["gender"]=profiles[third]["gender"] #storing gender into profile1
        profile3["age"]=profiles[third]["age"] #storing age into profile1
        profile3["name"]=third #storing name into profile1
        profile3["country"]=profiles[third]["country"] #storing country into profile1
        

        #append profile1,profile2 and proifle3 into listOutput
        listOutput.append(profile1)
        listOutput.append(profile2)
        listOutput.append(profile3)

        #return final output
        return listOutput

    #If there are only 2 people that are the opposite gender in the dictionary
    elif len(overallCompatibility) == 2:
        
        for key, value in sorted(overallCompatibility.iteritems(),reverse =True, key=lambda (k,v): (v,k)):
           k =(key, value)
           sortedoverallCompatibility.append(k)
        first = sortedoverallCompatibility[0][0]
        second = sortedoverallCompatibility[1][0]

        #To create a new list to store the top 3 profiles
        listOutput=[]

        #To create a new dict to store most compatible person profile
        profile1={}

        #To create a new dict to store first runner up person profile
        profile2={}


        profile1["gender"]=profiles[first]["gender"] #storing gender into profile1
        profile1["age"]=profiles[first]["age"] #storing age into profile1
        profile1["name"]=first #storing name into profile1
        profile1["country"]=profiles[first]["country"] #storing country into profile1


        profile2["gender"]=profiles[second]["gender"] #storing gender into profile1
        profile2["age"]=profiles[second]["age"] #storing age into profile1
        profile2["name"]=second #storing name into profile1
        profile2["country"]=profiles[second]["country"] #storing country into profile1
        

        #append profile1,profile2 and proifle3 into listOutput
        listOutput.append(profile1)
        listOutput.append(profile2)

        #return final output
        return listOutput

    #If there are only 1 people that are the opposite gender in the dictionary
    elif len(overallCompatibility) == 1:
        
        for key, value in sorted(overallCompatibility.iteritems(),reverse =True, key=lambda (k,v): (v,k)):
           k =(key, value)
           sortedoverallCompatibility.append(k)
        first = sortedoverallCompatibility[0][0]

        #To create a new list to store the top 3 profiles
        listOutput=[]

        #To create a new dict to store most compatible person profile
        profile1={}

        profile1["gender"]=profiles[first]["gender"] #storing gender into profile1
        profile1["age"]=profiles[first]["age"] #storing age into profile1
        profile1["name"]=first #storing name into profile1
        profile1["country"]=profiles[first]["country"] #storing country into profile1
        

        #append profile1,profile2 and proifle3 into listOutput
        listOutput.append(profile1)

        #return final output
        return listOutput

    #If there are no people that are the opposite gender in the dictionary
    elif len(overallCompatibility) == 0:
        
        #To create a new list to store the top 3 profiles
        listOutput=[]

        #return final output
        return listOutput
