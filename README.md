# URL PATH FINDER

Find interesting website paths via terminal.

  - Robots.txt parser
  - Use your wordlist
  - For Legal Purposes Only


### Installation

Pfinder requires [Python](https://www.python.org/) 3.x+ to run.

Install the dependencies to run the script.

```sh
$ pip install -r requirements.txt
$ python pfinder.py -u <url> -l <wordlist> --robots
```

### Arguments

Instructions on how to use them in your own terminal are linked below.

| Args | Default | Required |
| ------ | ------ | ------  |
| -u, -url | None | Yes |
| -l, -list | pathss.txt | No |
| --robots | False | No |


### Example

Parsing Robots.txt:
```sh
$ python pfinder.py -u http://example.com -l wordlist.txt --robots
```

Show help:
```sh
$ python pfinder.py -h
```

### Todos

 - Graphic User Interface
 - Progress
 - Find subdomains

### Screenshots

[![P|Finder](https://i.imgur.com/Kw8PL3G.png)](https://github.com/lithg/URL-PATH-FINDER/)

[![P|Finder](https://i.imgur.com/1GbjjHB.png)](https://github.com/lithg/URL-PATH-FINDER/)
