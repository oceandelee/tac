"""Query Wikidata for people born in Brussels who received an award"""

import argparse
from datetime import datetime as dt

from SPARQLWrapper import SPARQLWrapper, JSON

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filter', type=str, help='Filtering on name')
parser.add_argument('-n', '--number', type=int, help='Number of rows to display')

def get_rows():
    """Retrieve results from SPARQL"""
    endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
    sparql = SPARQLWrapper(endpoint,agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11")

    statement = """
   SELECT DISTINCT ?person ?personLabel ?award ?awardLabel WHERE {
        ?person wdt:P19 wd:Q239 .                                                         #Person born in Brussels
        ?person wdt:P166 ?award                                                           #Person who won an award
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en, fr, nl, de" .}    #In any language
    }
    order by ?personLabel
    """

    sparql.setQuery(statement)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    rows = results['results']['bindings']
    print(f"\n{len(rows)} awarded people found\n")
    return rows

def show(rows, name_filter=None, n=10):
    """Display n people (default=10)"""
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    if name_filter:
        rows = [row for row in rows if name_filter in row['personLabel']['value'].lower()]
    print(f"Displaying the first {n}:\n")
    for row in rows[:n]:
        try:
            award_label = row["awardLabel"]["value"]
        except ValueError:
            award_label = "????"
        print(f"{row['personLabel']['value']} - {award_label}")

if __name__ == "__main__":
    args = parser.parse_args()
    my_rows = get_rows()
    my_filter = args.filter if args.filter else None
    number = args.number if args.number else 10
    show(my_rows, my_filter, number)



