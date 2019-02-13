
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
        result = ronghao.viewMatchesOverall(profiles, profile_name)

        result[0]["eventCategory"] = "Music"
        result[1]["eventCategory"] = "Business"
        result[2]["eventCategory"] = "Food"

        result[0]["listOfEvents"] = [
            {"name": "FREE ADMISSION SATURDAY NIGHT PARTY  | THE VNYL  VINTAGE LIFESTYLE",
             "url": "https://www.eventbrite.com/e/free-admission-saturday-night-party-the-vnyl-vintage-lifestyle-tickets-17434703668?aff=ebapi"},
            {"name": "Big Tigger Hosts Suite Life Fridays At Suite Lounge - RSVP HERE",
             "url": "https://www.eventbrite.com/e/big-tigger-hosts-suite-life-fridays-at-suite-lounge-rsvp-here-tickets-53667810867?aff=ebapi"},
            {"name": "Suite Life Fridays Hosted By Big Tigger At Suite Lounge - RSVP HERE",
             "url": "https://www.eventbrite.com/e/suite-life-fridays-hosted-by-big-tigger-at-suite-lounge-rsvp-here-tickets-22601901897?aff=ebapi"},
            {"name": "ATLANTA'S NEWEST CLUB - REVEL OF WEST MIDTOWN",
             "url": "https://www.eventbrite.com/e/atlantas-newest-club-revel-of-west-midtown-tickets-34595163064?aff=ebapi"},
            {"name": "9th Annual Atlanta Hip Hop Day Festival",
             "url": "https://www.eventbrite.com/e/9th-annual-atlanta-hip-hop-day-festival-tickets-1880852681?aff=ebapi"}
        ]
        result[1]["listOfEvents"] = [
            {"name": "8th Philippine SME Business Expo & Conference 2019",
             "url": "https://www.eventbrite.com/e/8th-philippine-sme-business-expo-conference-2019-tickets-26676413872?aff=ebapi"},
            {"name": "RISE Weekend Dallas - July 18-20, 2019",
             "url": "https://www.eventbrite.com/e/rise-weekend-dallas-july-18-20-2019-tickets-54883442855?aff=ebapi"},
            {"name": "DrinkEntrepreneurs x Elbow Room by Drinks & Co 20 Feb",
             "url": "https://www.eventbrite.com/e/drinkentrepreneurs-x-elbow-room-by-drinks-co-20-feb-tickets-5339893766?aff=ebapi"},
            {"name": "6th Entrepreneur and Franchise Expo 2019",
             "url": "https://www.eventbrite.com/e/6th-entrepreneur-and-franchise-expo-2019-tickets-37795845391?aff=ebapi"},
            {"name": "INTERNET WORLD EXPO 2019 \u2013 the commerce e-xperience",
             "url": "https://www.eventbrite.de/e/internet-world-expo-2019-the-commerce-e-xperience-tickets-43928336838?aff=ebapi"}
        ]
        result[2]["listOfEvents"] = [
            {"name": "Chicago Food Truck Festival (Summer 2019)",
             "url": "https://www.eventbrite.com/e/chicago-food-truck-festival-summer-2019-tickets-54158401236?aff=ebapi"},
            {"name": "HENNY&WAFFLES CHARLOTTE | ALL STAR WEEKEND | FEB 17 | OAK ROOM",
             "url": "https://www.eventbrite.com/e/hennywaffles-charlotte-all-star-weekend-feb-17-oak-room-tickets-52417953510?aff=ebapi"},
            {"name": "Heights Crawfish Festival - OFFICAL",
             "url": "https://www.eventbrite.com/e/heights-crawfish-festival-offical-tickets-52206929331?aff=ebapi"},
            {"name": "Food & Wine Experience",
             "url": "https://www.eventbrite.com/e/food-wine-experience-tickets-44432192885?aff=ebapi"},
            {"name": "Black Food Truck Fridays (Special Edition)",
             "url": "https://www.eventbrite.com/e/black-food-truck-fridays-special-edition-tickets-54689941086?aff=ebapi"}
        ]

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

    resp = yongjie.view_profiles(profiles)

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

