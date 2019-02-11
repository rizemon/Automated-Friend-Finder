
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
# dictionary mapping field name to respective pie chart
piecharts = {}
# dictionary mapping every possible pair of profiles to a similarity score
matches_books = {}



def getMatches(profile_name, field):

    # Returns the profiles that are matched according to
    # "country", "likes", "dislikes", "books", "overall", "suggestion"
    #
    # Parameters:
    # profile_name (string): name of current user
    # field (string): Either "country", "likes", "dislikes", "books", "overall", "suggestion"
    #
    # Returns:
    # (list): list of profiles matched based on field

    result = []
    if field == "country":
        # Retrieve best matches by country
        result = yongjie.matched_by_countries(profile_name, profiles)
    elif field == "likes":
        # Retrieve best matches by likes
        result = yongjie.matched_likes(profile_name, profiles)
    elif field == "dislikes":
        # Retrieve best matches by dislikes
        result = yongjie.matched_dislikes(profile_name, profiles)
    elif field == "books":
        # Retrieve best matches by books
        result = jiale.viewMatchesBooks(profiles, matches_books, profile_name)
    elif field == "overall":
        # Retrieve best matches by overall information
        result = ronghao.viewMatchesOverall(profiles, profile_name)
    elif field == "suggestion":
        result = kijoon.view_first_date_suggestions(profile_name, profiles)

    return result


@app.route('/', methods=['GET'])
def index():

    # Returns the index.html of the front-end application
    #
    # Parameters:
    #
    # Returns:
    # (Response): contents of index.html

    return send_from_directory('static', "index.html")


@app.route('/<path:filename>', methods=['GET'])
def static_files(filename):

    # Returns the static files (HTML, CSS ,JS) of the front-end application
    #
    # Parameters:
    # filename (string): file name of the static files
    #
    # Returns:
    # (Response): contents of static file

    return send_from_directory('static', filename)


@app.route('/single', methods=['GET'])
def viewProfile():

    # Returns a JSON of the profile information of a given profile_name
    #
    # Parameters:
    #
    # Returns:
    # (Response): JSON of profile information

    profile_name = request.args.get("profile_name")
    return jsonify(profiles[profile_name])


@app.route('/all', methods=['GET'])
def viewAll():

    # Return a JSON of a list of all profiles
    #
    # Parameters:
    #
    # Returns:
    # (Response): JSON of list of profiles' information

    resp = yongjie.view_profiles(profiles)

    # Output as JSON
    return jsonify(resp)


@app.route('/bestmatch/<string:field>', methods=['GET'])
def viewBestMatch(field):

    # Return a JSON of a list of best matches based on field of a given profile
    #
    # Parameters:
    # field (string): Either "country", "likes", "dislikes", "books", "overall", "suggestion"
    #
    # Returns:
    # (Response): JSON of list of best matched profiles' information


    # Retrieve profile's name from GET parameters
    profile_name = request.args.get("current_profile")

    resp = getMatches(profile_name, field)

    # Output as JSON
    return jsonify(resp)


@app.route('/piechart/<string:field>', methods=['GET'])
def plotPiechart(field):

    # Return a PNG of the plotted pie chart based on field
    #
    # Parameters:
    # field (string): Either "country", "likes", "dislikes", "age"
    #
    # Returns:
    # (Response): PNG of pie chart plotted based on field

    # If unsupported field, return 204
    if field not in piecharts:
        return '', 204

    # Output as png file
    figure = piecharts[field]
    return Response(figure.getvalue(), mimetype='image/png')


@app.route('/csv', methods=['POST'])
def saveCSV():

    # Return a JSON of directory of the CSV saved
    #
    # Parameters:
    #
    # Returns:
    # (Response): JSON containing directory of CSV

    # Path where the .csv files will be stored
    directory = abspath(r".//output//")
    # Retrieve JSON body
    req = request.get_json()
    current_profile = req.get("current_profile")
    bestmatches_all = [getMatches(current_profile, field) for field in ["likes", "dislikes", "books", "overall"]]
    titles = [
        "Top 3 best match by likes",
        "Top 3 best match by dislikes",
        "Top 3 best match by books read",
        "Top 3 best match by overall profile information"
    ]
    matchexport.export_matches(current_profile, titles, bestmatches_all, directory)
    # Output the absolute path of where .csv are stored
    return jsonify({"message": directory})


if __name__ == "__main__":
    # Initialize profiles directory
    directory = ""

    while True:
        # Prompt for profiles directory
        directory = getfilepath.getFilePath()
        # Check if directory does not exist
        if not isdir(directory):
            print "Folder does not exist."
            # Delete path.txt if exist
            remove("path.txt")
        else:
            break

    print "Reading profiles from %s now..." % directory

    # Read the profiles and store in profiles dictionary
    profiles = getfilepath.getProfiles(directory)

    #Pre-compute matches based on interests
    matches_books = jiale.getMatchesBooks(profiles)

    # Pre-compute all pie charts
    piecharts["likes"] = piechart.display_data_likes(profiles)
    piecharts["dislikes"] = piechart.display_data_dislikes(profiles)
    piecharts["country"] = piechart.display_data_nationality(profiles)
    piecharts["age"] = piechart.display_data_age(profiles)

    # Start Flask application on port 80 for loopback interface
    app.run(host="127.0.0.1", port=80, threaded=True)

