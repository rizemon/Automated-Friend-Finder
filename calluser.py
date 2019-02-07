import getfilepath
import os
from os.path import join
from yongjiefuncs import format_list, person_title, integer_input


def select_user(profiles):
    # print all user names
    index = 1
    for name, profile in profiles.items():
        title = person_title(profile['gender'])
        print("{}. {} {}".format(index,title, name))
        index += 1

    profile_index = integer_input("Enter a profile number to select")
    while profile_index > len(profiles):
        profile_index = integer_input("Invalid profile number ! \nEnter a profile number to select")
    # get profile from selected index
    user_profile = profiles.values()[profile_index - 1]
    # delete that profile from list
    del profiles[user_profile['name']]
    # return profile
    return user_profile


def valid_gender(gender):
    # check whether user is entering valid identifier for Male or Female
    return gender == 'M' or gender == 'F' or gender == 'm' or gender == 'f'


def valid_acceptable_range(age):
    # check whther user is entering valid range e.g 10-20 (int)-(int)
    try:
        if '-' in age:
            int(age.split('-')[0])
            int(age.split('-')[1])
            return True
    except Exception:
        pass
    return False


def input_user():
    # input users data to be registered in profiles folder
    user = dict()

    user['name'] = raw_input("Enter Name ! \n")

    valid_age = False
    while not valid_age:
        age = raw_input("\nEnter Age\n")
        try:
            user['age'] = int(age)
            valid_age = True
        except ValueError as err:
            print("Bad age value! try again")

    gender = raw_input("\nEnter gender [M/F]\n")
    while not valid_gender(gender):
        gender = raw_input("\nInvalid input ! Enter gender [M/F]\n")
    user['gender'] = 'Male' if gender == 'M' else 'Female'

    user['likes'] = raw_input("\nEnter likes with comma (,) separated\n")
    user['dislikes'] = raw_input("\nEnter dislikes with comma (,) separated\n")
    user['country'] = raw_input("\nEnter Country\n")
    user['acceptable_country'] = raw_input("\nEnter acceptable_country with comma (,) separated\n")

    age_range = raw_input("\nEnter acceptable_age_range with dash (-) separated\n")

    while not valid_acceptable_range(age_range):
        age_range = raw_input("\nInvalid range! Enter acceptable_age_range with dash (-) separated\n")

    user['acceptable_age_range'] = age_range
    user['books'] = raw_input("\nEnter books with comma (,) separated\n")
    return user


def convert_user_dict_to_str(user):
    # intiilize an empty string to convert dict in below format

    books = user['books'].split(',')
    books = format_list(books)

    line = ''
    line += 'Name: {}\n'.format(user['name'])
    line += 'Gender: {}\n'.format(user['gender'])
    line += 'Country: {}\n'.format(user['country'])
    line += 'Acceptable_country: {}\n'.format(user['acceptable_country'])
    line += 'Age: {}\n'.format(user['age'])
    line += 'Acceptable_age_range: {}\n'.format(user['acceptable_age_range'])
    line += 'Likes: {}\n'.format(user['likes'])
    line += 'Dislikes: {}\n'.format(user['dislikes'])
    line += '\n'
    line += 'Books:\n'
    line += "\n".join(books)
    return line


def get_last_user(directory):
    # get max file numebr in proifiles folder so next profile can be saved in an
    # incremental way
    max_user = 0
    for _file in os.listdir(directory):
        file_number = os.path.splitext(_file)[0]
        file_number = int(file_number)
        if max_user < file_number:
            max_user = file_number
    return max_user


def add_new_user():
    # this is main function which helps us getting new user data and save into profiles folder
    directory = getfilepath.getFilePath()
    # input user data into a dictionary
    user = input_user()
    # convert dictionary to string
    lines = convert_user_dict_to_str(user)
    # get max file numebr from prfiles folder
    last_max_file = get_last_user(directory)
    # e.g max file is 13.txt new file should be 14.txt
    next_user = '{}.txt'.format(last_max_file + 1)
    # save users data into pfoile folder
    with open(join(directory, next_user), 'w+') as file_to_write:
        file_to_write.write(lines)
