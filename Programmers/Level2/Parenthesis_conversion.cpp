#include <string>
#include <vector>
#include <stack>

using namespace std;

string solution(string input_str) {
    string answer = "";

    // v가 ""인 경우, "" 반환
    if(input_str == "")
        return input_str;

    // '(' 개수를 셀 변수
    int count_left_side_parenthesis = 0;
    // ')' 개수를 셀 변수
    int count_right_side_parenthesis = 0;

    // 위 두 변수의 값이 최초로 같을 때의 문자열(u)이
    // "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없는 "균형잡힌 괄호 문자열"이다.

    // 문자열의 문자를 하나씩 검사하는 인덱스
    // 잘라내는 문자열의 끝 인덱스가 된다.
    int char_check_index = -1;

    // 올바른 괄호 문자열인가?
    bool is_correct_str = true;

    // 괄호 짝 검사에 사용할 스택
    stack<char> parentheses_stack;

    // w -> u + v 분리
    // '('의 개수와 ')'의 개수가 최초로 같아지는 시점까지.
    // 즉, u를 구하기 위함.
    do{

        char_check_index++;

        // 문자열을 맨 앞의 문자부터 하나씩 검사하여 어떤 괄호인지 개수를 셈
        switch (input_str[char_check_index])
        {
        case '(':

            count_left_side_parenthesis++;

            // 아직 올바른 괄호 문자열임이 유지되고 있는 조건 하에,
            if(is_correct_str == true){
                // '(' 문자열이 나오면 스택에 push
                parentheses_stack.push('(');
            }

            break;
        case ')':

            count_right_side_parenthesis++;

            // 아직 올바른 괄호 문자열임이 유지되고 있는 조건 하에,
            if(is_correct_str == true){
                // 스택이 현재 비어있지 않다면 스택에 '('가 존재한다는 뜻이고,
                // 현재 짝인 ')'를 만났으므로 
                if(parentheses_stack.empty() == false){
                    // pop 해줌.
                    parentheses_stack.pop();
                }else{
                    // 스택이 비어있는데 ')'가 나오면 짝이 맞는 문자열이 아니므로
                    // 올바른 문자열인가에 대한 bool값을 false로 바꿈.
                    is_correct_str = false;
                }
            }

            break;
        }


    }while(count_left_side_parenthesis != count_right_side_parenthesis);
    
    // 두 종류 괄호의 개수가 최초로 같아질 때 while문을 나옴.
    // 즉, 문자열에서 char_check_index 이하 인덱스의 문자열은 u에 해당.

    // w -> u + v 분리
    string u = input_str.substr(0, char_check_index + 1);
    string v = "";
    
    // char_check_index가 마지막 인덱스가 아니라면
    if(char_check_index != input_str.length() - 1){
        // u 뒤의 문자열을 v에 할당.
        v = input_str.substr(char_check_index + 1);
    }

    // 만약 u가 "올바른 괄호 문자열"이라면,
    if(parentheses_stack.empty() && is_correct_str == true){
        // v에 대해서 재귀호출
        return u + solution(v);
    }else{

        // 아니라면,
        // u의 정답을 참조할 변수를 ""로 초기화 및 선언.
        string answer_u = "";
        // 맨 앞에 '('를 붙임.
        answer_u += '(';

        // v의 재귀 결과를 이어 붙임.
        answer_u += solution(v);

        answer_u += ')';

        // u의 첫번째 문자와 마지막 문자를 제거함.
        u = u.substr(1, u.length() - 2);
        // u의 괄호 방향을 뒤집어서 참조할 변수를 ""로 초기화 및 선언.
        string reverse_u_str = "";

        // u의 처음부터 끝까지 검사하면서
        for(int char_index = 0; char_index < u.length(); char_index++){
            // 괄호의 방향을 바꾸면서,
            // reverse_u_str에 이어붙임.
            switch (u[char_index])
            {
            case '(':
                reverse_u_str += ')';
                break;
            case ')':
                reverse_u_str += '(';
                break;
            }
        }
        answer_u += reverse_u_str;
        

        return answer_u;
    }
}