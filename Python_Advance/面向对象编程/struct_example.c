
#include <stdio.h>

#define Pi 3.14;
typedef double (*func)(double);

typedef struct circle{
    double R;
    func acreage;
}Circle;

double function(double r){
    return r*r*Pi;
};
Circle my_circle = {
    .R = 2.0,
    .acreage = function    
};

int main(void){
    printf("%f\n",my_circle.acreage(my_circle.R));
    return 0;
}