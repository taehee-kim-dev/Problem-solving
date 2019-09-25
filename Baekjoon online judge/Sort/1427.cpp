#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

bool desc(char a, char b){
    return a>b;
}

int main(void){

    int N;

    scanf("%d", &N);

    string N_str = to_string(N);

    sort(N_str.begin(), N_str.end(), desc);

    cout<<N_str;

    return 0;
}