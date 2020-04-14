#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(string s) {
    int answer = 0;

    // 압축된 문자열들의 길이
    vector<int> compressed_str_lengths_vec;


    for(int str_len = 1; str_len <= s.length(); str_len++){
        
        // 압축할 기준 문자열
        // 첫번째로 자른 문자열로
        string standard_str_to_compress =  s.substr(0, str_len);;

        // 현재까지 압축된 문자열
        string current_compressed_str = "";

        // 압축된 횟수
        int count_compression = 1;

        // 자를 문자열의 길이는 1개부터 문자열 전체의 길이 까지
        // 맨 앞부터 순서대로 자를 문자열의 길이만큼씩 검사하며,
        
        // 직후에 나오는 문자열이 직전에 나온 문자열과 다르다면,
        // 압축이 이어지지 않는 것이므로,
        // 직전까지 압축된 문자열 = 직전까지 압축된 횟수(1이면 생략) + 압축 기준 문자열
        // 이 된다.
        // 이 문자열을 만들어서, 이 문자열의 길이를 정답에 추가한다.
        // 그리고, 현재 검사한 문자열을 압축 기준 문자열로 초기화한다.
        // 압축 횟수도 1로 초기화한다.

        // 직후에 나오는 문자열이 직전에 나온 문자열과 같다면,
        // 압축이 가능한 것이므로 압축된 횟수를 1 증가하고,
        // 다음 문자열을 검사한다.

        for(int char_index = str_len; char_index < s.length(); char_index += str_len){

            // 현재 자를 길이만큼 앞에서부터 차례대로 자름.
            // 전체 문자열의 끝을 넘어간다면, 자동으로 전체 문자열의 끝까지만 자름.
            string current_str = s.substr(char_index, str_len);

            // 현재 자른 문자열이 마지막 문자열인가?
            bool is_final = false;

            // 마지막으로 잘리는 문자열인지 검사
            if(char_index + str_len - 1 >= s.length() - 1)
                is_final = true;

            // 압축 기준 문자열과 비교
            if(standard_str_to_compress == current_str){
                // 같다면 압축 가능
                count_compression++;
                // 압축 기준 문자열 유지
            }else{
                // 다르다면 압축이 이어지지 않음.

                // 압축 횟수 정수값을 문자열로 변환해서 저장할 변수
                string compression_count_str = "";
                
                // 압축 횟수 검사
                if(count_compression > 1){
                    // 압축된 횟수가 1보다 크다면,
                    compression_count_str = to_string(count_compression);
                    // 압축된 갯수를 압축한 문자열 앞에 추가해야 함.
                }
                // 압축된 횟수가 1이라면, 빈 문자열이므로 그대로 놔둠.

                // 직전까지 압축된 문자열 = 직전까지 압축된 횟수(1이면 생략) + 압축 기준 문자열의 길이
                // 현재까지 압축된 문자열에 직전까지 압축된 문자열을 추가.
                current_compressed_str +=  compression_count_str + standard_str_to_compress;
                
                // 초기화
                count_compression = 1;
                standard_str_to_compress = current_str;

            }

            // 마지막 문자열이라면,
            if(is_final){
                // 압축 횟수 정수값을 문자열로 변환해서 저장할 변수
                string compression_count_str = "";
                
                // 압축 횟수 검사
                if(count_compression > 1){
                    // 압축된 횟수가 1보다 크다면,
                    compression_count_str = to_string(count_compression);
                    // 압축된 갯수를 압축한 문자열 앞에 추가해야 함.
                }
                // 압축된 횟수가 1이라면, 빈 문자열이므로 그대로 놔둠.

                // 직전까지 압축된 문자열 = 직전까지 압축된 횟수(1이면 생략) + 압축 기준 문자열의 길이
                // 현재까지 압축된 문자열에 직전까지 압축된 문자열을 추가.
                current_compressed_str +=  compression_count_str + standard_str_to_compress;
            }
        }

        if(str_len == s.length()){
            current_compressed_str = standard_str_to_compress;
        }

        // 해당 문자열 길이로 모두 압축함.
        // 압축길이단위별 압축된 문자열 길이 저장 벡터에 push_back
        compressed_str_lengths_vec.push_back(current_compressed_str.length());
        // 압축할 기준 문자열
        standard_str_to_compress = "";

        // 현재까지 압축된 문자열
        current_compressed_str = "";

        // 압축된 횟수
        count_compression = 1;

    }

    // 최소 길이 저장.
    answer = *min_element(compressed_str_lengths_vec.begin(), compressed_str_lengths_vec.end());
    
    return answer;
}