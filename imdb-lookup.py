#-------------------------------------------------------------------------------
# Name:        imdb-lookup
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

import sys

import handlers

def finder(name):

    jsonvalues = handlers.getURL(name)

    #Opens the IMDb age using the JSON above
    if jsonvalues["Response"] == "True":
        imdbURL = "www.imdb.com/title/" + jsonvalues['imdbID']
        print('Opening new tab')
        webbrowser.open_new_tab(imdbURL)
        print('Opened')

file = sys.argv[1].split("\\")[-1]
finder(file)
