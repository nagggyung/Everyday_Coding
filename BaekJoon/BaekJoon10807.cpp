#include <iostream>
using namespace std;

int main() {
    int N, num, m=0;
    int arr[100] = {0,};
    int v, countNum=0;

    cin >> N;

    for(int m=0; m<N; m++){
        cin >> arr[m];
    }

    cin >> v;

    for(int i=0; i<N; i++){
        if(arr[i] == v){
            countNum++;
        }
    }

    cout << countNum;


    return 0;
}


