#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string A, B;

int result = 50; // A와 B의 차이 최소값

void solve(){
    for(int i = 0; i <= B.length() - A.length(); i++){
        int count = 0;
        for(int j = 0; j < A.length(); j++){
            if(A[j] != B[i + j])
                count++;
        }
        result = min(result, count);
    }

    cout<<result;
}

void input(){
    cin>>A>>B;
}

int main(void){
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    input();
    solve();

    return 0;
}