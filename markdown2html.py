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
    markdown_file = argv[1]
    output_file = argv[2]
    if not (path.exists(markdown_file) and path.islink(markdown_file)):
        print("Missing {}".format(argv[1]), file=stderr)
        exit(1)
