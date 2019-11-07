#include <cstdio>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

int main(void){

    string a, b;

    cin>>a>>b;

    int a_length = a.length();
    int b_length = b.length();

    vector<vector<int>> dp(a_length+1, vector<int>(b_length+1, 0));

    for(int i=0; i<a_length; i++){
        for(int j=0; j<b_length; j++){
            if(a[i]==b[j])
                dp[i+1][j+1] = dp[i][j]+1;
            else{
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j]);
            }
        }
    }

    printf("%d", dp[a_length][b_length]);

    return 0;
}