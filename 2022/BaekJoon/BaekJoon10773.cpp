#include <iostream>
#include <list>
using namespace std;


int main() {
    int k, num, sum=0;
    cin >> k;

    list<int> l;

    while(k--){
        cin >> num;
        if(num != 0){
            l.push_back(num);
        }else{
            l.pop_back();
        }
    }

    list <int> :: iterator it;

    for(it = l.begin(); it!=l.end(); it++){
        sum += *it;
    }

    cout << sum;



    return 0;
}

