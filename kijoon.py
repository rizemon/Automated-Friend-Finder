from ronghao import viewMatchesOverall
from nltk.corpus import wordnet as wn
from eventbrite import Eventbrite
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora
from nltk.data import path
path.insert(0, ".\\nltk_data")


# This function parses in your current profile and each matching profile into matching_interest_compiler
def view_first_date_suggestions(name, profiles):
    user_profile = profiles[name]
    name_list = []
    # Gets the profile informations of the top 3 best matched overall profiles from ronghao's viewMatchesOverall
    top_3_profile_without_interest = viewMatchesOverall(profiles, name)

    # Loops through the list without interest and puts them into name_list
    for index, value in enumerate(top_3_profile_without_interest):
        name_list.append(value["name"])

    # This adds back the name value into the list containing the dictionary of the profiles as top_3_profile_without_interest obtained from ronghao's viewMatchesOverall does not contain the name key pair value
    top_3_profile = []
    for name in name_list:
        top_3_profile.append(profiles[name])
    for i, d in enumerate(top_3_profile):
        d['name'] = name_list[i]

    # Loops through the indexes of the list in order to parse each matching profile into matching_interest_compiler
    output = []

    for index, value in enumerate(top_3_profile):
        output.append(matching_interest_compiler(user_profile, top_3_profile[index]))

    return output


# Compile likes and favourite books of the current profile AND each of the top 3 matched profile into a corpus
# It uses the top appearing interest between your matched profiles to return you date suggestions
def matching_interest_compiler(current_profile, matching_profile):

    # currentInterest stores the interests(Both likes and favourite books) of the current profile as a list
    currentInterest = documentPreparation(current_profile)
    # matchedInterest stores the interests(Both likes and favourite books) of the matching profile as a list
    matchedInterest = documentPreparation(matching_profile)

    # combinedInterest stores a list of string values containing the compiled interest of the current profile and matched interest
    combinedInterest = currentInterest + matchedInterest

    # cleanedDocument processes and cleans the compiled interest, returning lemmatized(base forms) of the words in combinedInterest
    cleanedDocument = documentPreprocessing(combinedInterest)

    #  The function documentTermMatrix returns the latent topics of the compiled interest, arranging the words according to their appearance as a list
    listOfMostSignificantTopic = document_term_matrix(cleanedDocument)

    # This is the api key for eventBrite
    eventbrite = Eventbrite('2AFR6PPQRSQS62J2CLIK')
    # eventCategoriesDict stores all the eventbrite id references into a dictionary
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

    # synSetDict2 stores the synsets of the events categories from eventbrite
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
                    # The similarity percentage will be stored in a dictionary with the key being the 2 matching words
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
    # list_of_date_suggestions = [{"name": event["name"]["text"], "description": event["description"]["text"], "url": event["url"]} for event in eventbrite.get(path="/events/search/", data={"categories": category_id})["events"][:5]]
    list_of_date_suggestions = [{"name": event["name"]["text"], "url": event["url"]} for event in eventbrite.get(path="/events/search/", data={"categories": category_id})["events"][:5]]

    # print "For the matched profile: " + matching_profile["name"]
    # print "The one of the ideal event type for your first date is: " + event_category_value
    # print "Here are 5 suggestions from EventBrite:"
    # # Prints out the list of best date suggestions
    # # This is the final desired output
    # print list_of_date_suggestions

    return {
        "name": matching_profile["name"],
        "gender": matching_profile["gender"],
        "country": matching_profile["country"],
        "age": matching_profile["age"],
        "eventCategory": event_category_value,
        "listOfEvents": list_of_date_suggestions
    }


# Returns the likes and favourite books of the profile given as interest
def documentPreparation(profile):
    interest = profile['likes'] + profile['books']
    return interest


def documentPreprocessing(corpus):
    # Cleaning and preprocessing

    # Places known natural language stopwords such as "a","the" into a set
    stop = set(stopwords.words('english'))

    # Places known punctuations into a set
    punc = set(string.punctuation)
    # Performs lemmatization on the word to convert it to its base form
    # This considers the context
    # It will return the original input if it fails
    lemma = WordNetLemmatizer()

    # Cleans each list item in the the given text(corpus)
    def document_cleaning(doc):
        stopwords_removed = " ".join([index for index in doc.lower().split() if index not in stop])
        punctuation_removed = ''.join(index for index in stopwords_removed if index not in punc)
        documents_normalized = " ".join(lemma.lemmatize(word) for word in punctuation_removed.split())
        return documents_normalized

    # Run the cleaning function for each list item then stores them into cleanedDocument
    cleanedDocument = [document_cleaning(doc).split() for doc in corpus]
    return cleanedDocument


#This functions performs the latent dirichlet allocations algorithm to get the latent topics in the interest of both profiles and group them accordingly
def document_term_matrix(cleanedDocument):

    # Assigns a unique token to each unique term
    # Dictionary(5 unique tokens: [u'chop', u'chicken', u'garlic', u'durain', u'swimming'])
    dictionary_unique = corpora.Dictionary(cleanedDocument)

    # Converts the text-based corpus into a matrix representation
    # dictionary.doc2bow converts the document into a list of token_id(I.E Unique tokens) and token_count tuples
    matrix_representation = [dictionary_unique.doc2bow(doc) for doc in cleanedDocument]

    lda_object = gensim.models.ldamodel.LdaModel

    # To determine optimal amount of topics for a dataset like ours, i chose 5
    # http://www.rpubs.com/MNidhi/NumberoftopicsLDA
    lda_model = lda_object(matrix_representation, num_topics=5, id2word=dictionary_unique, passes=200)

    # Returns all the most significant topics, arranging the topics and words by significance
    return lda_model.print_topics(num_topics=5, num_words=1)




