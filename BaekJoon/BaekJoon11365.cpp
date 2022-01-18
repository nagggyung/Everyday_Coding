#include<iostream>
#include<algorithm>
using namespace std;

int main(void){
    string word;

    while(true){
        getline(cin, word, '\n');
        if(word == "END") break;

        reverse(word.begin(), word.end());
        cout << word << endl;

    }

    return 0;
}
