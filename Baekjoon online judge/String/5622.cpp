#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main_5622(void){

    string input_str;

    cin>>input_str;

    int total_sec=0;

    for(int i=0;i<int(input_str.length());i++){
        switch (input_str[i])
        {
        case 'A':
        case 'B':
        case 'C':
            total_sec+=3;
            break;
        case 'D':
        case 'E':
        case 'F':
            total_sec+=4;
            break;
        case 'G':
        case 'H':
        case 'I':
            total_sec+=5;
            break;
        case 'J':
        case 'K':
        case 'L':
            total_sec+=6;
            break;
        case 'M':
        case 'N':
        case 'O':
            total_sec+=7;
            break;
        case 'P':
        case 'Q':
        case 'R':
        case 'S':
            total_sec+=8;
            break;
        case 'T':
        case 'U':
        case 'V':
            total_sec+=9;
            break;
        case 'W':
        case 'X':
        case 'Y':
        case 'Z':
            total_sec+=10;
            break;
        }
    }

    cout<<total_sec;

    return 0;
}