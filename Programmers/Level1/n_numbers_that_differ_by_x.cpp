#include <string>
#include <vector>

using namespace std;

vector<long long> solution(int x, int n) {
    vector<long long> answer;

    int diff = x;

    for(int i = 0; i < n; i++, x += diff){
        answer.push_back(x);
    }

    return answer;
}