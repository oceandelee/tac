"""Testing keyword extraction with YAKE"""

import os, sys
import yake

def searchKeywords(startString, keywordSearch, language, topNumber):

    ignored = set(["conseil communal", "conseil général"])
    kw_extractor = yake.KeywordExtractor(lan=language, top=topNumber)

    data_path = os.path.dirname(os.path.abspath(__file__))+ f"\\..\\rapport\\data\\txt\\"
    files = os.listdir(data_path)

    kwResult = []
    for f in sorted(files):
        if f.startswith(startString):
            print("try open" + f)
            text = open(data_path + f, encoding="latin-1").read()
            try:
                keywords = kw_extractor.extract_keywords(text)
                kept = []
                for score, kw in keywords:
                    words = kw.split()
                    if len(words) > 0 and kw not in ignored:
                        kept.append(kw)
                for k in kept:
                    for w in keywordSearch:
                        print(k + " - " + w)
                        if k.find(w) > -1:
                            kwResult.append(f)
                            print("add "+ f)
            except Exception as ex:
                print("Impossible to extract keyword in " + f + " file:")
                print(ex)
                pass
            #print(f"{f} mentions these keywords: {', '.join(kept)}...")
    
    print(len(kwResult))
    return kwResult
