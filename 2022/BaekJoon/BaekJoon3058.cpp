#include <iostream>

using namespace std;


int main() {
    int T;
    cin >> T;
    int num[7] = {0,};

    while(T--){
        int MIN = 101;
        int sum=0;

        for(int i=0; i<7; i++){
            cin >> num[i];
            if(num[i]%2 == 0){
                sum += num[i];
                if(MIN>num[i]){
                    MIN = num[i];
                }
            }

        }
        cout << sum <<" "<<MIN << endl;
    }

    return 0;
}

