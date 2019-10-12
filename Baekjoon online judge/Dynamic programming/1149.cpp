#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){

    vector<vector<int>> total_color_costs;

    vector<int> zero_house(3, 0);
    total_color_costs.push_back(zero_house);

    int N;
    scanf("%d", &N);
    int total_house_num = N;

    while(N--){
        int r, g, b;
        scanf("%d %d %d", &r, &g, &b);
        vector<int> color_costs_per_one_house;
        color_costs_per_one_house.push_back(r);
        color_costs_per_one_house.push_back(g);
        color_costs_per_one_house.push_back(b);
        total_color_costs.push_back(color_costs_per_one_house);
    }

    for(int i=2; i<=total_house_num; i++){
        total_color_costs[i][0] = min(total_color_costs[i-1][1], total_color_costs[i-1][2]) + total_color_costs[i][0];
        total_color_costs[i][1] = min(total_color_costs[i-1][0], total_color_costs[i-1][2]) + total_color_costs[i][1];
        total_color_costs[i][2] = min(total_color_costs[i-1][0], total_color_costs[i-1][1]) + total_color_costs[i][2];
    }

    printf("%d", *min_element(total_color_costs[total_house_num].begin(), total_color_costs[total_house_num].end()));

    return 0;
}