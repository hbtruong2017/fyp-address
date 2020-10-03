"""
this file generates constants that need to be generated and pickle stores them
"""
import pandas as pd

from helpers.common import *
from mongodb_helper import *

def generate_constants():

    print("generating constants", end=" ")

    db = get_database()
    countries_collection = db["test.aggregate.countries"]

    data = pd.read_csv("scripts/files/countries.csv", delimiter="\t")

    d = {}

    for code, lat, lon, cname in data.values:
        d[cname] = (lat, lon, code)

    countries = {}
    for i in countries_collection.find():
        
        cname = i["_id"]

        if cname not in d:
            print("country from database", cname, "not in csv file - pls check")
            continue
    
        lat, lon, code = d[cname]
        code = str(code)

        countries[cname] = {
            "lat": float(lat),
            "lon": float(lon),
            "code": code,
            "flag": f"https://www.countryflags.io/{code}/flat/64.png"
        }

    pickle.dump(countries, open("pickled/all_countries.sav", "wb"))

    print("- finished")