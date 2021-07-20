#include <iostream>
#include <algorithm>

using namespace std;


int main() {
    int num[9]={0,};
    int sum=0, index1, index2;

    for(int i=0; i<9; i++){
        cin >> num[i];
        sum += num[i];
    }

    for(int m=0; m<9; m++){
        for(int n=0; n<9; n++){
            if((sum - (num[m]+num[n]))==100){
                index1 = m;
                index2 = n;
            }
        }
    }
    num[index1] = 0;
    num[index2] = 0;
    sort(num, num+9);
    for(int j=0; j<9; j++){
        if(num[j]==0) continue;
        cout << num[j] << endl;
    }


    return 0;
}

