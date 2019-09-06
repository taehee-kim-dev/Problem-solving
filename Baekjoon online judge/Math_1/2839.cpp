#include <iostream>

using namespace std;

int main_2839(void){

    int n;

    cin>>n;

    int i = n/5;
    int j=0;

    while((5*i)+(3*j)!=n){
        while((5*i)+(3*j)<=n){
            j++;
            if((5*i)+(3*j)==n)
                break;
        }
        if((5*i)+(3*j)==n)
                break;
        i--;
        if(i<0)
            break;
    }

    if(i<0)
        cout<<-1;
    else
        cout<<i+j;

    return 0;
}