from hashlib import md5
from random import choice
from datetime import datetime


start = datetime.now()
while True:
    s = "".join([choice("0123456789") for i in range(50)])
    h = md5(s.encode('utf8')).hexdigest()

    if h.endswith("00000"):
        print(s, h)
        print(datetime.now() - start)

