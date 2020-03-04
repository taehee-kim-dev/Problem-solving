#include <iostream>



#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
    long long answer = 0;

    if(a == b)
        return a;
    
    int small = a < b ? a : b;
    int large = a > b ? a : b;

    for(int i = small; i <= large; i++){
        answer += i;
    }

    return answer;
}



int main(void){
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    
    int a = 5, b = 3;
    int answer = solution(a, b);
    cout<<answer;

    return 0;
}