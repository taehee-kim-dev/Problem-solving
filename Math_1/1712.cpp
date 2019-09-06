#include <iostream>

using namespace std;

int main_1712(void){

    int a, b, c;

    cin>>a;
    cin>>b;
    cin>>c;

    if(c-b<=0){
        cout<<-1;
        return 0;
    }

    double p = double(a)/double(c-b);
    cout<<int(p)+1;

    return 0;
}