#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>

using namespace std;

int main_2908(void){

    int a, b;

    cin>>a>>b;

    string str_a=to_string(a);
    string str_b=to_string(b);

    reverse(str_a.begin(), str_a.end());
    reverse(str_b.begin(), str_b.end());

    a=atoi(str_a.c_str());
    b=atoi(str_b.c_str());


    if(a>b){
        cout<<a;
    }else{
        cout<<b;
    }

    return 0;
}