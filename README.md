help-yada
=========

Expand `-h` on executables

python
------

```shell
$ echo > help_yada << EOP
"""Expand -h from Python

Send 
* `--help` to help/man page or -h
* `--help-readme` to readme.* or None
* `--help-license` to license* or None
* `--help-tags` to StackOverflow

"""
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
```
