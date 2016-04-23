# First, install Pillow (the friendly Python Image Library fork)
# $ pip install Pillow

from PIL import Image
import re
img = Image.open('oxygen.png')

row = [chr(img.getpixel((i, 50))[0]) for i in range(0, 609, 7)]
s = "".join(row)
print(s)

'''
String s is :smart guy, you made it. the next level is
[105, 110, 116, 101, 103, 114, 105, 116, 121]
'''

list = re.findall('\d+', s)
print(''.join(chr(int(n)) for n in list))

'''
Another method is :
print(''.join(chr(int(n)) for n in s[43:-1].replace(',', '').split()))
Or:
''.join(map(chr, map(int, list)))
'''
