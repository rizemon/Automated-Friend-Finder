import yongjiefuncs
from yongjiefuncs import pretty_print_yj

    # Function 1: List all the names, gender and age from all the profiles

def view_profiles (profiles):
    for row in profiles.values():
        title = yongjiefuncs.person_title(row['gender'])
        full_gender = yongjiefuncs.full_gender(row['gender'])
    all_profile_output = yongjiefuncs.user_profile_to_list(profiles.values())
    return all_profile_output


    # Function 2: List all the matched students of one given student B based on
    # country (e.g all the students that fall in to the acceptable country of
    # B should be printed out)

def matched_by_countries(username, profiles):
    # select user profile user username name
    user_profile = yongjiefuncs.get_profile_by_name(profiles=profiles, username=username)
    if not user_profile:
        return
    # Compare other user profile with the selected user acceptable country range
    filtered_profiles = yongjiefuncs.filter_same_gender(profiles=profiles, user_profile=user_profile)
    filtered_profiles = yongjiefuncs.filter_in_acceptable_age_range(filtered_profiles, user_profile)
    # reset dataframe from starting from index 1
    if not filtered_profiles:
        return []
    output_country = yongjiefuncs.user_profile_to_list(filtered_profiles)
    #return yongjiefuncs.user_profile_to_list(filtered_profiles)
    return output_country


    # Function 3: List the top 3 best matched students who share the most simliar
    # likes or dislikes for one given student B. Note that you may define one
    # similarity metrics (e.g # of shared likes/dislikes etc ) in order to rank
    # their similarity

def matched_likes(username, profiles):
    user_profile = yongjiefuncs.get_profile_by_name(profiles=profiles, username=username)
    if not user_profile:
        return
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
    if not likes:
        return []

    output_likes =yongjiefuncs.user_profile_to_list(likes)
    # pretty_print(test)
    return output_likes


def matched_dislikes(username, profiles):
    # filter by opp gender
    user_profile = yongjiefuncs.get_profile_by_name(profiles=profiles, username=username)
    if not user_profile:
        return []

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
        return []
    # yongjiefuncs.print_profile_lists(dislikes, reason="dislikes")
    # yongjiefuncs.eval(dislikes)
    output_dislikes =yongjiefuncs.user_profile_to_list(dislikes)
    #pretty_print(test)
    return output_dislikes
