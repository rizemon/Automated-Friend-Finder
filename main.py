from fileparser import pretty_print
import getfilepath
import piechart

from os.path import isdir
from sys import exit
from flask import Flask, jsonify, Response, request, abort, send_from_directory
from flask_cors import CORS

import yongjie
import ronghao
import kijoon
import jiale
import william

# Initialize Flask application
app = Flask(__name__)
# Enable CORS
CORS(app)

# profiles dictionary to be accessed by all functions
profiles = {}
piecharts = {}

@app.route('/')
def index():
    return send_from_directory('static', "index.html")


@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)


@app.route('/all')
def viewAll():

    # Return a JSON of an array of all profiles

    resp = [{"name": name, "gender": profiles[name]["gender"], "age": profiles[name]["age"]} for name in profiles]

    # Output as JSON
    return jsonify(resp)

@app.route('/bestmatch/<string:field>')
def viewBestMatch(field):

    # Return a JSON of an array of best matches based on field and profile's name

    resp = []

    # Retrieve name from GET parameters
    profile_name = request.args.get("current_profile", default="", type=str)

    if field == "country":
        # Retrieve best matches by country
        resp = [{"name": name, "gender": profiles[name]["gender"], "age": profiles[name]["age"]} for name in profiles]
    elif field == "likes":
        # Retrieve best matches by likes/dislikes
        resp = [{"name": name, "gender": profiles[name]["gender"], "age": profiles[name]["age"]} for name in profiles]
    elif field == "books":
        # Retrieve best matches by books
        resp = [{"name": name, "gender": profiles[name]["gender"], "age": profiles[name]["age"]} for name in profiles]
    elif field == "overall":
        # Retrieve best matches by overall information
        # resp = [{"name": name, "gender": profiles[name]["gender"], "age": profiles[name]["age"]} for name in profiles]
        resp = ronghao.viewMatchesOverall(profiles, profile_name)
    else:
        abort(404)
        return

    # Output as JSON
    return jsonify(resp)


@app.route('/piechart/<string:field>')
def plotPiechart(field):

    # Return a PNG of the plotted pie chart based on field

    # If unsupported field, return NOT FOUND
    if field not in piecharts:
        abort(404)
        return

    # Output as png file
    figure = piecharts[field]
    return Response(figure.getvalue(), mimetype='image/png')


if __name__ == "__main__":
    # Get directory of profiles
    directory = getfilepath.getFilePath()

    # If directory does not exist, exit the program
    if not isdir(directory):
        print "Invalid directory!"
        exit(0)
    print "Reading profiles from %s now..." % directory

    # Read the profiles and store in profiles dictionary
    profiles = getfilepath.getProfiles(directory)
    # For debugging purposes
    pretty_print(profiles)

    # Function 1,2,3 (Based on Project 1 Description.pdf)
    yongjie.viewProfiles(profiles)
    yongjie.viewMatchesCountry(profiles)
    yongjie.viewMatchesLikesDislikes(profiles)

    # Function 4
    # jiale.viewMatchesBooks(profiles)
    matches_books = jiale.getMatchesBooks(profiles)
    # Print top three for each person based on books
    for name in profiles:
        print "%s's top three based on books: %s" % (name, jiale.getTopThree(name, matches_books))

    # Function 6
    william.storeCSV()

    # Pre-compute all pie charts
    piecharts["likes"] = piechart.display_data_likes(profiles)
    piecharts["dislikes"] = piechart.display_data_dislikes(profiles)
    piecharts["country"] = piechart.display_data_nationality(profiles)
    piecharts["age"] = piechart.display_data_age(profiles)

    # Open function
    kijoon.openFunction(profiles)

    # Start Flask application on port 80 for loopback interface
    app.run(host="127.0.0.1", port=80, threaded=True)


