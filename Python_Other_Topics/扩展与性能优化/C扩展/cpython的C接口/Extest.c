#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Python.h"
#define BUFSIZE 10

//原始函数
int fac(int n) {
    if (n < 2)
        return 1;
    return n * fac(n - 1);
}

char *reverse(char *s) {
    register char t;
    char *p = s;
    char *q = (s + (strlen(s) - 1));
    while (p < q) {
        t = *p;
        *p++ = *q;
        *q-- = t;
    }
    return s;
}

//包装函数,为每个模块的每一个函数增加一个型如PyObject* Module_func()的包装函数

static PyObject *
Extest_fac(PyObject *self, PyObject *args) {
    int res;
    int num;
    PyObject* retval;

    res = PyArg_ParseTuple(args, "i", &num);
    if (!res) {
        return NULL;
    }
    res = fac(num);
    retval = (PyObject *)Py_BuildValue("i", res);
    return retval;
}

static PyObject *
Extest_reverse(PyObject *self, PyObject *args) {
    char *orignal;
    if (!(PyArg_ParseTuple(args, "s", &orignal))) {
        return NULL;
    }
    return (PyObject *)Py_BuildValue("s", reverse(orignal));
}

//可以返回原始字符串和翻转字符串
static PyObject *
Extest_doppel(PyObject *self, PyObject *args) {
    char *orignal;
    char *resv;
    PyObject *retval;
    if (!(PyArg_ParseTuple(args, "s", &orignal))) {
        return NULL;
    }
    retval = (PyObject *)Py_BuildValue("ss", orignal, resv=reverse(strdup(orignal)));
    free(resv);
    return retval;
}

//注册方法
static PyMethodDef 
ExtestMethods[] = {
    {"fac", Extest_fac, METH_VARARGS},
    {"doppel", Extest_doppel, METH_VARARGS},
    {"reverse", Extest_reverse, METH_VARARGS},
    {NULL, NULL},
};

//初始化模块
void initExtest() {
    Py_InitModule("Extest", ExtestMethods);
}

//测试函数

int test() {
    char s[BUFSIZE];
    printf("4! == %d\n", fac(4));
    printf("8! == %d\n", fac(8));
    printf("12! == %d\n", fac(12));
    strcpy(s, "abcdef");
    printf("reversing 'abcdef', we get '%s'\n", reverse(s));
    strcpy(s, "madam");
    printf("reversing 'madam', we get '%s'\n", reverse(s));
    return 0;
}

static PyObject *
Extest_test(PyObject *self, PyObject *args) {
    test();
    //返回空的话，就使用下面这一句 
    return (PyObject *)Py_BuildValue("");
}