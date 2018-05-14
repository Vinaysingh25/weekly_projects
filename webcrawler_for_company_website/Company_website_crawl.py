"""
Author: Vinayak Singh
Week: 6th - 12th May 2018
functionality: this the the updated one
"""

import re
import urllib.error

from bs4 import BeautifulSoup

master_list = []
starting_url = 'https://www.adobe.com'
master_list.append(starting_url)
while len(master_list) > 0:
    for url in master_list:

        try:
            html = urllib.request.urlopen(url).read()

        except print():
            print('something is wrong with URL')
            continue
        soup = BeautifulSoup(html, 'html.parser')

        listing = []
        tags = soup('a')
        for tag in tags:
            tagger = tag.get('href', None)
            listing.append(tagger)

        listing2 = []
        for item in listing:
            if item is not None and 'www' in item:
                if re.search('^//', item):
                    listing2.append(item[2:])
                else:
                    listing2.append(item)
                    print('new url added: ', item)

            if item not in master_list:
                master_list.append(item)

print(len(master_list))
