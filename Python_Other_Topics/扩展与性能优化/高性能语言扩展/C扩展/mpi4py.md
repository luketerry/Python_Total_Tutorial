
mpi是c,c++,以及fortran下的并行框架,而[mpi4py](http://mpi4py.readthedocs.org/en/stable/)是它的python接口,pypy也可以使用呦

安装它先要安装openmpi,然后安装numpy和cython

> 例 


```
%%writefile hl.py
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("hello world")
print("my rank is:",rank)
```

    Overwriting hl.py


    mpirun –np 3 python h1.py
