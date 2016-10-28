#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "vector.h"

//向量结构体
Vector add(Vector a,Vector b){
    Vector c;
    c.x = a.x+b.x;
    c.y = a.y+b.y;
    return c;
}
