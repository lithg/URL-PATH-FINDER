import urllib.request


def find_paths():
    count = 0
    found = []
    url = 'https://controle.podcast45minutos.com.br/'

    with open('paths.txt') as path:
        lines = path.readlines()

    for path in lines:
        path = path.rstrip()

        try:
            urllib.request.urlopen(url + path).getcode()
            print('Panel found! Path:', path)
            found.append(path)

        except ValueError:
            count += 1
            print('[' + str(count) + ']', 'Trying:', path)

    if len(found) > 0:
        print('#-#-#-#-# PANEL FOUNDS #-#-#-#-#')
        for panel in found:
            print('[' + str(panel.index()) + ']', url + path)


if __name__ == '__main__':
    find_paths()