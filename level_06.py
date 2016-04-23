import zipfile
import re

findnothing = re.compile(r'Next nothing is (\d+)').match
seed = '90052'
z = zipfile.ZipFile("channel.zip", "r")  # Load the zip file.
comments = []

while True:
    fname = seed + '.txt'
    comments.append(z.getinfo(fname).comment.decode())
    text = z.read(fname).decode()
    m = findnothing(text)
    if m:
        seed = m.group(1)
    else:
        break

print("".join(comments))
