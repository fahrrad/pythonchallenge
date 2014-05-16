from urllib import request


def get_comment_block(page):
    page = request.urlopen(page).readlines()
    
    (start, stop) = get_last_comment_block(page)
    
    everything = page[start:stop+1]

    print("first: ", everything[0])
    print("last: ", everything[-1])
    print("len: ", len(everything))
    
    comment = ''.join([x.decode('utf-8') for x in everything])

    return comment


def get_last_comment_block(page):
    last_start_comment_line = 0
    last_end_comment_line = 0
    
    for i, line in enumerate(page):

        if line.startswith(b"<!--"):
            last_start_comment_line = i
            print(i, line)

        if line.startswith(b"-->"):
            last_end_comment_line = i
            print(i, line)

    return last_start_comment_line+1, last_end_comment_line-1