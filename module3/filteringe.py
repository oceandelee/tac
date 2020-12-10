"""Filter out stopwords for word cloud"""

import sys
import nltk
from nltk.corpus import stopwords

sw = stopwords.words("french")
sw += ["les", "plus", "cette", "fait", "faire", "être", "deux", "comme", "dont", "tout",
       "ils", "bien", "sans", "peut", "tous", "après", "ainsi", "donc", "cet", "sous",
       "celle", "entre", "encore", "toutes", "pendant", "moins", "dire", "cela", "non",
       "faut", "trois", "aussi", "dit", "avoir", "doit", "contre", "depuis", "autres",
       "van", "het", "autre", "jusqu", "faite", "messieurs", "elles", "celui", "habitant",
        "toute", "avant", "car", "leurs", "pourrait", "cependant", "aucun", "ceux", "aujourd'hui",
        "chaque", "alors", "ville", "conseil", "conseil communal", "très", "seulement",
        "mois", "habitants", "enfin", "quatre", "beaucoup", "plusieurs", "également",
        "aujourd hui", "tandis", "grand", "dernier", "sieur", "dessus", "sieur", "rien",
        "toujours", "assez", "tant", "peuvent", "pourra", "établi", "quand", "etc", "déjà", 
        "aucune", "celles", "trouve", "laquelle", "rien", "crois", "chose", "agit", "mêmes", 
        "parce", "mis", "seule", "devant", "personne", "peu", "tel", "ans", "jamais", "voici", "aujourd",
        "hui", "autant", "première", "bourgmestre", "échevins", "trouvés", "ici", "lorsqu", "trop",
        "ailleurs", "donne", "grande", "telle", "quant", "quelque", "communal", "seul", "personnes",
        "doivent", "delà", "bruxelles", "faites", "présente", "premier", "existe", "quelques", "administration communale",
        "chez", "rue", "rues", "administration", "communale", "franc", "francs", "vers", "propose", "compris", "cinq", "six",
        "donné", "année", "soumis", "procès verbal", "mai", "octobre", "devons", "collège", "commune", "honorable",
        "rapport", "nouveau", "présenté", "chargé", "bon", "bonne", "lorsque"]
sw = set(sw)


def filtering(year):
    path = f"{year}.txt"
    output = open(f"{year}_keywords.txt", "w", encoding="utf-8")

    with open(path) as f:
        text = f.read()
        words = nltk.wordpunct_tokenize(text)
        kept = [w.lower() for w in words if len(
            w) > 2 and w.isalpha() and w.lower() not in sw]
        kept_string = " ".join(kept)
        output.write(kept_string)


if __name__ == '__main__':
    year = sys.argv[1]
    print(year)
    filtering(year)
