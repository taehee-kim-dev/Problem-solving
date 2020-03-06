#include <iostream>



#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {

    for(int i = 0; i < s.length(); i++){
        
        if(isupper(s[i])){
            if(s[i] + n > 'Z'){
                s[i] = 'A' - 1 + ((s[i] + n) % 'Z');
            }else{
                s[i] += n;
            }
        
        }else if(islower(s[i])){
            if(s[i] + n > 'z'){
                s[i] = 'a' - 1 + ((s[i] + n) % 'z');
            }else{
                s[i] += n;
            }
        }
    }

    return s;
}



int main(void){
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    
    solution();

    return 0;
}