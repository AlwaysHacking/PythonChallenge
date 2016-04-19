import re
# Get the mission HTML data with urlopen.
from urllib.request import urlopen
CHALLENGE_URL = 'http://www.pythonchallenge.com/pc/def/equality.html'
text = urlopen(CHALLENGE_URL).read()

# ***decode b'' --> ''
text = text.decode()

# Use regular expressions to find the requried characters
print(''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', text)))    
