#include <iostream>
#include <algorithm>
using namespace std;



int main() {
    int score[8] = {0,};
    int sum=0;

    for(int i=0; i<8; i++){
        cin >> score[i];
    }

    int m=0, n=0, MAX = -1, index, indexArr[5] = {0,};

    while(m<5){
        for(int j=0; j<8; j++){
            if(MAX < score[j]){
                MAX = score[j];
                index = j;
            }
        }
        sum += MAX;
        indexArr[n++] = index+1;
        MAX = -1;
        score[index] = 0;
        m++;
    }

    sort(indexArr, indexArr + 5);
    cout << sum << endl;
    for(int i=0; i<5; i++){
        cout << indexArr[i] <<" ";
    }

    return 0;
}


