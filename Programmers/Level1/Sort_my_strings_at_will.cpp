#include <iostream>



#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int N;

bool compare(string a, string b){
    
    if(a[N] != b[N])
        return a[N] < b[N];
    else{
        return a < b;
    }
}

vector<string> solution(vector<string> strings, int n) {

    N = n;

    sort(strings.begin(), strings.end(), compare);

    return strings;
}



int main(void){
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    
    vector<string> strings{"abce", "abcd", "cdx"};
    int n = 2;

    vector<string> answer = solution(strings, n);

    for(int i = 0; i < answer.size(); i++){
        cout<<answer[i]<<" ";
    }

    return 0;
}