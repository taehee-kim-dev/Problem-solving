#include <vector>

using namespace std;

int get_gcd(int n, int m){
    
    int r;

    while(m){
        r = n % m;
        n = m;
        m = r;
    }

    return n;

}

int get_lcm(int n, int m){

    return n * m / get_gcd(n, m);
}

vector<int> solution(int n, int m) {
    vector<int> answer;

    answer.push_back(get_gcd(n, m));
    answer.push_back(get_lcm(n, m));

    return answer;
}