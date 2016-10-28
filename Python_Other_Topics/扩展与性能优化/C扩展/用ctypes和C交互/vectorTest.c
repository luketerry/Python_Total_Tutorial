#include <stdio.h>
#include <string.h>

#include "vector.h"

int main(void){
    Vector a,b,c;
    a.x = 10.0;
    a.y = 20.0;

    b.x = 1.0;
    b.y = 2.0;
    c = add(a,b);
    printf("x %f y %f\n",c.x,c.y);
    return 0;
}
