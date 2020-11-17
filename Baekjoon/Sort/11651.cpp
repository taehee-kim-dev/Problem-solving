#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

bool y_first_compare(const pair<int, int> &a, const pair<int, int> &b){
    if(a.second==b.second){
        return a.first<b.first;
    }else{
        return a.second<b.second;
    }
}

int main(void){

    int N;
    scanf("%d", &N);

    vector<pair<int, int>> points;
    while(N--){
        int x, y;
        scanf("%d %d", &x, &y);

        points.push_back(make_pair(x, y));
    }

    sort(points.begin(), points.end(), y_first_compare);

    for(vector<pair<int, int>>::iterator iter=points.begin(); iter!=points.end(); iter++){
        printf("%d %d\n", (*iter).first, (*iter).second);
    }



    return 0;
}