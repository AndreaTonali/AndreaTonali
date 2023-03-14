import re

test = "caio bella(cid:1234)ciao bella ciao(cid:123)"


def cid2str(string, code):
    cid = f'\(cid\:{code}\)'
    return re.sub(cid, 'CODE', string)
