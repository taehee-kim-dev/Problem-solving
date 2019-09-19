#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main(void){

    vector<vector<char>> black_first_correct = {{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                                                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                                                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                                                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                                                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                                                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                                                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                                                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'}};

    vector<vector<char>> white_first_correct = {{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                                                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                                                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                                                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                                                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                                                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                                                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                                                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'}};

    int N, M;

    scanf("%d %d", &N, &M);

    vector<vector<char>> board(N, vector<char>(M, 'N'));

    for(int n=0;n<N;n++){
        cin.ignore(1);
        for(int m=0;m<M;m++){
            char color;
            scanf("%c", &color);
            board[n][m]=color;
        }
    }

    int min=100;
    for(int n=0;n<N-8+1;n++){
        for(int m=0;m<M-8+1;m++){
        
            int count=0;

            for(int r=n;r<n+8;r++){
                for(int c=m;c<m+8;c++){

                    if(board[n][m]=='W'){
                        if(board[r][c]!=white_first_correct[r-n][c-m]){
                            count++;
                            printf("r=%d, c=%d, r-n=%d, c-m=%d, board=%c, answer=%c //", r, c, r-n, c-m, board[r][c], white_first_correct[r-n][c-m]);
                        }
                    }else if(board[n][m]=='B'){
                        if(board[r][c]!=black_first_correct[r-n][c-m]){
                            count++;
                            printf("r=%d, c=%d, r-n=%d, c-m=%d, board=%c, answer=%c //", r, c, r-n, c-m, board[r][c], black_first_correct[r-n][c-m]);
                        }
                    }
                }
                printf("\n");
            }

            printf("\n");

            if(count<min){
                min=count;
            }
        }
        printf("\n");
    }

    printf("%d", min);
    

    return 0;
}