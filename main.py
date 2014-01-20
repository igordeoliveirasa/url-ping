from navigator import *
import sys

if __name__ == "__main__":
    status_code = 0
    navigator = Navigator()
    urls = sys.argv[1:]
    for url in urls:
        if navigator.ping(url) != 200:
            status_code = 1
    sys.exit(status_code)
