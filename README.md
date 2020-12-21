# TAC

Course material for "Traitement automatique de corpus" (STIC-B545) taught at [ULB](https://ulb.be)

Caution: Python 3.6 or higher required to handle [f-strings](https://www.python.org/dev/peps/pep-0498/) (3.7 or 3.8 is better)

It is recommended to run this code in a virtual environment:

```bash
git clone git@github.com:madewild/tac.git
cd tac
pip install virtualenv
virtualenv venv --python=python3
source venv/bin/activate
which pip
```

Then install Python dependencies with `pip install -r requirements.txt`

You can use either the scripts (\*.py) or the Jypyter Notebooks (\*.ipynb)

I decided to add my part for the final paper below the module because it is useful to keep parts about modules (made by the teacher).

## Module 1

`s1_sql.py`: querying a simple relational database

`s2_sparql.py`: querying the Wikidata SPARQL endpoint

`s3_api.py`: playing with OpenStreetMap and EUcountries APIs

`s4_scrape.py`: scraping the AVB to retrieve 2833 PDF bulletins

## Module 2

`s1_convert.sh`: bash script to convert PDFs to TXTs, move them to dedicated folder and aggregate them in single big text file

`s2_explore.py`: playing with various categories (city, year, decade, type...)

`s3_freq.py`: basic frenquency analysis, hapaxes, long words...

## Module 3

### Keyword extraction

`s1_keywordse.py`: using YAKE to extract French keywords in each text file

Librairies : yake

`s2_wordcloud.sh`: generating a wordcloud for a given year (calling `filtering.py` in the background)

### Named-entity recognition

Install SpaCy from requirements then run this command to download French model: `python -m spacy download fr_core_news_sm`

`s3_ner.py`: perform NER with SpaCy FR model

### Sentiment analysis

`s4_sentiment.py`: analyse positive/negative sentences with textblob

## Module 4

`classification.py`: supervised classification of 20 newsgroups

`clustering.py`: unsupervised clustering with k-means

`sentence_tokenizer.py`: split big text into sentences

`model_builder.py`: train word2vec model on corpus

`model_explorer.py`: explore similarity between vectors

## Module 5

`language_detection`: language identification with langid

`anonymization.py`: de-identification of data with Faker

## Module 6

`extraction.py`: extract text from various file types

`htr.sh`: script for handwritten text recognition

## Rapport

To install librairies, tape `pip install` and name of the library

`main.py` : to launch codes from scrape.py to wordcloude.sh ; library : os

`scrape.py`: scraping the AVB to retrieve 2833 PDF bulletins ; library : requests

`s1_convert.sh`: bash script to convert PDFs to TXTs, move them to dedicated folder and aggregate them in single big text file

`s3_freq.py`: frenquency analysis, hapaxes, long words and keywords analysis from a chosen list 

`s1_keywordse.py`: using YAKE to extract French keywords from a chosen list ; library : yake

`s2_wordcloude.sh`: generating a wordcloud for a given year (calling `filteringe.py` in the background) ; libraries : wordcloud_cli, nltk

`s4_sentiment.py`: analyse positive/negative sentences with textblob ; libraries : textblob, textblob_fr

`sentence_tokenizer.py`: split big text into sentences

`model_buildere.py`: train word2vec model on corpus. Librairies : gensim

`model_explo.py`: explore similarity between vectors

`detection_lan` language identification with langid ; libraries : pycountry, langid


