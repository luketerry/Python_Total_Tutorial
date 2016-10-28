#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//向量结构体
typedef struct{
    float x,y;
    char repr[50];
}Vector;

Vector add(Vector a,Vector b){
    Vector c;
    c.x = a.x+b.x;
    c.y = a.y+b.y;
    char tempx[10];
    char tempy[10];
    //char x = itoa(c.x,&tempx,10);
    //char y = itoa(c.y,&tempy,10);
    int len = sprintf(c.repr, "<x:%f,y:%f>\n",c.x,c.y);
    //c.repr = "<x:" + x + "," + "y:" + y + ">";
    return c;
}

int main(void){
    Vector a,b,c;
    a.x = 10.0;
    a.y = 20.0;
    strcpy(a.repr,"<x:10.0,y:20.0>");

    b.x = 1.0;
    b.y = 2.0;
    strcpy(b.repr,"<x:10.0,y:20.0>");
    c = add(a,b);
    printf("x %f y %f\n",c.x,c.y);
    printf("%s\n",c.repr);
    return 0;
}
