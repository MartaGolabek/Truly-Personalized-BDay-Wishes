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
    __website_address = "https://www.yellowoctopus.com.au/pages/happy-birthday-messages#happy%20birthday%20messages%20for%20friends"
    r = requests.get(__website_address)

    doc = BeautifulSoup(r.text, "html.parser")

    raw_wishes = ["text"]
    for record in doc.select("p"):
        if re.match("\d+\.", record.text) is None:
            raw_wishes.append(record.text)

    print(len(raw_wishes))

    with open("../../data/raw/bday_wishes_for_friend_6.csv", "w", newline="") as file:
        csv_writer = csv.writer(file, delimiter=";")

        # It was difficult to extract "clean" bday wishes from the rest of records
        # so I have only used the first 698 records
        for record in raw_wishes[0:698]:
            if record and any(c.isalpha() for c in record):
                print(record)
                csv_writer.writerow([record])


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()