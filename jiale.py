# Set the directory of the nltk data
from nltk.data import path
path.insert(0, ".\\nltk_data")

from nltk.corpus import wordnet
from nltk import word_tokenize


def checkPossiblePartner(person1, person2, profiles):

    # Returns whether person2 is a possible partner for person1
    #
    # Parameters:
    # person1 (string): name of person1
    # person2 (string): name of person2
    # profiles (dict): profiles dictionary
    #
    # Returns:
    # (boolean): True if person2 is a possible partner for person1,
    #            False if person 2 is not possible partner for person1

    # Check if person2 is the same person as person1
    if person1 == person2:
        return False
    # Check if person2 have the same gender as person1
    if profiles[person1]["gender"] == profiles[person2]["gender"]:
        return False
    # Check if person2's age is in the acceptable_age_range of person1
    if not (profiles[person1]["acceptable_age_range"]["start"]
            <= profiles[person2]["age"]
            <= profiles[person1]["acceptable_age_range"]["end"]):
        return False

    return True


def isNoun(word):

    # Returns whether a word is a noun
    #
    # Parameters:
    # word (string): word
    #
    # Returns:
    # (boolean): True if the word is a noun
    #            False if the word is not a noun

    for meaning in wordnet.synsets(word):
        type = meaning.pos()
        if type == 'n':
            return True
    return False


def calculateSimilarity(person1, person2, interests):

    # Returns the similarity score between person1's list of interests and
    # person2's list of interests
    #
    # Parameters:
    # person1 (string): name of person1
    # person2 (string): name of person2
    # interests (dict): dictionary mapping profile name to their respective list of interests
    #
    # Returns:
    # (double): total similarity score based on 2 persons' list of interests

    similarity = 0
    for keyword1 in interests[person1]:
        for keyword2 in interests[person2]:
            similarity += wordnet.synsets(keyword1)[0].path_similarity(wordnet.synsets(keyword2)[0])
    return similarity


def viewMatchesBooks(profiles, matches, name):

    # Returns top 3 profiles with the most similar interests of a given profile
    #
    # Parameters:
    # profiles (dict): profiles dictionary
    # matches (dict):  2D dictionary mapping every possible pair of profiles to a similarity score
    # name (string): name of profile to view matches based on
    #
    # Returns:
    # (list): list of profiles matched based on books for the given profile

    # Perform sorting in descending order and retrieve top 3 persons with similar interests for a given person
    return [{
        "name": partner_name,
        "gender": profiles[partner_name]["gender"],
        "age": profiles[partner_name]["age"],
        "country": profiles[partner_name]["country"]}
        for partner_name in sorted(matches[name], reverse=True)[:3]]


def getMatchesBooks(profiles):

    # Returns a 2D dictionary mapping every possible pair of profiles to a similarity score
    #
    # Parameters:
    # profiles (dict): profiles dictionary
    #
    # Returns:
    # (dict): 2D dictionary that maps 2 names to a similarity score

    # A dictionary mapping person's name to a list of their possible interests
    interests = {}

    # A 2D dictionary that maps 2 names to a similarity score
    matches = {}

    # Loop through each profile
    for name in profiles:
        if name not in interests:
            # Initialize the empty list of possible interests
            interests[name] = set()
            # Initialize the similarity score between the current profile and the possible partners' profiles to 0
            matches[name] = {partner_name: 0 for partner_name in profiles.keys()
                             if checkPossiblePartner(name, partner_name, profiles)}

        # Loop through each book for the current profile
        for book in profiles[name]["books"]:
            # Split and extract each keyword for name of the book
            token_list = word_tokenize(book.lower())
            # Append keywords that are nouns to the current profile's list of possible interests
            interests[name].update([word for word in token_list if isNoun(word)])

    # Loop through each name
    for name in matches:
        # Loop through each possible partner of name
        for partner_name in matches[name]:
            # Check if the score between name and partner_name has already been calculated
            if matches[name][partner_name] == 0:
                # Calculate the score based on both profile's list of interests
                matches[name][partner_name] = calculateSimilarity(name, partner_name, interests)
                # Check if name is also a possible partner of partner_name
                if name in matches[partner_name]:
                    # Make sure the score is bidirectional
                    matches[partner_name][name] = matches[name][partner_name]

    return matches
