#include <cstdio>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){

    int N;
    scanf("%d", &N);

    vector<pair<int, int>> points;

    for(int i=0; i<N; i++){
        int x, y;
        scanf("%d %d", &x, &y);
        points.push_back(make_pair(x, y));
    }

    sort(points.begin(), points.end());

    for(vector<pair<int, int>>::iterator iter=points.begin(); iter!=points.end(); iter++){
        printf("%d %d\n", (*iter).first, (*iter).second);
    }

    return 0;
}