#include <string>
#include <vector>

using namespace std;

int solution(int num) {
    int count = 0;

    long long long_num = (long long)num;

    while(long_num != 1){

        if(count == 500){
            return -1;
        }

        if(long_num % 2 == 0){
            long_num /= 2;
        }else{
            long_num *= 3;
            long_num += 1;
        }

        count++;

    }

    return count;
}