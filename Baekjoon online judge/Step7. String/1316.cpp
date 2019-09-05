#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main_1316(void){

    int n;

    cin>>n;

    vector<string> str_vec;

    for(int i=0;i<n;i++){
        string input_str;
        cin>>input_str;
        str_vec.push_back(input_str);
    }

    int count_group_word=0;

    for(int i=0;i<str_vec.size();i++){
        bool is_group = true;
        string str_to_check = str_vec[i];

        int index_to_start_check = 0;
        char target = str_to_check[index_to_start_check++];

        while(index_to_start_check<str_to_check.length()){
            while(str_to_check[index_to_start_check]==target && index_to_start_check<str_to_check.length()){
            index_to_start_check++;
            }

            if(index_to_start_check == str_to_check.length()){
                break;
            }
            else if(str_to_check.find(target, index_to_start_check)!=string::npos){
                is_group=false;
                break;
            }
            else if(str_to_check.find(target, index_to_start_check)==string::npos){
                target = str_to_check[index_to_start_check++];
            }
        }
        if(is_group==true){
            count_group_word++;
        }
    }

    cout<<count_group_word;

    return 0;
}