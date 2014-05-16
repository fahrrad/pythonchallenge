
from collections import defaultdict
import utilities as i

import re

comment = i.get_comment_block("http://www.pythonchallenge.com/pc/def/ocr.html")

d = defaultdict(int)
for x in comment:
    d[x] += 1

rare_letters = [k for k,v in d.items() if v <= 1]

print ('rare letters: ', rare_letters)

print (re.sub('[^%s]'% ''.join(rare_letters),'', comment))
