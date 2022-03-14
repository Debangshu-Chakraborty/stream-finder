# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:37:29 2022

@author: debangshu
"""

import requests
from bs4 import BeautifulSoup

# title="the-conjuring"

def format_title(title):
    title=title.lower()
    title_tokens=title.split(' ')
    title='-'.join(title_tokens)
    return title
    
    
def find_movie(title):
    try:
        title=format_title(title)
        url="https://www.justwatch.com/in/movie/"+title
        r = requests.get(url, allow_redirects=True)
        soup=BeautifulSoup(r.content,'html.parser')
        platforms_list=soup.find("div",{"class":"price-comparison__grid__row price-comparison__grid__row--stream"})
        # platforms_list=soup.find("div",{"class":"price-comparison__grid__row__holder"})
        # print(platforms_list)
        children=platforms_list.findChildren()
        platforms=[]
        for child in children:
            platforms.append(str(child))
        
        streams=[]
        for platform in platforms:
            if platform.find('class="price-comparison__grid__row__icon"') and platform[0:4]=="<img":
                stream=platform[10:]
                end=stream.find("\"")
                stream=stream[:end]
                streams.append(stream)
        #No streaming services found
        if len(streams)==0:
            return False
        return streams
    except:
        return "Unable to fetch info"

def find_tvseries(title):
    try:
        title=format_title(title)
        url="https://www.justwatch.com/in/tv-show/"+title
        r = requests.get(url, allow_redirects=True)
        soup=BeautifulSoup(r.content,'html.parser')
        platforms_list=soup.find("div",{"class":"price-comparison__grid__row price-comparison__grid__row--stream"})
        # platforms_list=soup.find("div",{"class":"price-comparison__grid__row__holder"})
        # print(platforms_list)
        children=platforms_list.findChildren()
        platforms=[]
        for child in children:
            platforms.append(str(child))
        
        streams=[]
        for platform in platforms:
            if platform.find('class="price-comparison__grid__row__icon"') and platform[0:4]=="<img":
                stream=platform[10:]
                end=stream.find("\"")
                stream=stream[:end]
                streams.append(stream)
        #No streaming services found
        if len(streams)==0:
            return False
        return streams
    except:
        return "Unable to fetch info"
                
    

    