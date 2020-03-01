#include <iostream>

#include <string>
#include <vector>

using namespace std;

// a월 b일은 무슨요일?
string solution(int a, int b) {
    string answer = "";
    vector<string> days_of_week{"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
    vector<int> days_of_month{0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    /*
        2016년 1월 1일은 금요일.
        2016년 a월 b일이 1월 1일부터 총 며칠 뒤인지 계산하여야 함.
    */

    int total_days = 0;
    for(int month = 1; month <= a-1; month++){
        total_days += days_of_month[month];
    }

    // 1월 1일부터 a월 b일 까지의 총 날짜 수
    total_days += b;

    // 여기에서 1을 빼면 2016년 a월 b일이 1월 1일부터 총 며칠 뒤인지에 대한 값.
    total_days -= 1;

    // 총 일수를 7일로 나눈 나머지를 구한다.
    
    int extra_days = total_days % 7;

    answer = days_of_week[extra_days];

    return answer;
}

int main(void){
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);


    cout<<solution(5, 24);

    return 0;
}