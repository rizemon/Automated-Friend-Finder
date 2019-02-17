import yongjiefuncs

    # Function 1: List all the names, gender and age from all the profiles

def view_profiles (profiles):
    all_profile_output = yongjiefuncs.user_profile_to_list(profiles.values())
    return all_profile_output


    # Function 2: List all the matched students of one given student B based on
    # country (e.g all the students that fall in to the acceptable country of
    # B should be printed out)

def matched_by_countries(username, profiles):
    #check if profile given is true
    user_profile = yongjiefuncs.get_profile_by_name(profiles=profiles, username=username)
    if not user_profile:
        return

    # Compare other user profile with the selected user acceptable country range
    filtered_profiles = yongjiefuncs.filter_same_gender(profiles=profiles, user_profile=user_profile)

    filtered_profiles = yongjiefuncs.filter_in_acceptable_country_range(filtered_profiles, user_profile)
    # reset the list to [] if No Matched profile is found

    # filter profile by acceptable age range
    filtered_profiles = yongjiefuncs.filter_in_acceptable_age_range(filtered_profiles, user_profile)

    if not filtered_profiles:
        return []

    # return output in dict format
    output_country = yongjiefuncs.user_profile_to_list(filtered_profiles)
    return output_country


    # Function 3: List the top 3 best matched students who share the most simliar
    # likes or dislikes for one given student B. Note that you may define one
    # similarity metrics (e.g # of shared likes/dislikes etc ) in order to rank
    # their similarity

def matched_likes(username, profiles):
    # check if profile given is true
    user_profile = yongjiefuncs.get_profile_by_name(profiles=profiles, username=username)
    if not user_profile:
        return

    # filter by opp gender
    filtered_profiles = yongjiefuncs.filter_same_gender(profiles=profiles, user_profile=user_profile)

    # filter profile by acceptable country range
    filtered_profiles = yongjiefuncs.filter_in_acceptable_country_range(filtered_profiles, user_profile)

    # filter profile by acceptable age range
    filtered_profiles = yongjiefuncs.filter_in_acceptable_age_range(filtered_profiles, user_profile)

    # get similarity count for each user
    for profile in filtered_profiles:
        profile['similar_likes'] = yongjiefuncs.similarities(
            user_likes=user_profile['likes'], target=profile['likes']
        )

    # sort users by similarity likes and get top 3 results
    likes = yongjiefuncs.top_profiles(profiles=filtered_profiles, key='similar_likes')

    #If user dosen't have any matched likes return empty
    if not likes:
        return []

    #return output in dict format
    output_likes =yongjiefuncs.user_profile_to_list(likes)
    return output_likes


def matched_dislikes(username, profiles):

    #check if profile given is true
    user_profile = yongjiefuncs.get_profile_by_name(profiles=profiles, username=username)
    if not user_profile:
        return []

    # filter by opp gender
    filtered_profiles = yongjiefuncs.filter_same_gender(profiles=profiles, user_profile=user_profile)

    # filter profile by acceptable country
    filtered_profiles = yongjiefuncs.filter_in_acceptable_country_range(filtered_profiles, user_profile)
    user_dislikes = user_profile['dislikes']

    # filter profile by acceptable age range
    filtered_profiles = yongjiefuncs.filter_in_acceptable_age_range(filtered_profiles, user_profile)


    # get dissimilarity count for each user
    for profile in filtered_profiles:
        profile['similar_dislikes'] = \
            yongjiefuncs.similarities(user_likes=user_dislikes, target=profile['dislikes'])

    # sort users by similarity max likes and get top 3
    dislikes = yongjiefuncs.top_profiles(profiles=filtered_profiles, key='similar_dislikes')

    # If user dosen't have any matched dislikes found then allow them to select other functions.
    if not dislikes:
        return []

    output_dislikes =yongjiefuncs.user_profile_to_list(dislikes)
    return output_dislikes
