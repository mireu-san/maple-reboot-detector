import requests
from bs4 import BeautifulSoup
import time
from win11toast import toast


class KeywordChecker:
    def __init__(self, url, keyword):
        self.url = url
        self.keyword = keyword

    # Method to check for keyword in the provided URL
    def check_keyword(self):
        response = requests.get(self.url)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")
        for li in soup.select("div.news_board ul li"):
            a_text = li.find("a").text if li.find("a") else ""
            if self.keyword in a_text:
                return True
        return False

    # Method to check for keyword in the provided URL
    def send_notification(self, message):
        toast(
            "Keyword Found",
            message,
            on_click="https://maplestory.nexon.com/News/Notice/Notice",
        )


if __name__ == "__main__":
    url = "https://maplestory.nexon.com/News/Notice/Notice"
    keyword = "리부트"
    checker = KeywordChecker(url, keyword)

    # Infinite loop to keep checking for the keyword at the specified URL
    while True:
        if checker.check_keyword():
            checker.send_notification("리부트 공지가 있습니다!")
            print("Keyword found from the first page. See url.")
            break
        else:
            checker.send_notification("리부트 공지는 안 보입니다.")
            print("Keyword not found from the first page. See url.")
        time.sleep(14400)  # Set as 4hrs to avoid spamming the target url.
