import requests
from bs4 import BeautifulSoup
import time
from win11toast import toast
from datetime import datetime, timedelta


# Check if keyword exists in the first page of the url
def check_keyword(url, keyword):
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    for li in soup.select("div.news_board ul li"):
        a_text = li.find("a").text if li.find("a") else ""
        if keyword in a_text:
            return True  # Return True if keyword found
    return False  # Return False if no matching keyword found


# Send alarm to Windows 11's notification center
def send_notification(message):
    toast(
        "Keyword Found",
        message,
        on_click="https://maplestory.nexon.com/News/Notice/Notice",
    )


url = "https://maplestory.nexon.com/News/Notice/Notice"
keyword = "리부트"

# Message to be sent to Windows 11's notification center
while True:
    if check_keyword(url, keyword):
        send_notification("리부트 공지가 있습니다!")
        print("Keyword found from the first page. See url.")
        break
    else:
        send_notification("리부트 공지는 안 보입니다.")
        print("Keyword not found from the first page. See url.")
    time.sleep(86400)
