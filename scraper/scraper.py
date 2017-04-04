#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# imports
from bs4 import BeautifulSoup
import requests
from operator import itemgetter

# this function returns a soup page object
def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, "lxml")
    return spobj

# scraper website: heise.de
def main():

    d = {}   # create a dictionary

    for page in range(1,5,1):

        # all https topics
        heise_https_url = "https://www.heise.de/thema/https?seite=" + str(page)

        # https topics
        content = getPage(heise_https_url).find("div", {"class":"keywordliste"})
        content = content.findAll("header")

        # split wordlist into words
        for line in content:
            linetxt = line.text.encode('utf-8')
            wordlist = linetxt.split()

            # store all words with appearances in dictionary
            for word in wordlist:
                if not d.has_key(word):
                    d[word] = 1
                if d.has_key(word):
                    d[word] = d[word]+1

    print("\nDONE !\n\nTopic https on heise.de was scraped completely.\n")

    # print top 3 words of dictionary
    sorted(d.items(), key=itemgetter(1), reverse=True)
    print(map(itemgetter(0), sorted(d.items(), key=itemgetter(1), reverse=True))[9])


# main program
if __name__ == '__main__':
    main()
