import concurrent.futures
import math
from random import choice
from hashlib import md5

def coin(x):
    return md5(x.encode('utf-8')).hexdigest()

def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=30) as executor:
        while True:
            s = "".join([choice("0123456789") for i in range(50)])
            h = coin(s)
            executor.map(coin, s)

            if h.endswith('00000'):
                print(s, h)
            
if __name__ == '__main__':
    main()