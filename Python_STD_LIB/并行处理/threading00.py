# --*--coding:utf-8 --*--
from __future__ import print_function

import threading
import time
 
def worker(i):
    print(i)
    time.sleep(1)
    print("AWAKE")
for i in xrange(5):
    t = threading.Thread(target=worker,args=(i,))
    t.start()
print("closed")