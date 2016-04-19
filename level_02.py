# Get the mission HTML data with urlopen.
from urllib.request import urlopen
CHALLENGE_URL = 'http://www.pythonchallenge.com/pc/def/ocr.html'
text = urlopen(CHALLENGE_URL).read()

# Find the enciphered text.
start = text.index(b'%%$@')
stop = start + text[start:].index(b'\n-->')
enc = text[start:stop]

# Recognize the character.
s = list(filter(lambda x: x in range(ord('a'), ord('z') + 1), enc))
key = ''
for ch in s:
    key += chr(ch)
print(key)
