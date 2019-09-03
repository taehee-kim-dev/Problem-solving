#include <iostream>
#include <string>
#include <cstring>


using namespace std;

int main_1154(void){

    char carray[1000000];

    cin.getline(carray, 1000000, '\n');

    char* p = strtok(carray, " ");

    int count=0;

    while(p!=NULL){
        p=strtok(NULL, " ");
        count++;
    }

    cout<<count;

    return 0;
}