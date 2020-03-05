#include <string>

using namespace std;

bool solution(string s) {

    if(!(s.length() == 4 || s.length() == 6))
        return false;
    
    for(int i = 0; i < s.length(); i ++){
        if(!('0' <= s[i] && s[i] <= '9'))
            return false;
    }

    return true;
}