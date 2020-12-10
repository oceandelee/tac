<<<<<<< HEAD
"""API for AVB"""

import json
import sys

import requests



def actualite_found ():
    osm = "https://opendata.bruxelles.be/api/datasets/1.0/search/?q="
    data = {

    "nhits":0,
    "parameters":{
        "dataset":"actualites-ville-de-bruxelles",
        "timezone":"UTC",
        "q":"actualite",
        "language": "fr",
        "rows":10,
        "start":0,
        "sort":[
            "published"
        ]
        ,
        "format":"json"
    }
    ,
    "records":[]
    }
    resp = requests.get(osm, data)
    if resp.status_code == 200:
        print(resp.json()["datasets"][0]["metas"])
    else:
        print("actualite not found")
    return resp

def get_result(resp,n,attribut):
    metas = resp.json()["datasets"][n]["metas"]
    return metas[attribut]



def nb_result(resp):
    return len(resp.json()["datasets"])

#Example of use
if __name__ == "__main__":
    resp = actualite_found()
    result = get_result(resp,2,"description")
    print(result)
=======
"""API for AVB"""

import json
import sys

import requests



def actualite_found ():
    osm = "https://opendata.bruxelles.be/api/datasets/1.0/search/?q="
    data = {

    "nhits":0,
    "parameters":{
        "dataset":"actualites-ville-de-bruxelles",
        "timezone":"UTC",
        "q":"actualite",
        "language": "fr",
        "rows":10,
        "start":0,
        "sort":[
            "published"
        ]
        ,
        "format":"json"
    }
    ,
    "records":[]
    }
    resp = requests.get(osm, data)
    if resp.status_code == 200:
        print(resp.json()["datasets"][0]["metas"])
    else:
        print("actualite not found")
    return resp

def get_result(resp,n,attribut):
    metas = resp.json()["datasets"][n]["metas"]
    return metas[attribut]



def nb_result(resp):
    return len(resp.json()["datasets"])

#Example of use
if __name__ == "__main__":
    resp = actualite_found()
    result = get_result(resp,2,"description")
    print(result)
>>>>>>> 52fcf1c237ca3b8de5976e083487c759cfee2d8f
    print(nb_result(resp))