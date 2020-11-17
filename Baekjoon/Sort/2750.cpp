#include <cstdio>
#include <vector>

using namespace std;

int main(void){

    vector<int> nums;

    int N;
    scanf("%d", &N);

    while(N--){
        int num;
        scanf("%d", &num);
        nums.push_back(num);
    }

    for(int i=1; i<nums.size(); i++){
        int num_to_inserted = nums[i];
        int j;
        for(j=i-1; j>=0 && nums[j]>num_to_inserted; j--){
            nums[j+1]=nums[j];
        }
        nums[j+1]=num_to_inserted;
    }

    for(vector<int>::iterator iter=nums.begin(); iter!=nums.end(); iter++){
        printf("%d\n", *iter);
    }

    return 0;
}