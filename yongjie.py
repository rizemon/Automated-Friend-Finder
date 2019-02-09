import yongjiefuncs


    # Function 1: List all the names, gender and age from all the profiles

def view_profiles(profiles):
    index = 1
    for row in profiles.values():
        title = yongjiefuncs.person_title(row['gender'])
        full_gender = yongjiefuncs.full_gender(row['gender'])
        print('{}. {} {}, Gender: {}, Age {}'.format(
            index, title, row['name'], full_gender, row['age']
        ))
        index += 1
    yongjiefuncs.eval(profiles.values())


    # Function 2: List all the matched students of one given student B based on
    # country (e.g all the students that fall in to the acceptable country of
    # B should be printed out)

def matched_by_countries(user_profile, profiles, storetodict):
    # Compare other user profile with the selected user acceptable country range
    filtered_profiles = yongjiefuncs.filter_same_gender(profiles=profiles, user_profile=user_profile)
    filtered_profiles = yongjiefuncs.filter_in_acceptable_age_range(filtered_profiles, user_profile)
    # reset dataframe from starting from index 1
    if not filtered_profiles:
        print("No Matched profile found")
        raw_input("Enter any key to continue")
        return
    yongjiefuncs.print_profile_lists(filtered_profiles, reason="country", storetodict = storetodict)
    yongjiefuncs.eval(filtered_profiles)



    # Function 3: List the top 3 best matched students who share the most simliar
    # likes or dislikes for one given student B. Note that you may define one
    # similarity metrics (e.g # of shared likes/dislikes etc ) in order to rank
    # their similarity

def matched_likes(user_profile, profiles, storetodict):
    # filter by opp gender
    filtered_profiles = yongjiefuncs.filter_same_gender(profiles=profiles, user_profile=user_profile)
    # filter profile by acceptable age range
    filtered_profiles = yongjiefuncs.filter_in_acceptable_age_range(filtered_profiles, user_profile)

    for profile in filtered_profiles:
        profile['similar_likes'] = yongjiefuncs.similarities(
            user_likes=user_profile['likes'], target=profile['likes']
        )

    # sort users by similarity likes and get top 3 results
    likes = yongjiefuncs.top_profiles(profiles=filtered_profiles, key='similar_likes')

    #If user dosen't have any matched likes found then allow them to select other functions.
    #if no likes:
    if not likes:
        print("No matched Likes found")
        raw_input("Input any key to continue !")
        return

    yongjiefuncs.print_profile_lists(likes, reason="likes", storetodict = storetodict)
    yongjiefuncs.eval(likes)


def matched_dislikes(user_profile, profiles, storetodict):
    # filter by opp gender
    filtered_profiles = yongjiefuncs.filter_same_gender(profiles=profiles, user_profile=user_profile)
    # filter profile by acceptable age range
    filtered_profiles = yongjiefuncs.filter_in_acceptable_age_range(filtered_profiles, user_profile)
    user_dislikes = user_profile['dislikes']

    # get dissimilarity count for each user
    for profile in filtered_profiles:
        profile['similar_dislikes'] = \
            yongjiefuncs.similarities(user_likes=user_dislikes, target=profile['dislikes'])

    # sort users by similarity max likes and get top 3
    dislikes = yongjiefuncs.top_profiles(profiles=filtered_profiles, key='similar_dislikes')

    # If user dosen't have any matched dislikes found then allow them to select other functions.
    if not dislikes:
        print("No matching dislikes found")
        raw_input("Enter any key to continue !")
        return
    yongjiefuncs.print_profile_lists(dislikes, reason="dislikes", storetodict = storetodict)
    yongjiefuncs.eval(dislikes)
