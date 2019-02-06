# Set the directory of the nltk data
from nltk.data import path
path.insert(0, ".\\nltk_data")

from nltk.corpus import wordnet
from nltk import word_tokenize


def checkPossiblePartner(person1, person2, profiles):
    # Check if person2 is a possible partner for person1

    # Check if person2 is the same person as person1
    if person1 == person2:
        return False
    # Check if person2 have the same gender as person1
    if profiles[person1]["gender"] == profiles[person2]["gender"]:
        return False
    # Check if person2's country in the acceptable_country of person1
    if profiles[person2]["country"] not in profiles[person1]["acceptable_country"]:
        return False
    # Check if person2's age is in the acceptable_age_range of person1
    if not (profiles[person1]["acceptable_age_range"]["start"]
            <= profiles[person2]["age"]
            <= profiles[person1]["acceptable_age_range"]["end"]):
        return False

    return True


def isNoun(word):
    # Check if the word is a noun
    for meaning in wordnet.synsets(word):
        type = meaning.pos()
        if type == 'n':
            return True
    return False


def calculateSimilarity(person1, person2, interests):
    # Calculate the score based on 2 persons' list of interests
    similarity = 0
    for keyword1 in interests[person1]:
        for keyword2 in interests[person2]:
            similarity += wordnet.synsets(keyword1)[0].path_similarity(wordnet.synsets(keyword2)[0])
    return similarity


def getTopThree(name, matches):
    # Perform sorting in descending order and retrieve top 3 persons with similar interests for a given person
    return sorted(matches[name], reverse=True)[:3]


def getMatchesBooks(profiles):
    # Calculate the similarity score between any 2 persons using the profile dictionary

    # A dictionary mapping person's name to a list of their possible interests
    interests = {}

    # A 2D dictionary that maps 2 names to a similarity score
    matches = {}

    # Loop through each profile
    for name in profiles:
        if name not in interests:
            # Initialize the empty list of possible interests
            interests[name] = set()
            # Initialize the similarity score between the current profile and the others' profiles to 0
            matches[name] = {partner_name: 0 for partner_name in profiles.keys()
                             if checkPossiblePartner(name, partner_name, profiles)}

        # Loop through each book for the current profile
        for book in profiles[name]["books"]:
            # Split and extract each keyword for name of the book
            token_list = word_tokenize(book.lower())
            # Append keywords that are nouns to the current profile's list of possible interests
            interests[name].update([word for word in token_list if isNoun(word)])

    # Loop through each possible pair of profiles
    for name in matches:
        for partner_name in matches[name]:
            # Check if the score between the pair has already been calculated
            if matches[name][partner_name] == 0 or matches[partner_name][name] == 0:
                # Calculate the score based on each profile's list of interests
                matches[name][partner_name] = calculateSimilarity(name, partner_name, interests)
                # Make sure the score is bidirectional
                matches[partner_name][name] = matches[name][partner_name]

    return matches
