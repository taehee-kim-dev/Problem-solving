#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;

int main(void){

    int T;
    scanf("%d", &T);

    vector<int> result;

    while(T--){
        int x1, y1, r1, x2, y2, r2;
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);

        double d=sqrt(pow(double(x1-x2), 2.0)+pow(double(y1-y2), 2.0));

        int rn = r1 < r2 ? r1 : r2;
        int rm = r1 > r2 ? r1 : r2;

        if(d > double(rn) + double(rm) || d + double(rn) < double(rm)){
            result.push_back(0);
        }else if(x1==x2 && y1==y2 && r1 == r2){
            result.push_back(-1);
        }else if(d+double(rn)==double(rm) || double(rn)+double(rm)==d){
            result.push_back(1);
        }else if(d+double(rn)>double(rm) && d<double(rn)+double(rm)){
            result.push_back(2);
        }

    }

    for(vector<int>::iterator iter=result.begin(); iter!=result.end(); iter++){
        printf("%d\n", *iter);
    }

    return 0;
}