#include <iostream>
#include <string>

using namespace std;

int solution(int n)
{
    int answer = 0;

    // 숫자를 문자열로 변환
    string number_str = to_string(n);

    // 문자열의 각 자릿수를 다시 숫자로 변환하여 answer에 더함.
    for(int i = 0; i < number_str.length(); i++){
        answer += (number_str[i] - '0');
    }

    return answer;
}