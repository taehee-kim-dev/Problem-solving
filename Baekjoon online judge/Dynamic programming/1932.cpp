#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){

    int n;
    scanf("%d", &n);

    vector<vector<int>> triangle;

    for(int row=1; row<=n; row++){
        vector<int> row_vec;
        for(int col=1; col<=row; col++){
            int input_num;
            scanf("%d", &input_num);
            row_vec.push_back(input_num);
        }
        triangle.push_back(row_vec);
    }

    for(int row=0; row<n; row++){
        for(int col=0; col<=row; col++){
            if(row==0&&col==0)continue;
            else if(row!=0&&col==0){
                triangle[row][col]+=triangle[row-1][col];
            }else if(col==row){
                triangle[row][col]+=triangle[row-1][col-1];
            }else{
                triangle[row][col]+=max(triangle[row-1][col-1], triangle[row-1][col]);
            }
        }
    }

    sort(triangle[n-1].begin(), triangle[n-1].end());

    printf("%d", triangle[n-1][n-1]);

    return 0;
}