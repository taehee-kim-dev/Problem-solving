#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){

    int N;

    scanf("%d", &N);

    bool flag = false;

    vector<int> A_left_vec;
    vector<int> A_right_vec;

    int T=N;

    while(T--){
        int A_input;
        scanf("%d", &A_input);

        if(A_input==-1){
            flag=true;
            continue;
        }

        if(flag==false){
            A_left_vec.push_back(A_input);
        }else{
            A_right_vec.push_back(A_input);
        }
    }

    sort(A_left_vec.begin(), A_left_vec.end());
    sort(A_right_vec.begin(), A_right_vec.end());

    printf("%d", A_left_vec[0]+A_right_vec[0]);

    return 0;
}