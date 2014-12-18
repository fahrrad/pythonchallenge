from PIL import Image
from urllib import request
from urllib.parse import quote

__author__ = 'CoesseW'
img_file = open('oxygen.png', 'rb')

def print_color(pxl_array, pos):
    print("color@ %dx0: %s" %(pos, pxl_array[pos]))

def return_more_than_three_in_a_row(string):
    """yields every character in a sequence that occurs more 3 or more times ONCE for evey occurence
    >>> return_more_than_three_in_a_row("aabbbccccddeee")
    "bce"
    >>> return_more_than_three_in_a_row("")
    ""
    >>> return_more_than_three_in_a_row("abcdefg")
    ""

    Now that I think of it, i could probably do it easier by using this regex: ([a-z])\1\1+ => \1
    """
    return_list = []

    previous = ''
    count = 1
    for x in string:
        if x != previous:
            previous = x
            count = 1
        elif x == previous and count == 2:
            count += 1
            return_list.append(x)
        elif x == previous and count > 8:
            count = 1
            return_list.append(x)
        else:
            count += 1

    return return_list

def ordinals2string(ordinals):
    return ''.join([chr(x) for x in ordinals])

if not img_file:
    img_url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
    request.urlretrieve(img_url, 'oxygen.png')

img_file = open('oxygen.png', 'rb')
image = Image.open(img_file)
img_bbox = image.getbbox()
_,_, img_width, img_height = img_bbox
print("image dimensions (%dx%d)" % (img_width, img_height))


img_data = list(image.getdata())
# loop over the first pixel of every row, and find the onces with b=r=g
for i,(r,g,b,a) in enumerate(img_data[::img_width]):
    if r == g == b:
        print(i,r)

# I saw that row 46 is the middle row of the row that contains the greys
band = 46
row = img_data[img_width * band: img_width * (band+1)]

ordinals = (return_more_than_three_in_a_row([r for r,_,_,_ in row]))
print(ordinals2string(ordinals))
print (ordinals2string([105, 1110, 1116, 101, 103, 1114, 105, 1116, 121]))







