from fileparser import pretty_print
import getfilepath
import piechart

from os.path import isdir, abspath
from os import remove
from sys import exit
from flask import Flask, jsonify, Response, request, send_from_directory
from flask_cors import CORS

import yongjie
import ronghao
import kijoon
import jiale
import matchexport


# Initialize Flask application
app = Flask(__name__)
# Enable CORS
CORS(app)

# profiles dictionary to be accessed by all functions
profiles = {}
piecharts = {}
matches_books = {}


def getMatches(profile_name, field):
    result = []
    if field == "country":
        # Retrieve best matches by country
        result = [{"name": name, "gender": profiles[name]["gender"], "age": profiles[name]["age"],
                   "country": profiles[name]["country"]} for name in profiles]
    elif field == "likes":
        # Retrieve best matches by likes/dislikes
        result = [{"name": name, "gender": profiles[name]["gender"], "age": profiles[name]["age"],
                   "country": profiles[name]["country"]} for name in profiles]
    elif field == "books":
        # Retrieve best matches by books
        result = jiale.viewMatchesBooks(profiles, matches_books, profile_name)
    elif field == "overall":
        # Retrieve best matches by overall information
        result = ronghao.viewMatchesOverall(profiles, profile_name)

    return result


@app.route('/')
def index():
    return send_from_directory('static', "index.html")


@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)


@app.route('/all')
def viewAll():

    # Return a JSON of an array of all profiles

    resp = [{"name": name, "gender": profiles[name]["gender"], "age": profiles[name]["age"],
             "country": profiles[name]["country"]} for name in profiles]

    # Output as JSON
    return jsonify(resp)

@app.route('/bestmatch/<string:field>')
def viewBestMatch(field):

    # Return a JSON of an array of best matches based on field and profile's name

    # Retrieve name from GET parameters
    profile_name = request.args.get("current_profile")

    resp = getMatches(profile_name, field)

    # Output as JSON
    return jsonify(resp)


@app.route('/piechart/<string:field>')
def plotPiechart(field):

    # Return a PNG of the plotted pie chart based on field

    # If unsupported field, return 204
    if field not in piecharts:
        return '', 204

    # Output as png file
    figure = piecharts[field]
    return Response(figure.getvalue(), mimetype='image/png')


@app.route('/csv', methods=['POST'])
def saveCSV():
    # Path where the .csv files will be stored
    directory = abspath(r".//output//")
    # Retrieve JSON body
    req = request.get_json()
    current_profile = req.get("current_profile")
    # Export each list of best matches to .csv
    for field in ["likes", "books", "overall"]:
        matchexport.export_matches(current_profile, field, getMatches(current_profile, field), directory)
    # Output the absolute path of where .csv are stored
    return jsonify({"message": directory})


if __name__ == "__main__":
    # Get directory of profiles
    directory = ""
    while True:
        directory = getfilepath.getFilePath()
        if not isdir(directory):
            print "Folder does not exist."
            remove("path.txt")
        else:
            break


    print "Reading profiles from %s now..." % directory

    # Read the profiles and store in profiles dictionary
    profiles = getfilepath.getProfiles(directory)
    # For debugging purposes
    # pretty_print(profiles)

    # Function 1,2,3 (Based on Project 1 Description.pdf)
    yongjie.viewProfiles(profiles)
    yongjie.viewMatchesCountry(profiles)
    yongjie.viewMatchesLikesDislikes(profiles)

    # Function 4
    matches_books = jiale.getMatchesBooks(profiles)

    # Pre-compute all pie charts
    piecharts["likes"] = piechart.display_data_likes(profiles)
    piecharts["dislikes"] = piechart.display_data_dislikes(profiles)
    piecharts["country"] = piechart.display_data_nationality(profiles)
    piecharts["age"] = piechart.display_data_age(profiles)

    # Open function
    kijoon.openFunction(profiles)

    # Start Flask application on port 80 for loopback interface
    app.run(host="127.0.0.1", port=80, threaded=True)


