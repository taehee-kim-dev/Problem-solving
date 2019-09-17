#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main(void){

    int N;
    scanf("%d", &N);
            
    for(int i=1;i<=N;i++){
        string i_str = to_string(i);
        int sum=i;
        for(int j=0;j<i_str.length();j++){
            sum+=(i_str[j]-int('0'));
        }
        if(sum==N){
            printf("%d", i);
            return 0;
        }

    }
    printf("%d", 0);
    return 0;
}