#include <cstdio>

int main_2969(void){

    int a, b, v;
    scanf("%d %d %d", &a, &b, &v);

    if((v-a)%(a-b)==0){
        printf("%d", int((v-a)/(a-b))+1);
    }else{
        printf("%d", int((v-a)/(a-b))+2);
    }

    return 0;
}