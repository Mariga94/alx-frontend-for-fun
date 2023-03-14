#!/usr/bin/python3
"""
Markdown to HTML
"""
from sys import argv, stderr, exit
from os import path
if __name__ == "__main__":
    size = len(argv)
    if size < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)
    my_path = path.exists(argv[1])
    if my_path is False:
        print("Missing {}".format(argv[1]), file=stderr)
        exit(1)
