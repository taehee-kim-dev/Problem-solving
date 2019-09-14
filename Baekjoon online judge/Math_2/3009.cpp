#include <cstdio>
#include <set>

using namespace std;

int main(void){

    set<int> x_set;
    set<int> y_set;

    for(int i=0;i<3;i++){
        int x, y;
        scanf("%d %d", &x, &y);
        if(x_set.count(x)==0){
            x_set.insert(x);
        }else{
            x_set.erase(x);
        }

        if(y_set.count(y)==0){
            y_set.insert(y);
        }else{
            y_set.erase(y);
        }
    }

    printf("%d %d\n", *(x_set.begin()), *(y_set.begin()));



    return 0;
}