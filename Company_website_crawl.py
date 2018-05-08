'''
Author: Vinayak Singh
Week: 6-12th May 2018
Functionality: This base crawler can crawl your company website and prove you all the other pages releated to these pages
                This is a base exercise you can crawl all the linked the pages and later do further activites like auto webpage tagging
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

master_list = []
starting_url = 'https://www.adobe.com'
master_list.append(starting_url)
while len(master_list) > 0:
    for url in master_list:
        #url = input('Enter -')
        try:
            html = urllib.request.urlopen(url).read()

        except:
            print('something is wrong with URL')
            continue
        soup = BeautifulSoup(html, 'html.parser')

        ## Retrieve all the anchor tags

        listing = []
        tags = soup('a')
        for tag in tags:
            tagger = tag.get('href', None)
            listing.append(tagger)

        #print(listing)

        listing2 = []
        for list in listing:
            if list is not None and 'www' in list:
                if re.search('^//', list):
                    listing2.append(list[2:])
                else:
                    listing2.append(list)
                    print('new url added: ', list)

            if list not in master_list:
                master_list.append(list)

print(len(master_list))





