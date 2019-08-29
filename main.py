# -*- coding: utf-8 -*-

'''
Interesting Paths Finder
Author: lithg
github.com/lithg
'''

import urllib.request
from urllib.error import URLError, HTTPError
import time
from datetime import datetime, timedelta
from colorama import Fore

print(Fore.RED + '''
 ██▓███   ▄▄▄     ▄▄▄█████▓ ██░ ██      █████▒██▓ ███▄    █ ▓█████▄ ▓█████  ██▀███  
▓██░  ██▒▒████▄   ▓  ██▒ ▓▒▓██░ ██▒   ▓██   ▒▓██▒ ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░   ▒████ ░▒██▒▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██    ░▓█▒  ░░██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░ ▓█   ▓██▒ ▒██▒ ░ ░▓█▒░██▓   ░▒█░   ░██░▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░ ▒▒   ▓▒█░ ▒ ░░    ▒ ░░▒░▒    ▒ ░   ░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░     
░▒ ░       ▒   ▒▒ ░   ░     ▒ ░▒░ ░    ░      ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░   
░░         ░   ▒    ░       ░  ░░ ░    ░ ░    ▒ ░   ░   ░ ░  ░ ░  ░    ░     ░░   ░        by ''' + Fore.GREEN + 'LITHG' + '''
               ░  ░         ░  ░  ░           ░           ░    ░       ░  ░   ░     
                                                             ░                     
''')


url = ''
wordlist = 'paths.txt'


def format_url(url):

    if not url.endswith('/'):
        url = url + '/'

    return url


def read_wordlist():
    global lines

    try:
        with open(wordlist) as path:
            lines = path.readlines()

    except:
        print('Error while trying to read file.')


def timing(total_time):

    sec = timedelta(seconds=total_time)
    d = datetime(1,1,1) + sec

    total_time = "\nTiming: %dd:%dh:%dm:%ds" % (d.day-1, d.hour, d.minute, d.second)

    return total_time


def find_paths():
    read_wordlist()
    count = 0
    found_count = 0
    found = []
    global total_time

    start = time.time()  # TIMER START

    for path in lines:
        path = path.rstrip()

        try:
            urllib.request.urlopen(format_url(url) + path).getcode()
            print('Panel found! Path:', path)
            found.append(path)

        except HTTPError:
            count += 1
            print('[' + str(count) + ']', 'Failed:', format_url(url) + path)

        except URLError as e:
            print('Cannot run the script properly. Probably a URL issue.')
            print('Reason:', e)
            break

    end = time.time()
    total_time = end - start

    if len(found) > 0:
        print('#-#-#-#-# [' + str(len(found)) + '] PATH FOUND(s) #-#-#-#-#')
        for panel in found:
            found_count += 1
            print('[' + str(found_count) + ']', url + path)

    else:
        print('Cannot find any path. Try another wordlist!')

    print(timing(total_time))


if __name__ == '__main__':
    find_paths()