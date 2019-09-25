#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main(void){

    int N;
    scanf("%d", &N);

    vector<int> count_frequency(8001, 0);
    vector<int> input_nums;

    int sum=0;
    for(int i=0; i<N; i++){
        int input_num;
        scanf("%d", &input_num);
        input_nums.push_back(input_num);
        sum+=input_num;

        if(input_num>=0){
            count_frequency[input_num]++;
        }else{
            input_num*=(-1);
            input_num+=4000;
            count_frequency[input_num]++;
        }
    }
    
    int average = int(round(double(sum)/double(N)));

    printf("%d\n", average);

    sort(input_nums.begin(), input_nums.end());

    int mid = input_nums.size()/2;

    printf("%d\n", input_nums[mid]);

    vector<int>::iterator iter = max_element(count_frequency.begin(), count_frequency.end());

    int highest_frequency = *iter;

    int index_of_highest_freqency = iter - count_frequency.begin();

    vector<int> highest_frequency_nums;

    for(iter=count_frequency.begin(); iter!=count_frequency.end(); iter++){
        if(*iter==highest_frequency){
            int number = iter-count_frequency.begin();
            if(number>4000){
                number-=4000;
                highest_frequency_nums.push_back((-1)*(number));
            }else{
                highest_frequency_nums.push_back(number);
            }
        }
    }

    if(highest_frequency_nums.size()==1){
        int highest_frequency_num = highest_frequency_nums[0];
        if(highest_frequency_num>4000){
            highest_frequency_num*=(-1);
        }
        printf("%d\n", highest_frequency_num);
    }else if(highest_frequency_nums.size()>1){
        sort(highest_frequency_nums.begin(), highest_frequency_nums.end());
        int second_highest_frequency_num = highest_frequency_nums[1];
        printf("%d\n", second_highest_frequency_num);
    }

    int fisrt = *(input_nums.end());
    int last = *(input_nums.begin());

    printf("%d", *(input_nums.end()-1)-*(input_nums.begin()));

    return 0;
}