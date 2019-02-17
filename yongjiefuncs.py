# this file has all utility function to use and reuse in project
from json import dumps

def format_str(to_format_str):
    # remove unwanted spaces e.g input 'jackson ' output 'jackson'
    return to_format_str.strip()


def format_list(to_format_list):
    return [format_str(x) for x in to_format_list]


def similarities(user_likes, target):
    # this function calculates likes or dislikes score
    # common_user_likes = all those likes which are in target too
    # filtered_target = all likes in newly created common_user_likes list

    # eg. common_user_likes = ["onion","chicken", "banana"]
    # target = ["chicken and soup", "burger", "banana"]
    # common_user_likes = ["onion","chicken", "banana"]
    # filtered_target = ["chicken and soup", "banana"]
    common_user_likes = [like for like in user_likes if like in target]
    # common_user_likes = ["chicken", "banana"]
    filtered_target = [t for t in target if t in common_user_likes]
    # filtered_target = ["chicken and soup", "banana"]

    # sort them both

    # before: filtered_target_likes["chicken and soup", "banana",]
    # common_user_likes = ["chicken", "banana"]
    common_user_likes.sort()
    filtered_target.sort()

    # after: common_user_likes = ["banana", "chicken"]
    # filtered_target_likes = ["banana", "chicken and soup"]

    # calculate points
    # example
    # 1- common_user_likes = ["chicken"], filtered_target = ["chicken and soup"] points = 0.5
    # 2- common_user_likes = ["chicken and soup"], filtered_target = ["chicken"] points = 0.5
    # 3- common_user_likes = ["chicken and soup"], filtered_target = ["chicken and soups"] points = 1
    points = 0
    for i in range(len(common_user_likes)):
        if common_user_likes[i] != filtered_target[i]:
            points += 0.5
        else:
            points += 1
    return points


def top_profiles(profiles, key, top=3):
    # key = likes or dislikes
    # this function sorts profile based on likes or dislikes score
    # and then returns top profiles default =
    # sort profiles based on likes or dislikes score
    ordered = sorted(profiles, key=lambda p: p[key], reverse=True)

    # return non 0 top profiles
    return [p for p in ordered[:top] if p[key]]


def list_to_str(to_convert):
    # this function converts a list to string separated by ,
    return ", ".join(to_convert)


def filter_same_gender(user_profile, profiles):
    # this function filter same gender from profiles
    user_gender = user_profile['gender']
    return {k: v for k, v in profiles.items() if user_gender != v['gender']}


def filter_in_acceptable_country_range(profiles, user_profile):
    # this function filters profiles not in acceptable range of login user
    acceptable_country = user_profile['acceptable_country']
    return [p for p in profiles.values() if p['country'] in acceptable_country]


def filter_in_acceptable_age_range(profiles, user_profile):
    # this function filters profiles not in acceptable range of logged user
    acceptable_age = user_profile['acceptable_age_range']
    lower_age_limit = acceptable_age['start']
    upper_age_limit = acceptable_age['end']
    return [p for p in profiles if lower_age_limit <= p['age'] <= upper_age_limit]

# return users profile in list format for func 2,3,4
def user_profile_to_list(users):
    list_of_users = []
    for user in users:
        list_of_users.append({
            'name': user['name'],
            'gender': user['gender'],
            'age': user['age'],
            'country': user['country']
        })

    return list_of_users

    #Search for the profile with the given user name for example "Michael Jackson"
    #If found return the profiles values else return error msg
def get_profile_by_name(username, profiles):
    user_profile = profiles.get(username, None)
    if not user_profile:
        raw_input("Error! No user found with username {}".format(username))
        return
    return user_profile


def pretty_print_yj(dictionary):
    # Pretty prints a dictionary

    results_dict = dumps(dictionary, sort_keys=False, indent=4)
    return results_dict
