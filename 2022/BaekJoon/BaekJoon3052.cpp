#include<iostream>
#include<set>

using namespace std;



int main(void){
    int input, countNum=0;
    set<int> s;
    int remainder;


    for(int i=0; i<10; i++){
        cin >> input;
        remainder = input%42;
        s.insert(remainder);
    }

    cout << s.size();

    return 0;
}



