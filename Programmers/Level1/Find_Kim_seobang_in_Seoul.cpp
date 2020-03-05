#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> seoul) {
    string answer = "김서방은 ";

    answer += to_string(distance(seoul.begin(), find(seoul.begin(), seoul.end(), "Kim")));

    return answer + "에 있다";
}