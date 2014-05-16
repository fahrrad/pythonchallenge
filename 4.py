from utilities import get_comment_block
import re

pattern = re.compile(r'[^(A-Z)]+[A-Z]{3}([a-z])[A-Z]{3}[^(A-Z)]+')


page = get_comment_block('http://www.pythonchallenge.com/pc/def/equality.html')

print('first: ', page[0])
print('last: ', page[-1])
print(len(page))

s = ""

for m in pattern.findall(page):
    s += m

print(s)