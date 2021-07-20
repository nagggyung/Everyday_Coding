#include <iostream>

using namespace std;


int main() {
    int hamburger[3]={0,};
    int drink[2]={0,};

    for(int i=0; i<3; i++){
        cin >> hamburger[i];
    }
    for(int j=0; j<2; j++){
        cin >> drink[j];
    }

    int cheapest = hamburger[0]+drink[0];

    for(int m=0; m<3; m++){
        for(int n=0; n<2; n++){
            if(cheapest > hamburger[m]+drink[n]){
                cheapest = hamburger[m]+drink[n];
            }
        }
    }

    cout << cheapest-50;
    return 0;
}


