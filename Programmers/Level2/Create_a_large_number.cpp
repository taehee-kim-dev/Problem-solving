#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string number, int k) {
    string answer = "";

    // 제거하고 남은 숫자의 길이
    int remaining_length_of_number = number.length() - k;

    // 이 길이 만큼의 숫자를 뽑아내야함.
    // 그 중에서 가장 큰 수 찾기.

    // 검사 시, 전체 숫자 중에서 첫 번째로 검사될 수 있는 인덱스
    int start_index = 0;

    // 첫 번째 자릿수부터 뽑아낼 전체 자릿수까지 차례대로 검사하며 찾기.
    for(int single_digit = 1; single_digit <= remaining_length_of_number; single_digit++){
        // single_digit 번 째 자릿수는, 전체 숫자에서 (뽑아낼 숫자의 길이 - single_digit) 만큼의 수를 뒤에 남겨놓아야 함.
        // [첫 번째로 검사될 수 있는 iterator, 전체 문자열의 마지막 iterator - (뽑아낼 숫자의 길이 - 현재 자릿수)] 중에서 최대값이
        // 현재 자릿수의 최대값의 iterator
        auto max_number_iter = max_element(number.begin() + start_index
            , number.end() - (remaining_length_of_number - single_digit));

        // 현재 자릿수의 최대값을 정답에 추가
        answer += *max_number_iter;

        // 다음 검사 시, 첫 번째로 검사될 수 있는 인덱스는 현재 선택된 숫자의 인덱스 다음부터임.
        start_index = max_number_iter - number.begin() + 1;

    }

    return answer;
}