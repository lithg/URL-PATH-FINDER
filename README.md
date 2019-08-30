# URL PATH FINDER

Find interesting website paths via terminal.

  - Robots.txt parser
  - Use your wordlist
  - For Educational Purposes Only


### Installation

Pfinder requires [Python](https://www.python.org/) 3.x+ to run.

Install the dependencies to run the script.

```sh
$ pip install -r requirements.txt
$ python pfinder.py -u <url> -l <wordlist> --robots
```

### Arguments

Instructions on how to use them in your own terminal are linked below.

| Args | Example | Required |
| ------ | ------ | ------  |
| -u, -url | default: None | Yes |
| -l, -list | default: path.txt | No |
| --robots | default: False | No |


### Example

Parsing Robots.txt:
```sh
$ python pfinder.py -u http://example.com -l wordlist.txt --robots
```
### Todos

 - Graphic User Interface
