from fileparser import pretty_print
import getfilepath
import piechart

from os.path import isdir
from sys import exit
from flask import Flask, jsonify, Response, request, abort
from flask_cors import CORS
from io import BytesIO

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
    profile_name = request.args.get("name", default="", type=str)

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
        resp = [{"name": name, "gender": profiles[name]["gender"], "age": profiles[name]["age"]} for name in profiles]
    else:
        abort(404)
        return

    # Output as JSON
    return jsonify(resp)


@app.route('/piechart/<string:field>')
def plotPiechart(field):

    # Return a PNG of the plotted pie chart based on field

    plt = None
    if field == "likes":
        # Plot based on likes
        plt = piechart.display_data_likes(profiles)
    elif field == "dislikes":
        # Plot based on dislikes
        plt = piechart.display_data_dislikes(profiles)
    elif field == "age":
        # Plot based on age
        plt = piechart.display_data_age(profiles)
    elif field == "country":
        # Plot based country
        plt = piechart.display_data_nationality(profiles)
    else:
        abort(404)
        return

    # Save pie chart in png format
    figure = BytesIO()
    plt.savefig(figure, format="png", bbox_inches="tight")
    plt.clf()
    figure.seek(0)

    # Output as png file
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
    jiale.viewMatchesBooks(profiles)

    # Function 5
    ronghao.viewMatchesOverall(profiles)

    # Function 6
    william.storeCSV()

    # Open function
    kijoon.openFunction(profiles)

    # Start Flask application on port 80 for loopback interface
    app.run("127.0.0.1", 80, False)


