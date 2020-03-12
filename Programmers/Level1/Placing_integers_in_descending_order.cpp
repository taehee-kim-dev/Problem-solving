#include <string>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

long long solution(long long n) {
    long long answer = 0;

    vector<int> num_vec;

    string num_str = to_string(n);

    for(int i = 0; i < num_str.length(); i++){
        num_vec.push_back(num_str[i] - '0');
    }

    sort(num_vec.begin(), num_vec.end(), greater<int>());

    for(int i = 0; i < num_vec.size(); i++){
        answer *= 10;
        answer += num_vec[i];
    }

    return answer;
}