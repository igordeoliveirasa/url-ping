from navigator import *
import sys

if __name__ == "__main__":
    navigator = Navigator()
    urls = sys.argv[1:]
    for url in urls:
        navigator.ping(url)