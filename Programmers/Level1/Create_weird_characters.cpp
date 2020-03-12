#include <string>
#include <vector>

using namespace std;

// 짝수인덱스 -> 대문자
// 홀수인덱스 -> 소문자

string solution(string s) {

    string answer = "";


    // j는 단어의 인덱스
    // i는 문자열 전체의 인덱스
    for(int i = 0, j = 0; i < s.length(); i++, j++){

        // 만약 현재 검사하고 있는 문자가 공백이라면,
        if(s[i] == ' '){

            // answer에 공백문자 추가
            answer += ' ';

            // j를 -1로 초기화
            j = -1;

            continue;
        }

        // j가 짝수이면,
        if(j % 2 == 0){
            // 대문자로 바꿔서 answer에 추가.
            answer += toupper(s[i]);
        }else{
            // 홀수이면
            // 소문자로 바꿔서 answer에 추가.
            answer += tolower(s[i]);
        }
        
    }

    return answer;
}
