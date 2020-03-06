#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;

    bool is_positive = true;

    if(s[0] == '-')
        is_positive = false;

    if(isdigit(s[0]) == false)
        s = s.substr(1);

    answer = stoi(s);

    if(is_positive == false)
        answer *= -1;

    return answer;
}