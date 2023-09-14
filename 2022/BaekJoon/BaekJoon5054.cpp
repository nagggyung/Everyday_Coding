#include <iostream>
using namespace std;



int main() {
    int t, n;
    cin >> t;

    while(t--){
        int MAX = -1, MIN = 100, x[20];
        cin >> n;

        for(int i=0; i<n; i++){
            cin >> x[i];
            if(MAX < x[i]) MAX = x[i];
            if(MIN > x[i]) MIN = x[i];
        }
        cout << (MAX-MIN)*2 << endl;
    }




    return 0;
}


