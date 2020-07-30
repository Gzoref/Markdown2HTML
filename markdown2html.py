#!/usr/bin/python3

'''
Converts Markdown to HTML
'''
from sys import argv
from sys import stderr
from os import path


if __name__ == "__main__":
    '''
    Error messages
    '''
    if len(argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html', file=stderr)
        exit(1)
    if not path.exists(argv[1]):
        print('Missing {}'.format(argv[1]), file=stderr)
        exit(1)
    exit(0)

    """
    '''
    List of markdown file elements
    '''

    md_parser_list = []
    '''
    Reads markdown file and parses content
    '''

    html_headings = []
    number_of_hashes = 0
    for headings in md_parser_list:
        pass

    with open(markdown_file) as file:
        md_parser_list = file.readlines()

    '''
    Create HTML file and write converted markdown to html tags
    '''
    with open(output_file, 'w') as file:
        for md_symbol in md_parser_list:
            file.write(md_symbol + '\n') """
