#!/usr/bin/env python
#coding:utf-8
from __future__ import division, print_function
"""一个简单的下载功能
"""
import urllib 
import sys

def main():
    f = urllib.urlopen(sys.argv[1])
    while True:
        buf = f.read(2048)
        if not len(buf):
            break
        sys.stdout.write(buf)
if __name__=="__main__":
    main()