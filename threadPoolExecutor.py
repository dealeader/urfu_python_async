import concurrent.futures
from urllib.request import urlopen
from urllib.parse import unquote

def load_url(url, timeout):
        with urlopen(url, timeout=timeout) as conn:
            return conn.read()


with open('res.txt', encoding="utf-8") as URLS:
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS.read().split("\n")}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))