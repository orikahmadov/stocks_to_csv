import requests, os
from  bs4 import BeautifulSoup
import smtplib


request =  requests.get("https://www.investing.com/equities/", headers={"User-Agent": "Mozilla/5"})   #Request to investing.com with headers
soup = BeautifulSoup(request.text, features="lxml")                                                   #Soup Object for traversing HtMl
table_stock =  soup.find("table", id="cross_rate_markets_stocks_1")                                   #Selecting Table
headers = [" ".join(x.text.split()) for x in table_stock.find_all("th") ]                             #creating Headers for csv
stock_information = ["".join(x.text) for x in table_stock.find_all("td") if x != ""]                  #getting all stock prices
filtered_header =  [a for a in headers if a != "\xa0" if a != ""]                                     #filtering the headers
filtered_stock_information = [b for b in stock_information if b != "\xa0"]                            #filtering stock prices
new_list = []                                               
for index in range(0, len(filtered_stock_information), 8):                                            #spliting the list by 8 
    new_list.append(filtered_stock_information[index : index + 8])
with open("stock_prices.csv", "w", encoding="UTF-8") as f:                                            #writing it to a file
    for i in filtered_header:               
        f.write(f"{i},")
    for a in new_list:
        f.write("\n")
        f.write(f"{','.join(a)}")





