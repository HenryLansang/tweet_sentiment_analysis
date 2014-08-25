#!/usr/bin/python
import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")

pyresponse = json.load(response)

print pyresponse.key;

# NOTE: this file use obselete API. it doesn't work. 
