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
    __website_address = "https://happybirthdaywishesworld.com/happy-birthday-best-friend/"
    r = requests.get(__website_address)

    doc = BeautifulSoup(r.text, "html.parser")

    raw_wishes = ["text"]
    for record in doc.select("div.entry-content p"):
        if re.match("\d+\.\s", record.text) is not None:
            temp_1 = re.sub(r"\d+\.", "", record.text).strip()
            raw_wishes.append(temp_1)

    with open("../../data/raw/bday_wishes_for_friend_5.csv", "w", newline="") as file:
        csv_writer = csv.writer(file, delimiter=";")
        for record in raw_wishes:
            print(record)
            csv_writer.writerow([record])


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()