#include <cstdio>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

int main(void){

    vector<string> result;

    while(true){
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);

        if(a==0&&b==0&&c==0){
            break;
        }

        int tmp;
        if(a>b){
            tmp=a;
            a=b;
            b=tmp;
        }
        if(b>c){
            tmp=b;
            b=c;
            c=tmp;
        }

        if(a*a+b*b==c*c){
            result.push_back("right");
        }else{
            result.push_back("wrong");
        }
    }

    vector<string>::iterator iter;
    for(iter=result.begin();iter!=result.end();iter++){
        printf("%s\n", iter->c_str());
    }

    return 0;
}