from urllib.request import urlopen
CHALLENGE_URL = 'http://www.pythonchallenge.com/pc/def/map.html'
text = urlopen(CHALLENGE_URL).read()
#Create a translation table to shift each lower case ASCII byte by 2 places cyclically.
lower = bytes(i for i in range(ord('a'), ord('z') + 1))
table = bytes.maketrans(lower, lower[2:] + lower[:2])
start = text.index(b'g fmnc')
stop = start + text[start:].index(b'\n')
enc = text[start:stop]
print(enc.translate(table))
print(b'map'.translate(table))
