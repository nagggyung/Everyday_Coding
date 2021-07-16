#include <iostream>
using namespace std;

int main() {
    int T, num;
    cin >> T;

    while(T--){
        int loc =0;
        cin >> num;
        while(num>0){
        if(num%2 == 1){
            cout << loc <<" ";
        }
        loc++;
        num/=2;
        }
    }

    return 0;
}


