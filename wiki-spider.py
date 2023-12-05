import requests
from bs4 import BeautifulSoup
import random


def wikiScraper(url):
    # set "response" to the return value of calling the get method of requests on the desired url
    # "response" is set to a class with a "content" method
    response = requests.get(
        url=url,
    )
    # set "soup" to the result of calling BeautifulSoup on the content of "response" using the 'html.parser' type
    # "soup" is set to a class with a "find" method
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")
    print(title.text)

    # get every anchor tag and shuffle them
    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        # verify that link is another wikipedia article
        if link['href'].find("/wiki/") == -1:
            continue

        linkToScrape = link
        break

    wikiScraper("https://wikipedia.org" + linkToScrape['href'])


wikiScraper("https://en.wikipedia.org/wiki/Web_scraping")
