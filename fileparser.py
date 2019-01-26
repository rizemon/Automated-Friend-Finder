from json import dumps


def pretty_print(dictionary):

    # Pretty prints a dictionary

    print dumps(dictionary, sort_keys=False, indent=4)


def parse(doc):

    # Takes in an opened file, parses the different fields and updates the
    # profiles dictionary

    profile = {}
    lines = [i.strip() for i in doc.readlines()]
    name = lines[0][len("Name:"):].strip()
    gender = lines[1][len("Gender:"):].strip()
    if gender in ["Male", "M"]:
        gender = "M"
    else:
        gender = "F"
    country = lines[2][len("Country:"):].strip()
    acceptable_country = [i.strip()
                          for i in lines[3][len("Acceptable_country:"):]
                              .strip().split(',')]
    age = lines[4][len("Age:"):].strip()
    acceptable_age_range = lines[5][len("Acceptable_age_range:"):].strip()\
        .split('-')
    likes = [i.strip()
             for i in lines[6][len("Likes:"):].strip().split(',') if i != ""]
    dislikes = [i.strip()
                for i in lines[7][len("Dislikes:"):].strip().split(',') if i != ""]
    books = [i.strip()
             for i in lines[10:] if i != ""]
    profile = {
        "gender": gender[0],
        "country": country,
        "acceptable_country": acceptable_country,
        "age": int(age),
        "acceptable_age_range": {
            "start": int(acceptable_age_range[0]),
            "end": int(acceptable_age_range[1]) + 1,
        },
        "likes": likes,
        "dislikes": dislikes,
        "books": books
    }
    return name, profile
