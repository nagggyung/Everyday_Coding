#include <iostream>
using namespace std;

int main() {
    int N;
    int maxNum, minNum;
    cin >> N;

    int num[N] = {0,};

    for(int i=0; i<N; i++){
        cin >> num[i];
    }
    maxNum = num[N-1];
    minNum = num[0];

    for(int m=0; m<N; m++){
        if(maxNum<num[m]){
            maxNum = num[m];
        }
        if(minNum>num[m]){
            minNum = num[m];
        }
    }
    cout << minNum << " " << maxNum;

    return 0;
}


