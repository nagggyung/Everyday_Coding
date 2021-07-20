#include <iostream>
#include <algorithm>

using namespace std;


int main() {
    int T;
    int score[5]={0,};

    cin >> T;

    while(T--){
        int sum=0;
        for(int i=0; i<5; i++){
            cin >> score[i];
        }
        sort(score, score+5);

        score[0]=0;
        score[4]=0;

        for(int j=0; j<5; j++){
            sum += score[j];
        }

        if((score[3]-score[1])>=4){
            cout << "KIN";
        }else{
            cout << sum;
        }
        cout << endl;
    }


    return 0;
}

