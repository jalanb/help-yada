# hype
Expand help

`hylp` is a command to help helps

# git

`hylp` is built on an idea from `git`:

# git -h 
A short option like `-h` shows CLI arguments

     $ git status -h | sed -e"/^ *$/d" | head -n 4
     usage: git status [<options>] [--] <pathspec>...

    -v, --verbose         be verbose
    -s, --short           show status concisely
    
## git --help
A longer `--help` invokes `man` for more

    $ git status --help | head -n 4
    GIT-STATUS(1)         Git Manual   GIT-STATUS(1)

    NAME
       git-status - Show the working tree status
       

# fd
`fd` offers more levels

## fd -h
A short option like `-h` shows CLI arguments

    $ fd -h | head -n 6
    fd 7.1.0
    USAGE:
        fd [FLAGS/OPTIONS] [<pattern>] [<path>...]
    FLAGS:
        -H, --hidden            Search hidden files and directories
        -I, --no-ignore         Do not respect .(git|fd)ignore files

## fd --help
A longer `--help` show more detail on the args

    $ fd --help | head -n 7
    fd 7.1.0
    USAGE:
        fd [FLAGS/OPTIONS] [<pattern>] [<path>...]
    FLAGS:
        -H, --hidden
                Include hidden directories and files in the search results (default: hidden files and directories are skipped).
        -I, --no-ignore

## help fd
`man` and `info` are available

    $ LINES=7 man fd
    FD(1)
    NAME
           fd - find entries in the filesystem
    SYNOPSIS
           fd [-HIEsiaLp0hV] [-d depth] [-t filetype] [-e ext] [-E exclude] [-c when] [-j num] [-x cmd] [pattern] [path...]
    DESCRIPTION
           fd is a simple, fast and user-friendly alternative to find(1).

    $ LINES=4 info fd
    File: *manpages*,  Node: fd,  Up: (dir)
    FD(1) 
    NAME
           fd - find entries in the filesystem
