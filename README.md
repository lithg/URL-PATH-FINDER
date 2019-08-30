# URL PATH FINDER

Find interesting website paths via terminal.

  - Robots.txt parser
  - Use your wordlist
  - For Educational Purposes Only


### Installation

Dillinger requires [Python](https://www.python.org/) 3.x+ to run.

Install the dependencies to run the script.

```sh
$ pip install -r requirements.txt
$ python pfinder.py -u <url> -l <wordlist> --robots
```

### Plugins

Dillinger is currently extended with the following plugins. Instructions on how to use them in your own application are linked below.

| Args | Example |
| ------ | ------ |
| -u, -url | http://example.com |
| -l -list | default: path.txt |
| --robots | default: False |


### Example

Parsing Robots.txt:
```sh
$ python pfinder.py -u http://example.com -l wordlist.txt --robots
```
### Todos

 - Graphic User Interface
