#include <cstdio>

using namespace std;

int main(void){

    int x, y, w, h;

    scanf("%d %d %d %d", &x, &y, &w, &h);

    int x_direction = x <= (w-x) ? x : (w-x);
    int y_direction = y <= (h-y) ? y : (h-y);

    int shortest_distance = x_direction <= y_direction ? x_direction : y_direction;

    printf("%d", shortest_distance);

    return 0;
}