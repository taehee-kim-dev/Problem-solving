#include <iostream>

using namespace std;

int main_2292(void){

    int n;
    cin>>n;

    if(n==1){
        cout<<1;
        return 0;
    }

    int check = 2;
    int i=0;

    while(check<=n){
        i++;
        check+=6*i;
    }

    cout<<i+1;

    return 0;
}