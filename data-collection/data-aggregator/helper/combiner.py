from helper.nlp import *

def combine(countries, wikipedia, imf):
    """
        input: cleaned data from dbpedia.countries, wikipedia and imf
        output: dictionary
            key = country anme
            value = dictionary representing combined cleaned data from all 3 sources
    """

    for feature in wikipedia:
        
        print("combining wikipedia feature with dbpedia countries:", feature["name"])
        data = feature["data"]

        for row in data:

            wiki_country = row["country"]

            best_match, score = match(wiki_country, countries)

            if score > 0.85:

                main = feature["main"]

                if type(main) == str:
                    countries[best_match][feature["name"].replace(" ", "_")] = row[main]

                elif type(main) == list:
                    for k in main:
                        k_cleaned = feature["name"] + k
                        k_cleaned = k_cleaned.replace(" ", "_")
                        countries[best_match][k_cleaned] = row[k]

    """
    insert code to combine imf data below
    """
    
    return countries
