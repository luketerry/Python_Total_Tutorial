#!/usr/bin/env python
# --*-- coding:utf-8 --*--
from __future__ import print_function
import sys
import getopt
 #去掉第一位的自身名字

#短选项,'hvo:' 为短选项处理格式，h,v,都表示是为无参数，o:表示必有参数,必须要有参数的则在字符后面加“:”表示.
#getopt.getopt(args,'hvt:') 
#['help', 'version', 'output='] 为长选项处理格式，help,version都表示为无参数,output=表示为必有参数，表达工里需要在字符串后加 "=" 表示。

optlist,args = getopt.getopt(sys.argv[1:],'t:') 

def main():
    times = 1
    s = None

    for o,v in optlist:
        if o=="-t":
            times = int(v)
    if args:
        s = args[0]
    print(s*times)

if __name__ == "__main__":
    main()
