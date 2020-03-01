#include <iostream>

#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;

    for(int n = 0; n < commands.size(); n++){
        
        // commands에서 i, j, k 차례로 꺼냄.
        int i = commands[n][0], 
            j = commands[n][1], 
            k = commands[n][2];

        cout<<"i = "<<i<<", j = "<<j<<", k = "<<k<<"\n";

        // array의 i번째부터 j번째까지 잘라서 tmp vector에 할당.
        vector<int> tmp(array.begin() + i - 1, array.begin() + j);

        cout<<"tmp = ";
        for(int n = 0; n < tmp.size(); n++){
            cout<<tmp[n]<<" ";
        }
        cout<<"\n";

        // tmp vector 정렬.
        sort(tmp.begin(), tmp.end());

        cout<<"sorted!!\n";
        cout<<"tmp = ";
        for(int n = 0; n < tmp.size(); n++){
            cout<<tmp[n]<<" ";
        }
        cout<<"\n";

        // answer vector에 tmp vector의 k번째 원소 push_back.
        answer.push_back(tmp[k - 1]);

        cout<<"answer = ";
        for(int n = 0; n < answer.size(); n++){
            cout<<answer[n]<<" ";
        }

        cout<<"\n";
    }

    return answer;
}

int main(void){
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    
    vector<int> array{1, 5, 2, 6, 3, 7, 4};
    vector<vector<int>> commands{{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};
    vector<int> answer = solution(array, commands);

    cout<<"Final answer = ";
    for(int n = 0; n < answer.size(); n++){
        cout<<answer[n]<<" ";
    }

    return 0;
}