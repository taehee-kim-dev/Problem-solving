#include <cstdio>
#include <iostream>
#include <string>
#include <set>
#include <algorithm>


using namespace std;

struct word_compare{
    bool operator() (const string &a, const string &b){
    if(a.length() == b.length()){
        if(a.compare(b)<0){
            return true;
        }else{
            return false;
        }
    }else{
        return a.length() < b.length();
    }
}
};

int main(void){

    int N;
    scanf("%d", &N);

    set<string, word_compare> words;

    while(N--){
        string word;
        cin>>word;
        words.insert(word);
    }

    for(set<string>::iterator iter=words.begin(); iter!=words.end(); iter++){
        cout<<*iter<<endl;
    }

    return 0;
}