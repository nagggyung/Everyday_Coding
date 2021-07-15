#include<iostream>
#include <string>
#include <algorithm>

using namespace std;

void missSpell(int T){
    string word;
    string wordList[T];
    int loc;
    for(int i=0; i<T; i++){
        cin >> loc >> word;
        loc -= 1;
        word.erase(loc,1);
        wordList[i] = word;
    }

    for(int j=0; j<T; j++){
        cout << wordList[j] << endl;
    }

}




int main(void){
    int T;
    cin >> T;
    missSpell(T);

    return 0;
}



