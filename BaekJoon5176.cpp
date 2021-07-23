#include <iostream>
#include <set>
using namespace std;


int main() {

    int K, P, M;
    int sitNum;

    cin >> K;
    while(K--){
        set<int> s;
        cin >> P >> M;
        for(int i=0; i<P; i++){
            cin >> sitNum;
            if(sitNum <= M){
                s.insert(sitNum);
            }

        }
        cout << P - s.size() << endl;
        s.clear();
    }


    return 0;
}

