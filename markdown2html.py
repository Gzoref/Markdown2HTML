#!/usr/bin/python3

'''
Converts Markdown to HTML
'''

from sys import argv
from sys import stderr
from os import path


def parse_headings(headings_list: list):
    '''
    Parses markdown headings and converts them to HTML heading tags
    '''
    html_headings = []
    number_of_hashes = 0

    # If hash '#' is found, count number of hashes
    for headings in headings_list:
        if len(headings) > 0 and headings[0] == '#':
            while number_of_hashes < len(
                    headings) and headings[number_of_hashes] == '#':
                number_of_hashes += 1
            # If more than 6 hashes, default to h6
            if number_of_hashes > 6:
                number_of_hashes = 6
            html_tag = 'h' + str(number_of_hashes)
            headings = headings.strip('#')
            headings = headings.strip(' ')
            headings = '<' + html_tag + '>' + headings + '</' + html_tag + '>'
        html_headings.append(headings)
    return html_headings


def file_read_write():
    '''
    Parses markdown file, makes appropriate method call
    and creates HTML file with correct tags
    '''

    '''
    Error messages
    '''
    if len(argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html', file=stderr)
        exit(1)
    if not path.exists(argv[1]):
        print('Missing {}'.format(argv[1]), file=stderr)
        exit(1)

    markdown_file = argv[1]
    output_file = argv[2]

    '''
    List of markdown file elements
    '''

    md_parser_list = []

    '''
    Reads markdown file and parses content
    '''

    with open(markdown_file, 'r') as file:
        md_parser_list = file.readlines()
    md_parser_list = ''.join(md_parser_list).split('\n')

    md_parser_list = parse_headings(md_parser_list)
    md_parser_list = '\n'.join(md_parser_list).split('\n')

    '''
    Create HTML file and write converted markdown to html tags
    '''
    with open(output_file, 'w') as file:
        for md_symbol in md_parser_list:
            file.write(md_symbol + '\n')


if __name__ == "__main__":
    file_read_write()
