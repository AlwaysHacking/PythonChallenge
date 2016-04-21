import re
import sys
from urllib.request import urlopen

BASE_URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='


def next_nothing(n):
    text = urlopen(BASE_URL + n).read().decode()
    m = re.search('and the next nothing is ([0-9]+)', text)
    if not m:
        print('\n\n' + text + '\n')
    n = m.group(1)
    sys.stdout.write(n + ', ')
    sys.stdout.flush()
    return n

n = '12345'
while True:
    n = next_nothing(n)
