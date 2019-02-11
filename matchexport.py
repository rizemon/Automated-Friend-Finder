from datetime import date
import csv
import os


def export_matches(name, category, list_of_profiles,  file_output_directory):
    # Checks whether output folder is present, if not then it will create for the user
    if not os.path.exists(file_output_directory):
        os.mkdir(file_output_directory)

    # Starts the process of writing the csv file normal out put would be <name>_BestMatch_<category>_<date>.csv
    # e.g Carol_BestMatch_overall_2019-02-09.csv
    filename = os.path.join(file_output_directory, "{}_BestMatch_{}_{}.csv".format(name, category, date.today()))
    f = open(filename, "w")
    # Sets the field header names for the CSV file
    writer = csv.DictWriter(
        f, fieldnames=["name", "gender", "age", "country"])
    writer.writeheader()
    # For loop to write every dictionary in the list<dictionary> into the csv file
    for dictionary in list_of_profiles:
        writer.writerows([{"name": dictionary['name'], "gender": dictionary['gender'], "age": dictionary['age'], "country": dictionary['country']}])
    f.close()