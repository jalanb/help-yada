import sys

from help_yada import ArgumentParser

def parse_args():
    lines = __doc__.splitlines()
    head, tail = lines[0], lines[1:]
    parser = ArgumentParser(head, help=tail)
    parser.add_argument('Hello', help='World')
    return parser.parse_args()
    
if __name__ == '__main__':
   parse_args()
