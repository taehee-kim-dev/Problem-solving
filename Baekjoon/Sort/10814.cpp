#include <cstdio>
#include <iostream>
#include <tuple>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

bool compare(tuple<int, int, string> &a, tuple<int, int, string> &b){
    if(get<1>(a) != get<1>(b)){
        return get<1>(a) < get<1>(b);
    }else{
        return get<0>(a) < get<0>(b);
    }
}

int main(void){

    int N;
    scanf("%d", &N);

    vector<tuple<int, int, string>> members; 

    int signup_order=0;
    while(N--){
        int age;
        string name;
        scanf("%d", &age);
        cin>>name;
        members.push_back(make_tuple(signup_order++, age, name));
    }

    sort(members.begin(), members.end(), compare);

    for(vector<tuple<int, int, string>>::iterator iter=members.begin(); iter!=members.end(); iter++){
        printf("%d ", get<1>(*iter));
        cout<<get<2>(*iter);
        printf("\n");
    }

    return 0;
}