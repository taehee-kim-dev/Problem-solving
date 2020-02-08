#include <cstdio>

// start

#include <string>
#include <vector>

using namespace std;


// Combination
int fact(int n); 
  
int nCr(int n, int r) 
{ 
    return fact(n) / (fact(r) * fact(n - r)); 
} 
  
// Returns factorial of n 
int fact(int n) 
{ 
    int res = 1; 
    for (int i = 2; i <= n; i++) 
        res = res * i; 
    return res; 
} 


int solution(vector<string> user_id, vector<string> banned_id) {
    int answer = 0;

    // banned id의 case 하나씩만 저장할 vector
    vector<string> banned_cases;
    // 각 case에 중복되는 형태의 banned_id의 갯수를 저장할 vector
    vector<int> banned_duplicated_count;
    // 각 case에 해당하는 user_id의 갯수를 저장할 vector
    vector<int> banned_user_ids_count;
    // 각 case에 해당하는 user_id를 갯수를 저장할 vector
    vector<vector<string>> banned_user_ids;

    // 제제 아이디 모두를 검사하는데,
    for(int i=0; i<banned_id.size(); i++){
        // 중복되는 유형의 제제 아이디 갯수
        int count=0;
        // 현재 검사하고있는 banned_id가 ""이 아니라면,
        // 검사할 임시 string 객체를 선언해 초기화하고
        if(banned_id[i].compare("")==0){
            continue;
        }
        string to_check=banned_id[i];
        // banned_cases에 해당 case를 추가한다
        banned_cases.push_back(to_check);
        // 검사 대상 string 객체 다음 객체부터 비교한다
        for(int j=i+1; j<banned_id.size(); j++){
            // 만약, 중복되는 유형의 제제 아이디가 있으면,
            if(to_check.compare(banned_id[j])==0){
                // 중복 갯수를 증가시키고,
                count++;
                // 중복된 case를 ""로 만든다
                banned_id[j]="";
            }
        }
        // 해당 검사 케이스에 중복된 케이스가 몇개인지를 banned_duplicated_count에 저장한다
        banned_duplicated_count.push_back(count+1);
        count=0;
    }

    // 제제 아이디 케이스에 해당하는 아이디들의 갯수 세기
    // 모든 제제 아이디 케이스들에 대하여 검사
    for(int i=0; i<banned_cases.size(); i++){
        // 해당 제제 아이디 케이스에 해당하는 유저 아이디 갯수 세기 변수
        int count=0;
        // 모든 유저 아이디에 대해 검사하는데,
        vector<string> tmp_str;
        for(int j=0; j<user_id.size(); j++){
            // 해당 유저 아이디가 제제 아이디 케이스에 해당하는지 여부
            bool check=true;
            // 만약 문자열의 길이가 다르면 검사할 필요 없이 건너뛴다
            if(banned_cases[i].length() != user_id[j].length())continue;

            // 문자열의 길이가 같다면,
            // '*'문자는 건너뛰고 나머지가 일치하는지 검사
            for(int k=0; k<user_id[j].length(); k++){
                if(banned_cases[i].at(k)=='*')continue;
                if(banned_cases[i].at(k)!=user_id[j].at(k))check=false;
            }
            // 만약 검사한 유저 아이디가 현재 제제 아이디 케이스에 해당한다면,
            if(check==true){
                // 해당 케이스의 제제 의심 아이디 목록에 추가
                tmp_str.push_back(user_id[j]);
                // count 증가
                count++;
            }
        }
        // 해당 제제 케이스에 해당하는 유저 아이디의 갯수 저장
        banned_user_ids_count.push_back(count);
        banned_user_ids.push_back(tmp_str);
    }


    for(int i=0; i<banned_duplicated_count.size(); i++){
        answer += nCr(banned_user_ids_count[i], banned_duplicated_count[i]);
    }







    return answer;
}

// end

int main(void){

    vector<string> user_id_1= {"frodo", "fradi", "crodo", "abc123", "frodoc"};
    vector<string> user_id_2= {"frodo", "fradi", "crodo", "abc123", "frodoc"};
    vector<string> user_id_3= {"frodo", "fradi", "crodo", "abc123", "frodoc"};

    vector<string> banned_id_1= {"fr*d*", "abc1**"};
    vector<string> banned_id_2= {"*rodo", "*rodo", "******"};
    vector<string> banned_id_3= {"fr*d*", "*rodo", "******", "******"};

    solution(user_id_3, banned_id_3);

    // printf("%d %d %d", 
    //     solution(user_id_1, banned_id_1),
    //     solution(user_id_2, banned_id_2),
    //     solution(user_id_3, banned_id_3)
    //     );

    return 0;
}