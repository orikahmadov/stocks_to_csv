import requests, os
from  bs4 import BeautifulSoup
import smtplib


request =  requests.get("https://www.investing.com/equities/", headers={"User-Agent": "Mozilla/5"})
soup = BeautifulSoup(request.text, features="lxml")
table_stock =  soup.find("table", id="cross_rate_markets_stocks_1")
headers = [" ".join(x.text.split()) for x in table_stock.find_all("th") ]
stock_information = ["".join(x.text) for x in table_stock.find_all("td") if x != ""]
filtered_header =  [a for a in headers if a != "\xa0" if a != ""]
filtered_stock_information = [b for b in stock_information if b != "\xa0"]
new_list = []
for index in range(0, len(filtered_stock_information), 8):
    new_list.append(filtered_stock_information[index : index + 8])
with open("stock_prices.csv", "w", encoding="UTF-8") as f:
    for i in filtered_header:
        f.write(f"{i},")
    for a in new_list:
        f.write("\n")
        f.write(f"{','.join(a)}")





