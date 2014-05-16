__author__ = 'wardcoessens'
import glob
import re
from zipfile import ZipFile

pat = re.compile("Next nothing is (\d+)")

acc = ""

def read_file(number, zipfile):
    global acc
    fn = "%s.txt" % number
    with zipfile.open(fn) as f:
        l = f.readline().decode("utf-8")
        m = pat.search(l)

        if m:
            acc += zipfile.getinfo(fn).comment.decode("utf-8")
            return m.group(1)
        else:
            print(number, l, zipfile.getinfo(fn))
            return None


def read_comment_from_zip(filename):
    with ZipFile(filename) as z:
        for i in z.infolist():
            print(i.comment, i.filename)

n = None
with ZipFile("channel.zip") as zf:
    n = read_file(90052, zf)
    while n:
        n = read_file(n, zf)

print(acc)

# read_file(98181)
# read_comments()
# read_comment_from_zip('channel.zip')