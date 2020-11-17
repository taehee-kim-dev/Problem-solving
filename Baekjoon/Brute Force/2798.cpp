#include <cstdio>
#include <vector>
#include <set>

using namespace std;

int main(void){

    int N, M;
    scanf("%d %d", &N, &M);

    vector<int> cards;

    for(int i=0;i<N;i++){
        int card;
        scanf("%d", &card);
        cards.push_back(card);
    }

    set<int> sum_numbers;

    for(int i=0;i<N-2;i++){
        for(int j=i+1;j<N-1;j++){
            for(int k=j+1;k<N;k++){
            
            int sum = cards[i]+cards[j]+cards[k];
            if(sum_numbers.find(sum)==sum_numbers.end()){
                sum_numbers.insert(sum);
            }
        }
    }
    }

    int diff=300000;
    int result=0;
    for(set<int>::iterator iter=sum_numbers.begin(); iter!=sum_numbers.end(); iter++){
        if(*iter<=M && diff>M-*iter){
            result = *iter;
        }
    }

    printf("%d", result);

    return 0;
}