# Set the directory of the necessary files
from nltk.data import path
path.insert(0, ".\\nltk_data")

from nltk.corpus import wordnet
from nltk import word_tokenize
from heapq import nlargest

# Check if the word is a noun
def isNoun(word):
    for meaning in wordnet.synsets(word):
        type = meaning.pos()
        if type == 'n':
            return True
    return False

# Calculate the score based on 2 persons' list of interests
def calculateSimilarity(interests1, interests2):
    similarity = 0
    for keyword1 in interests1:
        for keyword2 in interests2:
            similarity += wordnet.synsets(keyword1)[0].path_similarity(wordnet.synsets(keyword2)[0])
    return similarity

# Perform heap sort and retrieve top 3 persons with similar interests for a given person
def getTopThree(name, matches):
    return nlargest(3, matches[name])

# Calculate the similarity score between any 2 persons using the profile dictionary
def getMatchesBooks(profiles):
    # Function 4: ...

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
            matches[name] = {partner_name: 0 for partner_name in profiles.keys() if name != partner_name}

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
                matches[name][partner_name] = calculateSimilarity(interests[name], interests[partner_name])
                # Make sure the score is bidirectional
                matches[partner_name][name] = matches[name][partner_name]

    return matches



