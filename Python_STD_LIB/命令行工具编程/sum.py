# !/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import print_function
import argparse

__version__=0.1

def sumarg(args):
    if args.sum:
        print(sum([int(i) for i in args.sum]))

def version(args):
    if args.version :
        print("version:"+str(__version__))

def argp():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sum", type=int,nargs='+', help="add the args ")
    parser.add_argument("-v","--version", help=u"get app's version",action="store_true")

    args = parser.parse_args()
    
    sumarg(args)
    version(args)

if __name__ == '__main__':
    argp()