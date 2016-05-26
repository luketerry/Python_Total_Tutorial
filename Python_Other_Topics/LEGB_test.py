#coding:utf-8
from __future__ import unicode_literals
from math import sin
import sys
def sin(n):
    import math
    return "这是G中的sin"+str(math.sin(n))
def main():
    def sin(n):
        import math
        return "这是E中的sin"+str(math.sin(n))
    def pr():
        def sin(n):
            import math
            return "这是L中的sin"+str(math.sin(n))
        print sin(int(sys.argv[1]))
    pr()
        
if __name__ == "__main__":
    main()