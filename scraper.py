from bs4 import BeautifulSoup

class KongkoScraper():
    def __init__(self, response):
        self.response = response

    def scrape(self):
        soup = BeautifulSoup(self.response, "html5lib")
        items = soup.find_all("div", {"class": "post-inner"})
        n = 1
        resources = []

        for item in items:
            html_categories = item.find("p", {"class": "post-category"}).find_all("a")
            categories = []

            for html_category in html_categories:
                categories.append(html_category.text)

            resources.append({
                "link": item.find("div", {"class": "post-thumbnail"}).find("a").get("href"),
                "title": item.find("div", {"class": "post-thumbnail"}).find("a").get("title"),
                "categories": ', '.join(categories),
                "date": item.find("p", {"class": "post-date"}).text,
                "content": item.find("div", {"class": "entry"}).text,
            })
            n=n+1
        return resources