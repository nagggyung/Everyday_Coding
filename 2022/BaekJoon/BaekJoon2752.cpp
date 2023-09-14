#include <iostream>
#include <algorithm>

using namespace std;


int main() {

    int num[3] = {0,};

    for(int i=0; i<3; i++){
        cin >> num[i];
    }
    sort(num, num+3);

    for(int j=0; j<3; j++){
        cout << num[j] << " ";

    }

    return 0;
}


