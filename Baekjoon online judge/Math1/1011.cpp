#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int main_1011(void){

    long long t, x, y;

    cin>>t;

    vector<pair<long long, long long>> v;

    for(int i=0;i<t;i++){
        cin>>x>>y;
        v.push_back(make_pair(x, y));
    }


    for(int i=0;i<v.size();i++){
        long long dist=v[i].second-v[i].first;
        for(long long a=1;a<46342;a++){
            if(a*a-a<dist&&dist<=a*a){
                cout<<2*a-1;
                break;
            }else if(a*a<dist&&dist<=a*a+a){
                cout<<2*a;
                break;
            }
        }
        if(i<v.size()-1)
            cout<<endl;
    }

    return 0;
}