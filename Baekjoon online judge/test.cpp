#include <cstdio>

using namespace std;

int gcd(int a, int b){
    while(b!=0){
        int r=a%b;
        a=b;
        b=r;
    }
    return a;
}

int lcm(int a, int b){
    return a*b/gcd(a, b);
}

int main(void){

    for(int m=1;m<100;m++){
        for(int n=1;n<100;n++){
            for(int x=1;x<=m;x++){
                for(int y=1;y<=n;y++){
                    int max = lcm(m, n);

                    int i=0;
                    while(x+i*m<=max){
                        int check_y = (x+i*m)%n;
                        if(check_y==0 && y!=n){
                            printf("M=%d, N=%d, x=%d, y=%d, year=%d\n", m, n, x, y, x+i*m);
                            break;
                        }else{
                            i++;
                        }

                    }
                }
            }
        }
    }

    return 0;
}