import lxml
import requests
import smtplib
from bs4 import BeautifulSoup

product_url = "https://www.amazon.in/ASUS-ZenBook-Ultra-Slim-Laptop/dp/B07QWLXCC7/ref=sr_1_13?dchild=1&qid=1619619394&refinements=p_n_feature_three_browse-bin%3A1464435031%2Cp_72%3A1318476031&rnid=1318475031&s=computers&sr=1-13"
header = {
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
  "Accept-Language":"en-US,en;q=0.5"
}
response = requests.get(url = product_url, headers = header)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(name = "span", id = "priceblock_ourprice").get_text()
title = soup.find(name = "span", id = "productTitle").get_text().strip()
price_without_currency = price.split()[1].replace(",","")
price_as_float = float(price_without_currency)
print(f"Product: {title}\nPrice: {price_as_float}")

BUY_PRICE = 200000

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=OTHER_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{product_url}"
        )