import pickle

# Get the original data
from urllib.request import urlopen
url = 'http://www.pythonchallenge.com/pc/def/banner.p'
text = urlopen(url).read()

# Use pickle to serialize the original data
data = pickle.loads(text)

# Print it
for raw in data:
    print(''.join(pair[0] * pair[1] for pair in raw))
