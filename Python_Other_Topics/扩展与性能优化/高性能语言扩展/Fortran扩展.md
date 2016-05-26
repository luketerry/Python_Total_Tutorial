
fortran是一门活跃于科学计算的古老语言,活跃在科学计算领域,它的执行效率很高.所以也常有人拿他扩展python

[f2py](https://sysbio.ioc.ee/projects/f2py2e/)是numpy的一个子项目,它就是用来写fortran扩展的


```python
%%writefile testfortran.f90
!SUBROUTINE        
      SUBROUTINE ADDSUB(A,B,C,D)  
      IMPLICIT NONE  
      DOUBLE PRECISION A,B,C,D  
!f2py intent(in) :: A,B  
!f2py intent(out) :: C,D  
      C = A + B  
      D = A - B  
      print*, "ADDSUB From Fortran!"  
      print*, "ADD=",C  
      print*, "SUB=",D  
      RETURN  
      END  
```

    Overwriting testfortran.f90


    !f2py intent(in) :: A,B  
    !f2py intent(out) :: C,D  
    
在fortran中是注释,而在f2py中是签名,注意签名前面不能有空格


```python
!f2py -m testfortran -c testfortran.f90  
```

    [39mrunning build[0m
    [39mrunning config_cc[0m
    [39munifing config_cc, config, build_clib, build_ext, build commands --compiler options[0m
    [39mrunning config_fc[0m
    [39munifing config_fc, config, build_clib, build_ext, build commands --fcompiler options[0m
    [39mrunning build_src[0m
    [39mbuild_src[0m
    [39mbuilding extension "testfortran" sources[0m
    [39mf2py options: [][0m
    [39mf2py:> /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7/testfortranmodule.c[0m
    [39mcreating /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD[0m
    [39mcreating /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7[0m
    Reading fortran codes...
    	Reading file 'testfortran.f90' (format:fix)
    Post-processing...
    	Block: testfortran
    			Block: addsub
    Post-processing (stage 2)...
    Building modules...
    	Building module "testfortran"...
    		Constructing wrapper function "addsub"...
    		  c,d = addsub(a,b)
    	Wrote C/API module "testfortran" to file "/var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7/testfortranmodule.c"
    [39m  adding '/var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7/fortranobject.c' to sources.[0m
    [39m  adding '/var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7' to include_dirs.[0m
    [39mcopying /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/numpy/f2py/src/fortranobject.c -> /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7[0m
    [39mcopying /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/numpy/f2py/src/fortranobject.h -> /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7[0m
    [39mbuild_src: building npy-pkg config files[0m
    [39mrunning build_ext[0m
    [39mcustomize UnixCCompiler[0m
    [39mcustomize UnixCCompiler using build_ext[0m
    [39mcustomize Gnu95FCompiler[0m
    [32mFound executable /usr/local/bin/gfortran[0m
    [39mcustomize Gnu95FCompiler[0m
    [39mcustomize Gnu95FCompiler using build_ext[0m
    [39mbuilding 'testfortran' extension[0m
    [39mcompiling C sources[0m
    [39mC compiler: gcc -fno-strict-aliasing -I/Users/huangsizhe/Lib/conda/anaconda/include -arch x86_64 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes
    [0m
    [39mcreating /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/var[0m
    [39mcreating /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/var/folders[0m
    [39mcreating /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/var/folders/2g[0m
    [39mcreating /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn[0m
    [39mcreating /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T[0m
    [39mcreating /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD[0m
    [39mcreating /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7[0m
    [39mcompile options: '-I/var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7 -I/Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/numpy/core/include -I/Users/huangsizhe/Lib/conda/anaconda/include/python2.7 -c'[0m
    [39mgcc: /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7/fortranobject.c[0m
    In file included from /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7/fortranobject.c:2:
    In file included from /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7/fortranobject.h:13:
    In file included from /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/numpy/core/include/numpy/arrayobject.h:15:
    In file included from /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:17:
    In file included from /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1728:
    /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/numpy/core/include/numpy/npy_deprecated_api.h:11:2: warning: "Using deprecated NumPy API, disable it by #defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
    #warning "Using deprecated NumPy API, disable it by #defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
     ^
    /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7/fortranobject.c:338:30: warning: equality comparison with extraneous parentheses [-Wparentheses-equality]
            if ((fp->defs[i].func==NULL)) {
                 ~~~~~~~~~~~~~~~~^~~~~~
    /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7/fortranobject.c:338:30: note: remove extraneous parentheses around the comparison to silence this warning
            if ((fp->defs[i].func==NULL)) {
                ~                ^     ~
    /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7/fortranobject.c:338:30: note: use '=' to turn this equality comparison into an assignment
            if ((fp->defs[i].func==NULL)) {
                                 ^~
                                 =
    2 warnings generated.
    [39mgcc: /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7/testfortranmodule.c[0m
    In file included from /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7/testfortranmodule.c:17:
    In file included from /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7/fortranobject.h:13:
    In file included from /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/numpy/core/include/numpy/arrayobject.h:15:
    In file included from /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:17:
    In file included from /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1728:
    /Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/numpy/core/include/numpy/npy_deprecated_api.h:11:2: warning: "Using deprecated NumPy API, disable it by #defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
    #warning "Using deprecated NumPy API, disable it by #defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
     ^
    1 warning generated.
    [39mcompiling Fortran sources[0m
    [39mFortran f77 compiler: /usr/local/bin/gfortran -Wall -ffixed-form -fno-second-underscore -m64 -fPIC -O3 -funroll-loops
    Fortran f90 compiler: /usr/local/bin/gfortran -Wall -fno-second-underscore -m64 -fPIC -O3 -funroll-loops
    Fortran fix compiler: /usr/local/bin/gfortran -Wall -ffixed-form -fno-second-underscore -Wall -fno-second-underscore -m64 -fPIC -O3 -funroll-loops[0m
    [39mcompile options: '-I/var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7 -I/Users/huangsizhe/Lib/conda/anaconda/lib/python2.7/site-packages/numpy/core/include -I/Users/huangsizhe/Lib/conda/anaconda/include/python2.7 -c'[0m
    [39mgfortran:fix: testfortran.f90[0m
    [39m/usr/local/bin/gfortran -Wall -m64 -Wall -undefined dynamic_lookup -bundle /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7/testfortranmodule.o /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/src.macosx-10.5-x86_64-2.7/fortranobject.o /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD/testfortran.o -L/usr/local/Cellar/gcc/5.3.0/lib/gcc/5/gcc/x86_64-apple-darwin15.0.0/5.3.0 -L/Users/huangsizhe/Lib/conda/anaconda/lib -lgfortran -o ./testfortran.so[0m
    [39mrunning scons[0m
    Removing build directory /var/folders/2g/vh7qp8xx7px1bplwvcn1fm_h0000gn/T/tmpY0QaoD


会在当前目录下生成testfortran.so的文件.


```python
!ls
```

    Fortran扩展.ipynb               testfortran.f90                 [31mtestfortranpypy.pypy-26.so[m[m
    ffitest.c                       [31mtestfortran.so[m[m                  [1m[36mtestfortranpypy.pypy-26.so.dSYM[m[m


于是我们就可以用它了


```python
import testfortran
```


```python
print testfortran.__doc__  
```

    This module 'testfortran' is auto-generated with f2py (version:2).
    Functions:
      c,d = addsub(a,b)
    .



```python
x=testfortran.addsub(4,9)
```


```python
x
```




    (13.0, -5.0)




```python
%timeit testfortran.addsub(4,9)
```

    100000 loops, best of 3: 17.1 µs per loop


pypy也支持fortran扩展,只是不如cpython那么快

    !f2pypy -m testfortranpypy -c testfortran.f90  


```python
import testfortranpypy as t
```


```python
print t.__doc__  
```

    This module 'testfortranpypy' is auto-generated with f2py (version:2).
    Functions:
      c,d = addsub(a,b)
    .



```python
x=t.addsub(4,9)
```


```python
x
```




    (13.0, -5.0)




```python
%timeit t.addsub(4,9)
```

    The slowest run took 6.37 times longer than the fastest. This could mean that an intermediate result is being cached.
    10000 loops, best of 3: 19.6 µs per loop

