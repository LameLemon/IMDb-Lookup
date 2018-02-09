import urllib2
import json

with open('config.json') as json_file:
    config = json.load(json_file)

API_KEY = config["api_key"]

#Loads keywords.txt into list content
def loadWords():
    with open('keywords.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def getURL(fname):
    replace = loadWords()

    #Gets year is present in fname
    year=0
    for y in range(1900,2099):
        if str(y) in fname:
            fname = fname.replace(str(y)," ")
            year = y
            break
    for value in replace:
        fname = fname.replace(value," ")

    #Removes new line characters and adds ''+' for spaces
    fname = fname.strip();
    fname = fname.replace(" ", "+")

    #Creates url
    if year!=0:
        url = "http://www.omdbapi.com/?apikey="+API_KEY+"&t="+fname+"&y="+str(year)
    else:
        url = "http://www.omdbapi.com/?apikey="+API_KEY+"&t="+fname

    #Gets JSON response
    response = urllib2.urlopen(url).read()
    jsonvalues = json.loads(response)

    return jsonvalues
