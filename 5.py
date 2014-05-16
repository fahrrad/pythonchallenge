__author__ = 'wardcoessens'
from urllib import request
import re

response_pat = re.compile("and the next nothing is (\d+)")


def open_request(number):
    resp = request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d" % number).read()

    m = response_pat.search(resp.decode("utf-8"))

    if m:
        print(m.groups()[0])
        return m.groups()[0]
    else:
        return None

# linkedlists.php
n = open_request(16044/2)
while n:
    n = open_request(int(n))

# end with 66831