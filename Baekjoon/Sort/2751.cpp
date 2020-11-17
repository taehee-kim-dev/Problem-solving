#include <cstdio>
#include <vector>

using namespace std;

void merge(vector<int> &list, int left, int mid, int right){
    vector<int> sorted;
    int i=left, j=mid+1;

    while(i<=mid && j<=right){
        if(list[i]<=list[j]){
            sorted.push_back(list[i++]);
        }else{
            sorted.push_back(list[j++]);
        }
    }

    if(i>mid){
        while(j<=right){
            sorted.push_back(list[j++]);
        }
    }else{
        while(i<=mid){
            sorted.push_back(list[i++]);
        }
    }

    int k=0;
    for(int l=left; l<=right; l++){
        list[l]=sorted[k++];
    }
}

void merge_sort(vector<int> &list, int left, int right){
    int mid;
    
    if(left<right){
        mid=(left+right)/2;
        merge_sort(list, left, mid);
        merge_sort(list, mid+1, right);
        merge(list, left, mid, right);
    }
}



int main(void){

    vector<int> nums;

    int N;
    scanf("%d", &N);

    while(N--){
        int num;
        scanf("%d", &num);
        nums.push_back(num);
    }

    merge_sort(nums, 0, nums.size()-1);

    for(vector<int>::iterator iter=nums.begin(); iter!=nums.end(); iter++){
        printf("%d\n", *iter);
    }

    return 0;
}