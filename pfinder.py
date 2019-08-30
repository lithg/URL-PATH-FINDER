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
import argparse
import sys


# -----------------------------------------------------

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
\n''')

print(Fore.YELLOW + "        ################# - Interesting Paths Finder - #################")
print(Fore.YELLOW + "        #                Works better with python 3.x                  #")
print(Fore.YELLOW + "        #           Usage: python3 pfinder.py -u <url> -l <wordlist>      #")
print(Fore.YELLOW + "        ################################################################\n\n")


# -----------------------------------------------------


def format_url(url):

    if not url.endswith('/'):
        url = url + '/'

    if url.startswith('www.'):
        url = url.replace('www.', 'http://')

    return url

# -----------------------------------------------------


def read_robots():
    robots_path = format_url(url) + 'robots.txt'

    print(Fore.YELLOW + '[' + Fore.BLUE + '+' + Fore.YELLOW + ']' + Fore.BLUE + ' Find paths in robots.txt...')

    try:
        data = urllib.request.urlopen(robots_path).read().decode("utf-8")
        for item in data.split("\n"):
            if item.startswith("Disallow:"):
                robots_found = item[11:]
                found.append(robots_found + Fore.YELLOW + ' (ROBOTS.TXT)')
                print(Fore.YELLOW + '[' + Fore.BLUE + '*' + Fore.YELLOW + ']' + Fore.BLUE + " Disallow rule found:", robots_found)

    except HTTPError:
        print(Fore.YELLOW + '[' + Fore.RED + 'x' + Fore.YELLOW + ']' + Fore.BLUE + " Could not retrieve robots.txt!")


# -----------------------------------------------------


def read_wordlist():
    global lines

    try:
        with open(wordlist) as path:
            lines = path.readlines()

    except:
        print(Fore.RED + 'Error while trying to read wordlist.')

# -----------------------------------------------------


def timing(total_time):

    sec = timedelta(seconds=total_time)
    d = datetime(1,1,1) + sec

    total_time = Fore.BLUE + "\nTiming: %dd:%dh:%dm:%ds" % (d.day-1, d.hour, d.minute, d.second)

    return total_time

# -----------------------------------------------------


def find_paths():
    read_wordlist()
    count = 0
    found_count = 0
    global found
    found = []
    global total_time

    start = time.time()  # TIMER START

    if robots:
        read_robots()

    for path in lines:
        path = path.rstrip()
        count += 1

        try:
            urllib.request.urlopen(format_url(url) + path)
            print(Fore.YELLOW + '[' + Fore.GREEN + str(count) + Fore.YELLOW + ']', Fore.GREEN + 'Found! Path:', Fore.YELLOW + path)
            found.append(path)

        except HTTPError:
            print(Fore.YELLOW + '[' + Fore.BLUE + str(count) + Fore.YELLOW + ']', Fore.RED + 'Failed:', format_url(url) + Fore.BLUE + path)

        except URLError as e:
            print('Cannot run the script properly. Probably a URL issue.')
            print(Fore.RED + 'Reason:', e)
            break

    end = time.time()
    total_time = end - start

    if len(found) > 0:
        print('\n' + Fore.GREEN + '*#*#*#*#*#* [' + Fore.BLUE + str(len(found)) + Fore.GREEN + '] PATH(s) FOUND(s) *#*#*#*#*#*\n')
        for path in found:
            found_count += 1
            print(Fore.YELLOW + '[' + Fore.BLUE + str(found_count) + Fore.YELLOW + '] ' + Fore.BLUE + format_url(url) + Fore.GREEN + path)

    else:
        print(Fore.RED + '\nCannot find any path. Try another wordlist!')

    print(timing(total_time))


# -----------------------------------------------------


if __name__ == '__main__':
    global robots
    robots = False
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '-url', nargs=1, help='Base URL', default=None, type=str)
    parser.add_argument('-l', '-list', nargs=1, help='Wordlist to use', default="paths.txt", type=str)
    parser.add_argument('--robots', action='store_true', help='Parse robots.txt file', default=False)
    args = parser.parse_args()

    if not args.u:
        print(Fore.RED + '***********************************')
        print(Fore.RED + '* URL required to run the script! *')
        print(Fore.RED + '***********************************')
        print(Fore.YELLOW + 'Usage: python3 pfinder.py -u <url> -l <wordlist> --robots \n')

    else:
        url = args.u[0]

    if args.l:
        wordlist = args.l

    if args.robots:
        robots = True

    if len(sys.argv) > 1:
        find_paths()

