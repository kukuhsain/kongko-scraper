import requests
from scraper import KongkoScraper

if __name__ == "__main__":
    url = "http://kongko.co"
    response = requests.get(url)
    resources = KongkoScraper(response.content)
    scraped_resources = resources.scrape()
    num = 1
    for res in scraped_resources:
        print(num)
        print(res["title"])
        print(res["link"])
        print(res["date"])
        print(res["categories"])
        print(res["content"])
        num = num+1
