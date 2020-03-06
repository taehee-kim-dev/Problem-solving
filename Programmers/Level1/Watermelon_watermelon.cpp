#include <string>
#include <vector>

using namespace std;

string solution(int n) {
    string answer = "";

    bool toggle = true;

    for(int i = 0; i < n; i++){
        if(toggle == true){
            answer += "수";
            toggle = false;
        }else{
            answer += "박";
            toggle = true;
        }
    }

    return answer;
}