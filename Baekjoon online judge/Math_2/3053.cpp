#define _USE_MATH_DEFINES
#include <cstdio>
#include <cmath>

using namespace std;

int main(void){

    int r;
    scanf("%d", &r);

    double u_circle_area=M_PI*double(r)*double(r);
    double t_circle_area=2.0*double(r)*double(r);

    printf("%.6f\n%.6f", u_circle_area, t_circle_area);

    return 0;
}