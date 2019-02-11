import collections
import matplotlib.pyplot as plt
from io import BytesIO


#  Gets all users' likes  and represents it in a pie chart
def display_data_likes(profiles):
    user_like_keys = []
    likes = []
    # Stores dictionary keys into user_likes_keys
    for i in profiles.keys():
        user_like_keys.append(i)
    # Stores the values into profile_like temporarily and appends values to a dictionary
    for i in user_like_keys:
        profile_like = profiles[i]['likes']
        for x in profile_like:
            likes.append(x)
    # Gets top 5 most common factors
    counter = collections.Counter(likes)
    common = dict(counter.most_common(5))
    # Instantiates pie chart with top 5 common factors as its elements and its keys as labels
    plt.pie([str(v) for v in common.values()], labels=[str(k) for k in common],
            autopct='%1.1f%%', startangle=90)

    # Save pie chart in png format
    figure = BytesIO()
    plt.savefig(figure, format="png", bbox_inches="tight")
    figure.seek(0)
    # Clear pie chart
    plt.clf()
    # Return pie chart bytes
    return figure


#  Gets all users' dislikes  and represents it in a pie chart
def display_data_dislikes(profiles):
    user_dislikes_keys = []
    dislikes = []
    # Stores dictionary keys into user_dislikes_keys
    for i in profiles.keys():
        user_dislikes_keys.append(i)
    # Stores the values into profile_dislikes temporarily and appends values to a dictionary
    for i in user_dislikes_keys:
        profile_dislikes = profiles[i]['dislikes']
        for x in profile_dislikes:
            dislikes.append(x)
    # Gets top 5 most common factors
    counter = collections.Counter(dislikes)
    common = dict(counter.most_common(5))

    # Instantiates pie chart with top 5 common factors as its elements and its keys as labels
    plt.pie([str(v) for v in common.values()], labels=[str(k) for k in common],
            autopct='%1.1f%%', startangle=90)

    # Save pie chart in png format
    figure = BytesIO()
    plt.savefig(figure, format="png", bbox_inches="tight")
    figure.seek(0)
    # Clear pie chart
    plt.clf()
    # Return pie chart bytes
    return figure


#  Gets all users' nationality and represents it in a pie chart
def display_data_nationality(profiles):
    user_nationality_keys = []
    nationalities = []
    # Stores dictionary keys into user_nationality_keys
    for i in profiles.keys():
        user_nationality_keys.append(i)
    # Stores the values into nationalities
    for i in user_nationality_keys:
        nationalities.append(profiles[i]['country'])

    # Gets top 5 most common factors
    counter = collections.Counter(nationalities)
    common = dict(counter.most_common(5))

    # Instantiates pie chart with top 5 common factors as its elements and its keys as labels
    plt.pie([str(v) for v in common.values()], labels=[str(k) for k in common],
            autopct='%1.1f%%', startangle=90)

    # Save pie chart in png format
    figure = BytesIO()
    plt.savefig(figure, format="png", bbox_inches="tight")
    figure.seek(0)
    # Clear pie chart
    plt.clf()
    # Return pie chart bytes
    return figure


#  Gets all users' age and represents it in a pie chart
def display_data_age(profiles):
    user_age_keys = []
    _user_ages = []
    # Stores dictionary keys into user_age_keys
    for i in profiles.keys():
        user_age_keys.append(i)
    # Stores the values into _user_ages
    for i in user_age_keys:
        _user_ages.append(profiles[i]['age'])

    # Gets top 5 most common factors
    counter = collections.Counter(_user_ages)
    common = dict(counter.most_common(5))
    
    # Instantiates pie chart with top 5 common factors as its elements and its keys as labels
    plt.pie([str(v) for v in common.values()], labels=[str(k) for k in common],
            autopct='%1.1f%%', startangle=90)

    # Save pie chart in png format
    figure = BytesIO()
    plt.savefig(figure, format="png", bbox_inches="tight")
    figure.seek(0)
    # Clear pie chart
    plt.clf()
    # Return pie chart bytes
    return figure
