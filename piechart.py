import collections
import matplotlib.pyplot as plt


#  Gets all users' likes  and represents it in a pie chart
def display_data_likes(profiles):
    user_like_keys = []
    likes = []
    for i in profiles.keys():
        user_like_keys.append(i)
    for i in user_like_keys:
        profilelike = profiles[i]['likes']
        for x in profilelike:
            likes.append(x)
    counter = collections.Counter(likes)
    common = dict(counter.most_common(5))

    plt.pie([str(v) for v in common.values()], labels=[str(k) for k in common],
            autopct='%1.1f%%', startangle=90)

    plt.show()


#  Gets all users' dislikes  and represents it in a pie chart
def display_data_dislikes(profiles):
    user_dislikes_keys = []
    likes = []
    for i in profiles.keys():
        user_dislikes_keys.append(i)
    for i in user_dislikes_keys:
        profile_dislikes = profiles[i]['dislikes']
        for x in profile_dislikes:
            likes.append(x)
    counter = collections.Counter(likes)
    common = dict(counter.most_common(5))

    plt.pie([str(v) for v in common.values()], labels=[str(k) for k in common],
            autopct='%1.1f%%', startangle=90)

    plt.show()


#  Gets all users' nationality and represents it in a pie chart
def display_data_nationality(profiles):
    user_nationality_keys = []
    likes = []
    for i in profiles.keys():
        user_nationality_keys.append(i)
    for i in user_nationality_keys:
        likes.append(profiles[i]['country'])

    counter = collections.Counter(likes)
    common = dict(counter.most_common(5))

    plt.pie([str(v) for v in common.values()], labels=[str(k) for k in common],
            autopct='%1.1f%%', startangle=90)

    plt.show()


#  Gets all users' age and represents it in a pie chart
def display_data_age(profiles):
    user_age_keys = []
    likes = []
    for i in profiles.keys():
        user_age_keys.append(i)
    for i in user_age_keys:
        likes.append(profiles[i]['age'])

    counter = collections.Counter(likes)
    common = dict(counter.most_common(5))

    plt.pie([str(v) for v in common.values()], labels=[str(k) for k in common],
            autopct='%1.1f%%', startangle=90)

    plt.show()
