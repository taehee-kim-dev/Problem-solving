#include <string>
#include <vector>

using namespace std;

bool solution(int x) {

    int sum_of_digits = 0;

    string x_to_str = to_string(x);

    for(int i = 0; i < x_to_str.length(); i++){
        sum_of_digits += x_to_str[i] - '0';
    }

    return x % sum_of_digits == 0 ? true : false;
}