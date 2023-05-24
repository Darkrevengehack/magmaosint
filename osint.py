#!/usr/bin/env python3
# coding: utf-8

import requests
from fuzzywuzzy import fuzz
from googlesearch import search
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init

# colorama
init(autoreset=True)

# Logo
print(Fore.YELLOW + '''
  █▀▄▀█ █▀▀█ █▀▀▀ █▀▄▀█ █▀▀█   █▀▀█ █▀▀ ░▀░ █▀▀▄ ▀▀█▀▀
  █░▀░█ █▄▄█ █░▀█ █░▀░█ █▄▄█   █░░█ ▀▀█ ▀█▀ █░░█ ░░█░░
  ▀░░░▀ ▀░░▀ ▀▀▀▀ ▀░░░▀ ▀░░▀   ▀▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ░░▀░░
                                   Created by LimerBoy
''')

query = input(Back.BLACK + Fore.YELLOW + 'Find > ' + Back.RESET + Fore.WHITE)
results = 100

print(Fore.GREEN + '[~] Searching ' + query)

for url in search(query, stop=results):
    print('\n' + Fore.CYAN + '[+] Url detected: ' + url)
    try:
        response = requests.get(url, timeout=1)
        text = response.text
    except:
        continue

    soup = BeautifulSoup(text, "html.parser")
    links_detected = []
    
    try:
        title = soup.title.text.replace('\n', '')
        print(Fore.MAGENTA + '[?] Title: ' + title)
    except:
        print(Fore.RED + '[?] Title: null')
    
    # Find <a> tags
    try:
        for link in soup.findAll('a'):
            href = link['href']
            if href not in links_detected:
                if href.startswith('http'):
                    # Filter
                    if url.split('/')[2] in href:
                        links_detected.append(href)
                    # If requested data found in the URL
                    elif query.lower() in href.lower():
                        print(Fore.GREEN + '--- Requested data found at link: ' + href)
                        links_detected.append(href)
                    # If text in link and link location is similar
                    elif fuzz.ratio(link.text, href) >= 60:
                        print(Fore.GREEN + '--- Text and link are similar: ' + href)
                        links_detected.append(href)
    except:
        continue

    if not links_detected:
        print(Fore.RED + '--- No data found')
