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


global_founds = []

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
print(Fore.YELLOW + "        #  Usage: python3 pfinder.py -u <url> -l <wordlist> --robots   #")
print(Fore.YELLOW + "        ################################################################\n\n")


# -----------------------------------------------------


def format_url(url):
    if not url.endswith('/'):
        url = url + '/'

    if url.startswith('www.'):
        url = url.replace('www.', 'http://')

    return url

# -----------------------------------------------------


def subdomain_format(url):
    if url.startswith('www.'):
        url = url.replace('www.', '')

    if url.startswith('http://'):
        url = url.replace('http://', '')

    if url.startswith('https://'):
        url = url.replace('https://', '')

    return url

# -----------------------------------------------------


def read_robots():
    robots_path = format_url(url) + 'robots.txt'

    print(Fore.YELLOW + '[' + Fore.BLUE + '+' + Fore.YELLOW + ']' + Fore.BLUE + ' Searching paths in robots.txt...')

    try:
        data = urllib.request.urlopen(robots_path).read().decode("utf-8")
        for item in data.split("\n"):
            if item.startswith("Disallow:"):
                robots_found = item[11:]
                found.append(robots_found + Fore.YELLOW + ' (ROBOTS.TXT)')
                print(Fore.YELLOW + '[' + Fore.BLUE + '*' + Fore.YELLOW + ']' + Fore.BLUE + " Disallow rule found:" + Fore.YELLOW, robots_found)

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


def progress(index):
    path_length = len(lines)
    percent = round((index / path_length) * 100, 1)
    percent = str(percent) + '%  ' + '[' + str(index) + '/' + str(path_length) + ']'

    return percent

# -----------------------------------------------------


def timing(total_time):
    sec = timedelta(seconds=total_time)
    d = datetime(1, 1, 1) + sec

    total_time = Fore.BLUE + "\nTiming: %dd:%dh:%dm:%ds" % (d.day-1, d.hour, d.minute, d.second)

    return total_time

# -----------------------------------------------------s


# def test():
#     a = urllib.request.urlopen('http://google.com')
#     print(a.getcode())

# -----------------------------------------------------


def find_paths():
    global total_time
    global found
    # test()
    read_wordlist()
    index = 0
    found_count = 0
    found = []

    if robots:
        read_robots()

    for path in lines:
        path = path.rstrip()
        index += 1

        try:
            code = urllib.request.urlopen(format_url(url) + path).getcode()
            print(Fore.YELLOW + '[' + Fore.GREEN + str(index) + Fore.YELLOW + ']', Fore.GREEN + 'Found! Path:', Fore.YELLOW + path + ' -> ' + progress(index) + ' [CODE : ' + str(code) + ']')
            found.append(path)

        except HTTPError:
            print(Fore.YELLOW + '[' + Fore.BLUE + str(index) + Fore.YELLOW + ']', Fore.RED + 'Failed:', format_url(url) + Fore.BLUE + path + Fore.YELLOW + ' -> ' + progress(index))

        except URLError as e:
            print('Cannot run the script properly. Probably a URL issue.')
            print(Fore.RED + 'Reason:', e)
            break

    end = time.time()
    total_time = end - start

    if len(found) > 0:  
        print('\n' + Fore.GREEN + '########## [' + Fore.BLUE + str(len(found)) + Fore.GREEN + '] PATH(s) FOUND(s) ##########\n')
        for sub in global_founds:
            print(sub)

        for path in found:
            found_count += 1
            print(Fore.YELLOW + '[' + Fore.BLUE + str(found_count) + Fore.YELLOW + '] ' + Fore.BLUE + format_url(url) + Fore.GREEN + path)

    else:
        print(Fore.RED + '\nCannot find any path. Try another wordlist!')

    print(timing(total_time) + '\n')


# -----------------------------------------------------


def subdomain():
    global found
    read_wordlist()
    index = 0
    found_count = 0
    found = []

    if robots:
        read_robots()

    for sub in lines:
        sub = sub.rstrip()

        if sub.endswith('/'):
            sub = sub.replace('/', '.')

        if sub.endswith('.php') or sub.endswith('.txt')  or sub.endswith('.asp'):
            sub = sub[:-3]

        if sub.endswith('.html'):
            sub = sub[:-4]

        sub = 'http://' + sub

        index += 1

        try:
            code = urllib.request.urlopen(sub + subdomain_format(url)).getcode()
            print(Fore.YELLOW + '[' + Fore.GREEN + str(index) + Fore.YELLOW + ']', Fore.GREEN + 'Found! Subdomain:', Fore.YELLOW + sub + subdomain_format(url) + ' -> ' + progress(index) + ' [CODE : ' + str(code) + ']')
            found.append(sub)
            global_founds.append(Fore.YELLOW + '[' + Fore.BLUE + 'X' + Fore.YELLOW + '] ' + sub + Fore.BLUE + subdomain_format(url) + Fore.YELLOW + ' (SUBDOMAIN)')

        except HTTPError:
            print(Fore.YELLOW + '[' + Fore.BLUE + str(index) + Fore.YELLOW + ']', Fore.RED + 'Failed:', sub + subdomain_format(url) + Fore.YELLOW + ' -> ' + progress(index))

        except ValueError:
            print(Fore.YELLOW + '[' + Fore.BLUE + str(index) + Fore.YELLOW + ']', Fore.RED + 'Failed:', sub + subdomain_format(url) + Fore.YELLOW + ' -> ' + progress(index))

        except URLError as e:
            print(Fore.YELLOW + '[' + Fore.BLUE + str(index) + Fore.YELLOW + ']', Fore.RED + 'Failed:', sub + subdomain_format(url) + Fore.YELLOW + ' -> ' + progress(index))

    if len(found) > 0:
        print('\n' + Fore.GREEN + '########## [' + Fore.BLUE + str(len(found)) + Fore.GREEN + '] SUBDOMAIN(s) FOUND(s) ##########\n')
        for sub in found:
            found_count += 1
            print(Fore.YELLOW + '[' + Fore.BLUE + str(found_count) + Fore.YELLOW + '] ' + Fore.BLUE + sub + subdomain_format(url) + '\n')

    else:
        print(Fore.RED + '\nCannot find any subdomain. Try another wordlist!')


# -----------------------------------------------------


if __name__ == '__main__':
    global start
    global robots
    robots = False
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '-url', nargs=1, help='Base URL <required>', default=None, type=str)
    parser.add_argument('-l', '-list', nargs=1, help='Wordlist to search paths', default="paths.txt", type=str)
    parser.add_argument('--robots', action='store_true', help='Parse robots.txt file and append rules to wordlist', default=False)
    parser.add_argument('--sub', action='store_true', help='Search for subdomains in website', default=False)
    args = parser.parse_args()

    if not args.u:
        print(Fore.RED + '***********************************')
        print(Fore.RED + '* URL required to run the script! *')
        print(Fore.RED + '***********************************')
        print(Fore.YELLOW + 'Usage: python3 pfinder.py -u <url> -l <wordlist> --robots --sub\n')

    else:
        url = args.u[0]

    if args.l:
        wordlist = args.l

    if args.sub:
        subdomain()

    if args.robots:
        robots = True

    if len(sys.argv) > 1:
        start = time.time()
        find_paths()