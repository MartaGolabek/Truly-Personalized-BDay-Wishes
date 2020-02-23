import scrapy
import csv

class BdayWishesFriendSpider(scrapy.Spider):
    name = "bday_wishes_friend"
    start_urls = ["https://therightmessages.com/short-and-long-birthday-wishes-for-best-friend/"]

    def parse(self, response):
        set_selector = 'p::text'

        raw_wishes = ["text"]
        for record in response.css(set_selector):
            print(record.get())
            raw_wishes.append(record.get())

        raw_wishes = raw_wishes[:-23]

        filename = "../../data/raw/bday_wishes_for_friend_2.csv"
        with open(filename, "w", newline="") as file:
            csv_writer = csv.writer(file, delimiter=";")
            for record in raw_wishes:
                csv_writer.writerow([record])
        self.log('Saved file %s' % filename)