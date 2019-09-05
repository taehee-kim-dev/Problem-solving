#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main_2941(void){

    vector<string> alpha_vec;

    alpha_vec.push_back("dz=");
    alpha_vec.push_back("c=");
    alpha_vec.push_back("c-");
    alpha_vec.push_back("d-");
    alpha_vec.push_back("lj");
    alpha_vec.push_back("nj");
    alpha_vec.push_back("s=");
    alpha_vec.push_back("z=");

    string input_str;

    cin>>input_str;

    int alpha_count=0;

    for(int i=0;i<alpha_vec.size();i++){

        int find_index = input_str.find(alpha_vec[i]);

        while(find_index!=string::npos){
            if(i==0){
                input_str.replace(find_index, 3, "FFF");
                alpha_count++;
            }else{
                input_str.replace(find_index, 2, "FF");
                alpha_count++;
            }
            find_index = input_str.find(alpha_vec[i]);
        }

    }

    int extra_count=0;

    for(int i=0;i<input_str.size();i++){
        if(input_str[i]!='F'){
            extra_count++;
        }
    }

    cout<<alpha_count+extra_count;

    return 0;
}