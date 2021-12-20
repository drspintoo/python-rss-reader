
import html

from datetime import datetime, timedelta

 

import requests

from bs4 import BeautifulSoup

 

today = datetime.now()

thirty_days_ago = today - timedelta(days=30)

 

url = requests.get(

    'https://feeds.highgearmedia.com/?sites=GreenCarReports&tags=news')

 

readerSoup = BeautifulSoup(url.content, 'xml')

items = readerSoup.find_all('item')

separator = "-" * 80

 

for item in items:

    title = item.title.text

    description = item.description.text

    link = item.link.text

    pubDate = item.pubDate.text

    dtobj = datetime.strptime(pubDate, '%a, %d %b %Y %X %z')

    by = item.find("dc:creator").text

 

    if 'rivian' not in description.lower() and 'rivian' not in title.lower():

        continue

    if thirty_days_ago <= dtobj.replace(tzinfo=None):

        print(

            f"\n{pubDate}\nTitle: {title}\nBy: {by}\n\nDescription: {html.unescape(description.split('/>')[1])}\n\nLink: {link}\n\n{separator}\n")

 

 

