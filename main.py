from bs4 import BeautifulSoup
import requests
import math
from csv import writer
import time
import json
def findCourses(search):
    with open(f"android.csv",'w',encoding="utf-8") as new: 
        wr=writer(new)
        head=["Serial_Number","name","rating","price","provider_name","price_currency","level","pace","audio","subtitles","details_path"]
        wr.writerow(head)
        html_text1=requests.get(f'https://classpert.com/search.json?p=1&q={search}').text
        a1=json.loads(html_text1)
        pages=(a1["meta"]["pages"])
        total=(a1["meta"]["total"])
        print(f"total results found: {total} in {pages} pages")
        print("extracting top 20 results:")
        c=0
        for _ in range(1,3):
            print("Page",_)    
            html_text1=requests.get(f'https://classpert.com/search.json?p={_}&q={search}').text
            a=json.loads(html_text1)
            b=(a["data"])
            for i in range (10):
                c+=1
                s=[c,(b[i]["name"]),(b[i]["rating"]),(b[i]["price"]),(b[i]["provider_name"]),(b[i]["price_currency"]),(b[i]["level"]),(b[i]["pace"]),(b[i]["audio"]),(b[i]["subtitles"]),"https://classpert.com"+(b[i]["details_path"])]
                wr.writerow(s)
        print(f"Table {search} has been updated")
findCourses(input("Course:\n"))