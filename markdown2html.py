#!/usr/bin/python3

from sys import argv
from sys import stderr
from os import path

"""
Converts Markdown to HTML
"""


def parse_headings(headings_list: list):
    """
    Parses markdown headings and converts them to HTML heading tags
    """
    html_headings = []
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
        html_headings.append(headings)
    return html_headings


def parse_unordered_lists(unorded_list: list) -> 'HTML ul li':
    '''
    Parses markdown unordered lists and converts them to HTML heading tags
    '''
    html_unordered = []
    number_of_li = []
    for uls in unorded_list:
        if len(uls) > 0 and uls[0] == '-':
            html_unordered.append('<ul>')
            html_unordered.append('<li>' + uls[1:].strip(' ') + '</li>')
        elif len(uls) == 0 or uls[0] != '-':
            html_unordered.append('</ul>')
            html_unordered.append(uls)
    return html_unordered


def _main():
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
    elif not path.exists(argv[1]):
        print('Missing {}'.format(argv[1]), file=stderr)
        exit(1)
    else:
        print()
        exit(0)

    markdown_file = argv[1]
    output_file = argv[2]

    # List of markdown file elements
    md_parser_list = []

    '''
    Reads markdown file and parses content
    '''
    with open(markdown_file) as file:
        md_parser_list = file.readlines()
    md_parser_list = ''.join(md_parser_list).split('\n')

    md_parser_list = parse_headings(md_parser_list)
    md_parser_list = '\n'.join(md_parser_list).split('\n')

    md_parser_list = parse_unordered_lists(md_parser_list)
    md_parser_list = '\n'.join(md_parser_list).split('\n')

    '''
    Create HTML file and write converted markdown to html tags
    '''
    with open(output_file, 'w') as file:
        for md_symbol in md_parser_list:
            file.write(md_symbol + '\n')


if __name__ == '__main__':
    _main()
