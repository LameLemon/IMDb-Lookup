#-------------------------------------------------------------------------------
# Name:        imdb-lookup-folder
# Purpose:
#
# Author:      manoj mj
#
# Created:
# Copyright:   (c) www.manojmj.com
# Licence:
#-------------------------------------------------------------------------------

import urllib2
import json
import webbrowser
import os
import collections
import sys

with open('config.json') as json_file:
    config = json.load(json_file)

data_dictionary = {}

import handlers

def finder(subdir):

    all_subdirs = [d for d in os.listdir(subdir)]

    for name in all_subdirs:
        datalist = []

        jsonvalues = handlers.getURL(name)

        # Assigns relevant tags to variables
        if jsonvalues["Response"]=="True":
            imdbrating = jsonvalues['imdbRating']
            imdburl = "http://www.imdb.com/title/"+jsonvalues['imdbID']
            imdbgenre = jsonvalues['Genre']
            imdbyear = jsonvalues['Year']
            imdbruntime = jsonvalues['Runtime']
            imdbactors = jsonvalues['Actors']
            imdbplot = jsonvalues['Plot']
            imdbplot = imdbplot.replace(',',' ')
            imdbawards = jsonvalues['Awards']
            imdbTitle = jsonvalues['Title']
        else:
            imdbTitle = name
            imdbrating = "Could not find"
            imdburl = "NA"
            imdbgenre = "NA"
            imdbyear = "NA"
            imdbruntime ="NA"
            imdbactors = "NA"
            imdbplot = "NA"
            imdbawards = "NA"

        datalist.append(imdbrating.encode('utf-8'))
        datalist.append(imdbgenre.encode('utf-8'))
        datalist.append(imdburl.encode('utf-8'))
        datalist.append(imdbyear.encode('utf-8'))
        datalist.append(imdbruntime.encode('utf-8'))
        datalist.append(imdbactors.encode('utf-8'))
        datalist.append(imdbplot.encode('utf-8'))
        datalist.append(imdbawards.encode('utf-8'))

        if imdbTitle not in  data_dictionary:
            data_dictionary[imdbTitle]=datalist

    sorted_dict = collections.OrderedDict(reversed(sorted(data_dictionary.items(),key=lambda t: t[1][0])))
    print('Creating moviefile.xls')
    if os.path.isfile("moviefile.xls"):
        os.remove("moviefile.xls")
    with open ("moviefile.xls","ab+") as data:
        #data.write("Movie Name\tRating\tGenre1\tGenre2\tGenre3\tUrl\tYear\tRuntime\tActor1\tActor2\tActor3\tActor4\tPlot\tAwards\n")
        data.write("Movie Name\tRating\tGenres\tUrl\tYear\tRuntime\tActors\tPlot\tAwards\n")
    for movie, [rating,genre,url,year,runtime,actors,plot,awards] in sorted_dict.iteritems():
        with open ("moviefile.xls","ab+") as data:
            data.write(str(movie)+"\t"+str(rating)+"\t"+str(genre)+"\t"+str(url)+"\t"+str(year)+"\t"+str(runtime)+
            "\t"+str(actors)+"\t"+str(plot)+"\t"+str(awards)+"\n")
    webbrowser.open("moviefile.xls")
    print('Done')

folder = sys.argv[1]
finder(folder)
