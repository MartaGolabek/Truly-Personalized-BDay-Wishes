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
    __website_address = "https://everydaypower.com/happy-birthday-quotes-for-a-friend/"
    r = requests.get(__website_address)

    doc = BeautifulSoup(r.text, "html.parser")

    raw_wishes = []
    for record in doc.find_all("p"):
        if re.match("\d+\.\s", record.text) is not None:
            temp_1 = re.sub(r"\d+\.", "", record.text)
            temp_2 = re.sub(r"\s\–\s.*", "", temp_1)[2:-1]
            raw_wishes.append(temp_2)

    with open("../../data/raw/bday_wishes_for_friend.csv", "w", newline="") as file:
        csv_writer = csv.writer(file, delimiter=";")
        for record in raw_wishes:
            print(record)
            csv_writer.writerow([record])
            # fix it
            # escape quotation marks
            # why is it get written into 3 columns instead of 1


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()