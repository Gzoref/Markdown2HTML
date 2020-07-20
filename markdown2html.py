#!/usr/bin/python3

from sys import argv
from sys import stderr
from os import path

"""
Converts Markdown to HTML
"""

def parse_headings(headings_list):
    """
    Parses markdown headings and converts them to HTML heading tags
    """
    md_headings = []
    number_of_hashes = 0
    for headings in headings_list:
        if len(headings) > 0 and headings[0] == '#':
            while number_of_hashes < len(
                    headings) and headings[number_of_hashes] == '#':
                number_of_hashes += 1
            if number_of_hashes > 6:
                number_of_hashes = 6
            html_tag = 'h' + str(number_of_hashes)
            headings = headings.strip('#')
            headings = headings.strip(' ')
            headings = '<' + html_tag + '>' + headings + '</' + html_tag + '>'
        md_headings.append(headings)
    return md_headings


def _main():
    if len(argv) < 3:
        print('Usage: ./markdown2html.py README.md', file=stderr)
        exit(1)
    if not path.exists(argv[1]):
        print('Missing {}'.format(argv[1]), file=stderr)
        exit(1)

    markdown_file = argv[1]
    output_file = argv[2]
    md_parser_list = []
    md_text_list = []

    with open(markdown_file) as file:
        md_parser_list = file.readlines()
    md_parser_list = ''.join(md_parser_list).split('\n')

    md_parser_list = parse_headings(md_parser_list)
    md_parser_list = '\n'.join(md_parser_list).split('\n')

    with open(output_file, 'w') as file:
        for md_symbol in md_parser_list:
            file.write(md_symbol + '\n')


if __name__ == "__main__":
    _main()
