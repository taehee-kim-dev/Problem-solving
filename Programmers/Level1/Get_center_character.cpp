#include <iostream>

#include <string>

using namespace std;

string solution(string s) {
    string answer = "";

    bool is_odd;

    if(s.length() % 2 == 0)
        is_odd = false;
    else
        is_odd = true;

    if(is_odd){
        answer = s[s.length() / 2];
    }else{
        answer += s[(s.length() / 2) - 1];
        answer += s[s.length() / 2];
    }

    return answer;
}

int main(void){
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    
    cout<<solution("abcde")<<"\n";
    cout<<solution("qwer");

    return 0;
}