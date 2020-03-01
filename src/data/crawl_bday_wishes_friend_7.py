# -*- coding: utf-8 -*-
import logging
import requests
from bs4 import BeautifulSoup
import re
import csv

def main():
    """ Crawls a website, parse bday wishes and saves them to a file.
    """
    logger = logging.getLogger(__name__)
    logger.info('crawling and parsing a website')

    # crawl bday wishes for a friend
    __website_address = "https://www.wishesquotes.com/birthday/birthday-wishes"
    r = requests.get(__website_address)

    doc = BeautifulSoup(r.text, "html.parser")

    raw_wishes = []
    for record in doc.select("li"):
        if record.text and any(c.isalpha() for c in record.text):
            raw_wishes.append(record.text)

    print(len(raw_wishes))

    with open("../../data/raw/bday_wishes_for_friend_8.csv", "w", newline="") as file:
        csv_writer = csv.writer(file, delimiter=";")
        raw_wishes_extracted = raw_wishes[28:167]
        raw_wishes_extracted.insert(0, "text")
        for record in raw_wishes_extracted:
                print(record)
                csv_writer.writerow([record])


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()