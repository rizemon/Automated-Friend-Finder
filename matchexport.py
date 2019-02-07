from datetime import date
import csv
import os

# Sample data :: TO DELETE
# notice how I didn't write into william.py because I simply completely forgotten about it
# well I'm just like fk it man, you're gonna rename this into some other script anyways right?

output = [{'gender': 'F', 'age': 22, 'name': 'Angela Little', 'country': 'Singapore'},
          {'gender': 'M', 'age': 29, 'name': 'Joel Jackson', 'country': 'Singapore'},
          {'gender': 'F', 'age': 25, 'name': 'Rose', 'country': 'Singapore'},
          {'gender': 'F', 'age': 25, 'name': 'Jenny Wang', 'country': 'China'},
          {'gender': 'F', 'age': 22, 'name': 'Teresa', 'country': 'Singapore'},
          {'gender': 'F', 'age': 22, 'name': 'Lisa Marie', 'country': 'Singapore'},
          {'gender': 'F', 'age': 23, 'name': 'Carol', 'country': 'USA'},
          {'gender': 'F', 'age': 24, 'name': 'Shelley', 'country': 'China'},
          {'gender': 'M', 'age': 25, 'name': 'Kevin', 'country': 'Singapore'},
          {'gender': 'M', 'age': 29, 'name': 'Michael Jackson', 'country': 'Singapore'}]


# For JiaLe, Please input the match output into the function's args and adjust accordingly

def export_matches():
    # Checks whether output folder is present, if not then it will create for the user
    file_output_directory = r"..//output//"
    if not os.path.exists(file_output_directory):
        os.mkdir(file_output_directory)
    # Starts the process of writing the csv file normal out put would be BestMatch_<date>.csv
    # e.g BestMatch_2019-02-07.csv
    f = open(os.path.join(file_output_directory, "BestMatch_{}".format(date.today()) + '.csv'), "w")
    # Sets the field header names for the CSV file
    writer = csv.DictWriter(
        f, fieldnames=["name", "gender", "age", "country"])
    writer.writeheader()
    # For loop to write every dictionary in the list<dictionary> into the csv file
    for dictionary in output:
        writer.writerows([{"name": dictionary['name'], "gender": dictionary['gender'], "age": dictionary['age'], "country": dictionary['country']}])
    f.close()
