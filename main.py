# -*- coding: utf-8 -*-

'''
Interesting Paths Finder
Author: lithg
github.com/lithg
'''

import urllib.request
from urllib.error import URLError, HTTPError
import time


url = ''
wordlist = ''


def format_url(url):

    if not url.endswith('/'):
        url = url + '/'

    return url


def read_wordlist():
    global lines

    try:
        with open('paths.txt') as path:
            lines = path.readlines()

    except:
        print('eee')


def find_paths():
    read_wordlist()
    count = 0
    found = []

    for path in lines:
        path = path.rstrip()

        try:
            urllib.request.urlopen(format_url(url) + path).getcode()
            print('Panel found! Path:', path)
            found.append(path)

        except HTTPError:
            count += 1
            print('[' + str(count) + ']', 'Trying:', path)

        except URLError as e:
            print('Cannot run the script properly. Probably a URL issue.')
            print('Reason: ' + e)

    if len(found) > 0:
        print('#-#-#-#-# [' + str(len(found)) + '] + PANEL FOUNDS #-#-#-#-#')
        for panel in found:
            print('[' + str(panel.index()) + ']', url + path)

    else:
        print('Cannot find any path. Try another wordlist!')


if __name__ == '__main__':
    find_paths()