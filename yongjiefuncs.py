# this file has all utility function to use and reuse in project


def format_str(to_format_str):
    # remove unwanted spaces e.g input 'jackson ' output 'jackson'
    return to_format_str.strip()


def format_list(to_format_list):
    return [format_str(x) for x in to_format_list]


def clear_shell():
    # print 20 empty lines for main menu
    print "\n" * 20


def person_title(gender):
    # get title by gender
    return 'Mr' if format_str(gender) == 'M' else 'Ms'


def full_gender(gender):
    # get full gender of profiles
    return 'Male' if gender == 'M' else 'Female'


def similarities(user_likes, target):
    # this function calculates likes or dislikes score
    # common_user_likes = all those likes which are in target too
    # filtered_target = all likes in newly created common_user_likes list

    # eg. common_user_likes = ["onion","chicken", "banana"]
    # target = ["chicken and soup", "burger", "banana"]
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

#store to dict i set to none because we dont want to save logs in case of function 1
def eval(profiles):
    # this function lets user to see profiles of users by states function
    # e.g profile by matched country
    # 1- Mr A
    # 2- Mr B
    # when user enters 2 it will show compete profile of Mr B
    index = -1
    while index != 0:
        index = integer_input("Enter profile index to view profile , Enter 0 to quit")
        if index == 0:
            return
        if index > len(profiles):
            print("Index out of bound. Please enter again !")
        else:
            #print_profile(profiles[index - 1])
            user_profile = profiles[index - 1]


            # this function prints profile on console, remove this if not required
            print_profile(user_profile)
            # #
            # if storetodict is not None:
            #     storetodict.append({
            #         'name': user_profile['name'],
            #         'gender': user_profile['gender'],
            #         'age': user_profile['age'],
            #         'country': user_profile['country']
            #     })






def list_to_str(to_convert):
    # this function converts a list to string separated by ,
    return ", ".join(to_convert)


def integer_input(message):
    # this function helps in taking integer input from user
    # this function will keep taking input util user does not input a valid integer
    while True:
        num = raw_input(message)
        try:
            return int(num)
        except ValueError:
            print("Input is not a valid integer! please try again")


def print_profile(row):
    # print complete profile of a user

    title = person_title(row['gender'])
    gender = full_gender(row['gender'])
    likes = list_to_str(row['likes'])
    dislikes = list_to_str(row['dislikes'])
    books = ",\n".join(row['books'])

    print
    print('{} {} \n'
          'Age: {}\n'
          'Country: {}\n'
          'Gender: {}\n'
          'Likes: {}\n'
          'Dislikes: {}\n'
          '\nBooks: \n{}'.format(title,
                                 row['name'], row['age'],
                                 row['country'], gender,
                                 likes, dislikes, books
                                 ))


def print_profile_lists(profiles, reason):
    # this function print top 3 profiles for function 3 and 4
    index = 1
    for profile in profiles:
        title = person_title(profile['gender'])

        reason_value = profile[reason]
        if type(profile[reason]) == list:
            reason_value = ", ".join(profile[reason])

        print('{}. {} {}, Age {}, {}: {}'.format(
            index, title, profile['name'], profile['age'], reason, reason_value))

        # if storetodict is not None:
        #     storetodict.append({
        #         'name': profile['name'],
        #         'gender': profile['gender'],
        #         'age': profile['age'],
        #         'country': profile['country']
        #     })
        index += 1
    #print storetodict

def filter_same_gender(user_profile, profiles):
    # this function filter same gender from profiles
    user_gender = user_profile['gender']
    return {k: v for k, v in profiles.items() if user_gender != v['gender']}


def filter_in_acceptable_age_range(profiles, user_profile):
    # this function filters profiles not in acceptable range of logged user
    acceptable_country = user_profile['acceptable_country']
    return [p for p in profiles.values() if p['country'] in acceptable_country]


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
