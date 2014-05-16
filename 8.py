__author__ = 'wardcoessens'
from urllib import request
import png

png = png.Reader(file=request.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png"))

pxls = png.asRGBA()[2]


for (r,g,b) in pxls:
    print(r,g,b)
