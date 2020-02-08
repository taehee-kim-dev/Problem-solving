#include <iostream>

using namespace std;

int main_1193(void){

    int x;
    cin>>x;

    int step=0, step_start_num=1;
    while(true){
        step++;
        step_start_num+=step;
        if(step_start_num>x)
            break;
    }

    int last_location_of_previous_step = step_start_num-1-step;

    int location_in_current_step = x-last_location_of_previous_step;

    if(step%2==0){
        int up=location_in_current_step;
        int down=step-location_in_current_step+1;
        cout<<up<<'/'<<down;
    }else{
        int up=step-location_in_current_step+1;
        int down=location_in_current_step;
        cout<<up<<'/'<<down;
    }

    return 0;
}