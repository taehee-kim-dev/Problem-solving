#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

bool isPrime(int n){
    if(n==1)
        return false;
    
    for(int i=2;i<=(n/2);i++){
        if(n%i==0)
            return false;
    }

    return true;
}

int main(void){

    int N;

    scanf("%d", &N);
    
    vector<int> numbers;
    while(N--){
        int input_num;
        scanf("%d", &input_num);
        numbers.push_back(input_num);
    }

    int prime_count=0;

    for(int i=0;i<numbers.size();i++){
        if(isPrime(numbers[i]))
            prime_count++;
    }
    
    printf("%d", prime_count);

    return 0;
}