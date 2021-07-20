#include <iostream>
#include <algorithm>
using namespace std;



int main() {
    int N;
    cin >> N;
    int num, arr[N]={0,};

    for(int i=0; i<N; i++){
       cin >> num;
        for(int j=0; j<N; j++){
            if(num == arr[j]){
                break;
            }else{
                arr[i] = num;
            }
        }
    }
   sort(arr, arr+N);
    for(int m=0; m<N; m++){
        cout << arr[m] << endl;
    }

    return 0;
}


