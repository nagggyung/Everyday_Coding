#include<iostream>
using namespace std;

int main(void){
    int arr[100] = {0,};
    int num=0, maxnum = arr[99], sum =0, index = 0, check = 0;
    while(check < 10){
        cin >> num;
        if(num < 1000 && num %10 ==0){
            sum += num;
            arr[num/10] += 1;
        }
        check ++;
    }
    for(int i=0; i<100; i++){
        if(maxnum < arr[i]){
            maxnum = arr[i];
            index = i;
        }
    }
    cout <<endl;
    cout << sum/10 << endl;
    cout << index*10;

    return 0;
}



