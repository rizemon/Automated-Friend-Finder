from datetime import date
import csv
import os

best_match_likes = [{'gender': 'F', 'age': 22, 'name': 'Angela Little', 'country': 'Singapore'},
          {'gender': 'M', 'age': 29, 'name': 'Joel Jackson', 'country': 'Singapore'},
          {'gender': 'F', 'age': 25, 'name': 'Rose', 'country': 'Singapore'},
          {'gender': 'F', 'age': 25, 'name': 'Jenny Wang', 'country': 'China'},
          {'gender': 'F', 'age': 22, 'name': 'Teresa', 'country': 'Singapore'},
          {'gender': 'F', 'age': 22, 'name': 'Lisa Marie', 'country': 'Singapore'},
          {'gender': 'F', 'age': 23, 'name': 'Carol', 'country': 'USA'},
          {'gender': 'F', 'age': 24, 'name': 'Shelley', 'country': 'China'},
          {'gender': 'M', 'age': 25, 'name': 'Kevin', 'country': 'Singapore'},
          {'gender': 'M', 'age': 29, 'name': 'Michael Jackson', 'country': 'Singapore'}]

best_match_dislikes = [{'gender': 'F', 'age': 22, 'name': 'Angela Little', 'country': 'Singapore'},
          {'gender': 'M', 'age': 29, 'name': 'Joel Jackson', 'country': 'Singapore'},
          {'gender': 'F', 'age': 25, 'name': 'Rose', 'country': 'Singapore'},
          {'gender': 'F', 'age': 25, 'name': 'Jenny Wang', 'country': 'China'},
          {'gender': 'F', 'age': 22, 'name': 'Teresa', 'country': 'Singapore'},
          {'gender': 'F', 'age': 22, 'name': 'Lisa Marie', 'country': 'Singapore'},
          {'gender': 'F', 'age': 23, 'name': 'Carol', 'country': 'USA'},
          {'gender': 'F', 'age': 24, 'name': 'Shelley', 'country': 'China'},
          {'gender': 'M', 'age': 25, 'name': 'Kevin', 'country': 'Singapore'},
          {'gender': 'M', 'age': 29, 'name': 'Michael Jackson', 'country': 'Singapore'}]

best_match_books = [{'gender': 'F', 'age': 22, 'name': 'Angela Little', 'country': 'Singapore'},
          {'gender': 'M', 'age': 29, 'name': 'Joel Jackson', 'country': 'Singapore'},
          {'gender': 'F', 'age': 25, 'name': 'Rose', 'country': 'Singapore'},
          {'gender': 'F', 'age': 25, 'name': 'Jenny Wang', 'country': 'China'},
          {'gender': 'F', 'age': 22, 'name': 'Teresa', 'country': 'Singapore'},
          {'gender': 'F', 'age': 22, 'name': 'Lisa Marie', 'country': 'Singapore'},
          {'gender': 'F', 'age': 23, 'name': 'Carol', 'country': 'USA'},
          {'gender': 'F', 'age': 24, 'name': 'Shelley', 'country': 'China'},
          {'gender': 'M', 'age': 25, 'name': 'Kevin', 'country': 'Singapore'},
          {'gender': 'M', 'age': 29, 'name': 'Michael Jackson', 'country': 'Singapore'}]

best_match_overall = [{'gender': 'F', 'age': 22, 'name': 'Angela Little', 'country': 'Singapore'},
          {'gender': 'M', 'age': 29, 'name': 'Joel Jackson', 'country': 'Singapore'},
          {'gender': 'F', 'age': 25, 'name': 'Rose', 'country': 'Singapore'},
          {'gender': 'F', 'age': 25, 'name': 'Jenny Wang', 'country': 'China'},
          {'gender': 'F', 'age': 22, 'name': 'Teresa', 'country': 'Singapore'},
          {'gender': 'F', 'age': 22, 'name': 'Lisa Marie', 'country': 'Singapore'},
          {'gender': 'F', 'age': 23, 'name': 'Carol', 'country': 'USA'},
          {'gender': 'F', 'age': 24, 'name': 'Shelley', 'country': 'China'},
          {'gender': 'M', 'age': 25, 'name': 'Kevin', 'country': 'Singapore'},
          {'gender': 'M', 'age': 29, 'name': 'Michael Jackson', 'country': 'Singapore'}]

def export_matches():
    # Dictionary_list stores the all the dictionaries (best match by like,dislike,books read and profile info)
    # into a list so that it can be looped to create the csv
    # Dictionary_names are hardcoded because the order will not change
    dictionary_list = []
    dictionary_names = ["Top 3 best match by likes", "Top 3 best match by dislikes", "Top 3 best match by books read", "Top 3 best match by profile information"]
    dictionary_list.append(best_match_likes)
    dictionary_list.append(best_match_dislikes)
    dictionary_list.append(best_match_books)
    dictionary_list.append(best_match_overall)

    # Checks whether output folder is present, if not then it will create for the user
    file_output_directory = r"..//output//"
    if not os.path.exists(file_output_directory):
        os.mkdir(file_output_directory)
    # Starts the process of writing the csv file normal out put would be BestMatch_<date>.csv
    # e.g BestMatch_2019-02-07.csv
    f = open(os.path.join(file_output_directory, "BestMatch_{}".format(date.today()) + '.csv'), "w")
    for index,dictionary in enumerate(dictionary_list):
        f.write("{}\n".format(dictionary_names[index]))
        # Sets the field header names for the CSV file
        writer = csv.DictWriter(
            f, fieldnames=["name", "gender", "age", "country"])
        writer.writeheader()
        # For loop to write every dictionary in the list<dictionary> into the csv file
        for dictionary_item in dictionary:
            writer.writerows([{"name": dictionary_item['name'], "gender": dictionary_item['gender'], "age": dictionary_item['age'], "country": dictionary_item['country']}])
    f.close()

