#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> stock_prices_vec) {
    vector<int> stock_price_retention_time_vec;

    // 맨 앞 시점부터 검사
    for(int stock_price_index1 = 0; stock_price_index1 < stock_prices_vec.size(); stock_price_index1++){

        // 현재 검사하는 시점의 바로 직후부터 맨 끝까지 검사해야 하지만,
        // 마지막 인덱스 검사 때문에, 현재 검사하는 시점의 인덱스부터 시작하게 했다.
        // 어차피 가격이 같은 경우는 상관 없으므로 괜찮다.
        for(int stock_price_index2 = stock_price_index1; stock_price_index2 < stock_prices_vec.size(); stock_price_index2++){

            // 현재 검사에서 가격이 떨어지거나, 검사의 마지막 인덱스 일 때
            if(stock_prices_vec[stock_price_index2] < stock_prices_vec[stock_price_index1] || stock_price_index2 == stock_prices_vec.size() - 1){
                // 가격이 유지된 시간을 기록한다.
                stock_price_retention_time_vec.push_back(stock_price_index2 - stock_price_index1);
                // 다음 시점 검사
                break;
            }
        }
    }

    return stock_price_retention_time_vec;
}