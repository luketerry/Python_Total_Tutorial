#! /usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import print_function
import shutil
import argparse
import os

__version__=1.0
__author__="Huang Sizhe"

class InputError(Exception):
    def __init__(self, arg):
        self.value = arg
    def __str__(self):
        return repr(self.value)

def version(args):
    if args.version :
        print("version:"+str(__version__))

def rename(args):
    try:
        assert (True if len(args.rename)==2 else False)
    except AssertionError:
        raise InputError('too many args')
    try:
        assert os.path.exists(args.rename[0])
    except AssertionError:
        raise InputError("target path doesn't exist")
    try:
        assert (not (os.path.exists(args.rename[1])))
    except AssertionError:
        raise InputError("file is already exist")

    os.rename(args.rename[0],args.rename[1])
    print("done!")


def argp():
    parser = argparse.ArgumentParser()
    parser.add_argument("rename",nargs='+',help="rename a file")
    parser.add_argument("-v","--version", help=u"get app's version",action="store_true")

    args = parser.parse_args()

    rename(args)
    version(args)

if __name__ == '__main__':
    argp()
