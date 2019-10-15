#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){

    vector<int> scores_of_stairs(1, 0);
    vector<int> scores_of_stairs_accumulated;

    int n;
    scanf("%d", &n);

    for(int i=0; i<n; i++){
        int score_per_one_stair;
        scanf("%d", &score_per_one_stair);

        scores_of_stairs.push_back(score_per_one_stair);
    }

    scores_of_stairs_accumulated.assign(scores_of_stairs.begin(), scores_of_stairs.end());

    scores_of_stairs_accumulated[2] += scores_of_stairs[1];

    for(int i=3; i<=n; i++){
        scores_of_stairs_accumulated[i] += max(scores_of_stairs_accumulated[i-3]+scores_of_stairs[i-1], scores_of_stairs_accumulated[i-2]);

    }

    printf("%d", scores_of_stairs_accumulated[n]);

    return 0;
}