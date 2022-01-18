#include<iostream>

using namespace std;



int main(void){
    int a,b,c,d,who;
    int sum=0, maxScore=0;

    for(int i=0; i<5; i++){
        cin >> a >> b >> c >> d;
        sum = a+b+c+d;
        if(maxScore<sum){
            maxScore = sum;
            who = i+1;
        }
    }
    cout << who << " "<<maxScore;



    return 0;
}



