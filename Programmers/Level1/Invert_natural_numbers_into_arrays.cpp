#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(long long n) {
    vector<int> answer;

    string numbers_str = to_string(n);

    for(int i = 0; i < numbers_str.length(); i++){
        answer.push_back(numbers_str[i] - '0');
    }

    reverse(answer.begin(), answer.end());

    return answer;
}