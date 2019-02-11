# This functions uses the top appearing interest between your matched profiles to return you date suggestions
def view_first_date_suggestions(name, profiles):
    from nltk.corpus import wordnet as wn
    from eventbrite import Eventbrite

    user_profile = profiles[name]
    # Placeholder results for top 3 overall profiles to get from ronghao function
    tempList = []
    tempList.append(profiles["Joel Jackson"])
    tempList.append(profiles["Kevin"])
    tempList.append(profiles["Joel Jackson"])

    # Compile likes and favourite books of the current profile AND each of the top 3 matched profile into a corpus

    # currentInterest stores the interests(Both likes and favourite books) of the current profile as a list
    currentInterest = documentPreparation(user_profile)
    # matchedInterest stores the interests(Both likes and favourite books) of the matching profile as a list
    matchedInterest = documentPreparation(profiles["Joel Jackson"])

    # combinedInterest stores a list of string values containing the compiled interest of the current profile and matched interest
    combinedInterest = currentInterest + matchedInterest

    # cleanedDocument processes and cleans the compiled interest, returning lemmatized(base forms) of the words in combinedInterest
    cleanedDocument = documentPreprocessing(combinedInterest)

    #  The function documentTermMatrix returns the latent topics of the compiled interest, arranging the words according to their appearance as a list
    listOfMostSignificantTopic = documentTermMatrix(cleanedDocument)

    eventbrite = Eventbrite('2AFR6PPQRSQS62J2CLIK')
    # eventCategoriesDict stores all the eventbrite id references in a dictionary
    eventCategoriesDict = {"Music": "103", "Business": "101", "Food": "110", "Community": "113", "Arts": "105", "Film": "104", "Sports": "108", "Health": "107", "Science": "102", "Outdoor": "109", "Charity": "111", "Spirituality": "114", "Family": "115", "Holiday": "116", "Politics": "112", "Fashion": "106", "Lifestyle": "117", "Auto": "118", "Hobbies": "119", "Other": "119", "School": "120"}

    # Stores all the keys of eventCategoriesDict in a list
    eventCategoriesList = []
    for keys in eventCategoriesDict:
        eventCategoriesList.append(keys)

    # This removes the changes the tuple in the list into unicode string
    listOfMostSignificantTopicUni = [str(index[1]) for index in listOfMostSignificantTopic]

    # Converts the unicode list item into ascii characters
    listOfMostSignificantTopicStr = [i.encode('ascii') for i in listOfMostSignificantTopicUni]

    # Keep only the alphabetic character in the list items
    # This is the final list that stores all the best matching interest(latent topics) between current profile and matched profile
    listOfMostSignificantTopicAlpha = ["".join(filter(str.isalpha, i)) for i in listOfMostSignificantTopicUni]

    # This function stores all synsets of a list item as a key:value pair, with the list item being the key, and the value being all the available synsetss
    # Synsets are sets of synonyms that share a common meaning
    # This makes sure when we compare the similarity, we are comparing similarity behind the inherent meaning of the word
    # synSetDict stores the synsets of the best matching interest between the current user and matched profile
    synSetDict = {i : [] for i in listOfMostSignificantTopicAlpha}

    for key, value in synSetDict.items():
        for synset in wn.synsets(key):
            # for lemma in synset.lemmas():
            value.append(synset)

    # synSetDict stores the synsets of the events categories from eventbrite
    synSetDict2 = {i: [] for i in eventCategoriesList}

    for key, value in synSetDict2.items():
        for synset in wn.synsets(key):
            # for lemma in synset.lemmas():
            value.append(synset)

    # Now we have to compare the similarity of all the synsets of both dictionaries

    similarity_percent_dict ={}
    # This loops through all the values in syn_set_dict
    for key1, value1 in synSetDict.items():
        for index1 in value1:
            for key2, value2 in synSetDict2.items():
                for index2 in value2:
                    similarity_percent = wn.wup_similarity(index1, index2)
                    similarity_percent_dict[key1+key2] = similarity_percent

    # top_matching_category is a string containing the best matched interest and corresponding event category(The one with the highest similarity percentage as it's value
    # It is the best match between the latent interest of both users with one of the event categories
    # Example values are: ethicScience, with ethic being the matched interest and Science being the corresponding event category
    top_matching_category = max(similarity_percent_dict, key=similarity_percent_dict.get)

    # Loops through all the values in eventCategoriesDict
    for value in eventCategoriesDict:
        # category_id stores the corresponding string category id of the category value that appears in top_matching_category
        if value in top_matching_category:
            category_id = (eventCategoriesDict[value])
            event_category_value = value

    # list_of_date_suggestions is a list containing the first 5 events that matches eventCategoryID found to be most suitable for this couple
    # Each event is stored in a dictionary with the keys being "url", "name" and "description"
    # Example output would be: [{"url": "https://www.eventbrite.com", "name": "DeveloperWeek 2019", "description": "blah blah"},{...},{...},{...},{...}]
    list_of_date_suggestions = [{"name": event["name"]["text"], "description": event["description"]["text"], "url": event["url"]} for event in eventbrite.get(path="/events/search/", data={"categories": category_id})["events"][:5]]

    print "The one of the ideal event type for your first date is: " + event_category_value
    print "Here are 5 suggestions from EventBrite:"
    # Prints out the list of best date suggestions
    # This is the final desired output
    print list_of_date_suggestions

# Returns the likes and favourite books of the profile given as interest
def documentPreparation(profile):
    interest = profile['likes'] + profile['books']
    return interest


def documentPreprocessing(corpus):
    # Cleaning and preprocessing
    from nltk.corpus import stopwords
    from nltk.stem.wordnet import WordNetLemmatizer
    import string

    # Places known natural language stopwords such as "a","the" into a set
    stop = set(stopwords.words('english'))

    # Places known punctuations into a set
    exclude = set(string.punctuation)
    # Performs lemmatization on the word to convert it to its base form
    # This considers the context
    # It will return the original input if it fails
    lemma = WordNetLemmatizer()

    # Cleans each list item in the the given text(corpus)
    def documentCleaning(doc):
        stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
        punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
        normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
        return normalized

    cleanedDocument = [documentCleaning(doc).split() for doc in corpus]
    return cleanedDocument

#This functions is La
def documentTermMatrix(cleanedDocument):
    import gensim
    from gensim import corpora

    # Assigns a unique token to each unique term
    # Dictionary(5 unique tokens: [u'chop', u'chicken', u'garlic', u'durain', u'swimming'])
    dictionary = corpora.Dictionary(cleanedDocument)

    # Converts the text-based corpus into a matrix representation
    # dictionary.doc2bow converts the document into a list of token_id(I.E Unique tokens) and token_count tuples
    matrixRepresentation = [dictionary.doc2bow(doc) for doc in cleanedDocument]

    ldaObject = gensim.models.ldamodel.LdaModel

    # To determine optimal amount of topics for a dataset like ours, i chose 5
    # http://www.rpubs.com/MNidhi/NumberoftopicsLDA
    ldamodel = ldaObject(matrixRepresentation, num_topics=5, id2word= dictionary, passes= 100)

    # Returns all the most significant topics, arranging the topics and words by significance
    return ldamodel.print_topics(num_topics=5, num_words=1)




