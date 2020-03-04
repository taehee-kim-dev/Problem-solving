#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;

    // 직전 숫자 임시 저장
    int before = -1;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] != before){
            answer.push_back(arr[i]);
            before = arr[i];
        }
    }

    return answer;
}

int main(void){
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    
    vector<int> input{4,4,4,3,3};
    vector<int> answer = solution(input);
    for(int i = 0; i < answer.size(); i++){
        cout<<answer[i]<<" ";
    }

    return 0;
}