from copy import deepcopy
from helper.nlp import *

def combine(dbpedia, wikipedia, imf):
    """
    input:
        dbpedia - dict representing country data from dbpedia
            {
                country1: data1,
                country2: data2
            }

        wikipedia - list of dicts representing table data from wikipedia
            [
                {table1 data},
                {table2 data}
            ]

        imf - dict representing country data from imf
            {
                country1: data1,
                country2: data2
            }
    """

    def get_dbpedia_imf_mappings(dbpedia, imf, threshold=0.85):
        """
        output: dict containing dbpedia-imf country mappings
            - country names are inconsistent in both dictionaries
            - pick only those who score > threshold
            - so that everything in final output will have data from both dbpedia and imf
        """
        out = {}
        for country in dbpedia:
            best_match, score = match(country, imf)

            if score > 0.85:
                out[country] = best_match
 
        return out

    dbpedia_imf_mappings = get_dbpedia_imf_mappings(dbpedia, imf)

    aggregate = {k:v for k,v in dbpedia.items() if k in dbpedia_imf_mappings}
    embeddings = deepcopy(aggregate)


    # combining both aggregate and embeddings with wikipedia data
    for feature in wikipedia:

        print("Combining with wikipedia tables:", feature["name"])
        data = feature["data"]

        for row in data:
            
            wiki_country = row["country"]
            best_match, score = match(wiki_country, dbpedia_imf_mappings)
            
            if score > 0.85:
                
                # inserting wiki data into aggregate
                aggregate[best_match][feature["name"]] = row

                # inserting wiki data into embeddings
                main = feature["main"]
                if type(main) == str:
                    embeddings[best_match][feature["name"].replace(" ", "_")] = row[main]

                elif type(main) == list:
                    for k in main:
                        k_cleaned = feature["name"] + "_" + k
                        k_cleaned = k_cleaned.replace(" ", "_")
                        embeddings[best_match][k_cleaned] = row[k]

    for country, imf_country in dbpedia_imf_mappings.items():

        for imf_key, imf_value in imf[imf_country].items():
            
            # inserting imf data into aggregate
            aggregate[country][imf_key] = imf_value

            # inserting imf data into embeddings
            latest = sorted([(k,v) for k,v in imf_value.items()], key=lambda x:x[0])[-1][-1]
            try: latest = float(latest)
            except: pass

            embeddings[country][imf_key] = latest

    return aggregate, embeddings







    