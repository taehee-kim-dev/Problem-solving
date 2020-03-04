#include <iostream>

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr, int divisor) {
    vector<int> answer;

    for(int i = 0; i < arr.size(); i++){
        if(arr[i] % divisor == 0){
            answer.push_back(arr[i]);
        }
    }

    if(answer.empty()){
        answer.push_back(-1);
    }else{
         sort(answer.begin(), answer.end());
    }

    return answer;
}

int main(void){
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);

    vector<int> arr{3,2,6};
    int divisor = 10;
    
    vector<int> answer = solution(arr, divisor);

    for(int i = 0; i < answer.size(); i++){
        cout<<answer[i]<<" ";
    }

    return 0;
}