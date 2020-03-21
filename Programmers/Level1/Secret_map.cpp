#include <string>
#include <vector>
#include <bitset>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;

    // 각 지도의 문자열값을 담을 벡터
    vector<string> arr1_bit_str_vec;
    vector<string> arr2_bit_str_vec;

    for(int i = 0; i < n; i++){
        // 각 지도의 정수값들을 모두 이진수형태의 문자열로 변경
        // 비트수 인자는 상수이므로, 최대값으로 설정.
        string str_tmp = bitset<16>(arr1[i]).to_string();
        // 맨 뒤의 n개의 값만 자름.
        str_tmp = str_tmp.substr(str_tmp.size()-n);

        // 해당 문자열의 값에서 1의값은 #으로, 0의값은 " "로 변경
        for(int j = 0; j < n; j++){
            if(str_tmp[j] == '1'){
                str_tmp[j] = '#';
            }else{
                str_tmp[j] = ' ';
            }
        }

        arr1_bit_str_vec.push_back(str_tmp);
    }

    // arr2에 대해 같은 과정 반복.
    for(int i = 0; i < n; i++){
        string str_tmp = bitset<16>(arr2[i]).to_string();
        str_tmp = str_tmp.substr(str_tmp.size()-n);

        for(int j = 0; j < n; j++){
            if(str_tmp[j] == '1'){
                str_tmp[j] = '#';
            }else{
                str_tmp[j] = ' ';
            }
        }

        arr2_bit_str_vec.push_back(str_tmp);
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(arr1_bit_str_vec[i][j] == '#')
                arr2_bit_str_vec[i][j] = '#';
        }
    }


    return arr2_bit_str_vec;
}