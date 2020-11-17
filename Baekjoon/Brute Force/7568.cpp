#include <cstdio>
#include <vector>
#include <utility>

using namespace std;

int main(void){

    int N;
    scanf("%d", &N);

    vector<pair<int, int>> human;

    while(N--){
        int weight, height;
        scanf("%d %d", &weight, &height);
        human.push_back(make_pair(weight, height));
    }

    for(int i=0;i<human.size();i++){
        int larger_count=0;
        int current_weight=human[i].first;
        int current_height=human[i].second;
        for(int j=0;j<human.size();j++){
            if(human[j].first>current_weight && human[j].second>current_height){
                larger_count++;
            }
        }
        printf("%d ", larger_count+1);
    }

    return 0;
}