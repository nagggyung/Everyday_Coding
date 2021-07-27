#include <iostream>
#include <string>
using namespace std;


int main() {
    string words;
    getline(cin, words);
    string alphabet = "abcdefghijklmnopqrstuvwxyz";

    for(int i=0; i<alphabet.length(); i++){
        cout << (int)words.find(alphabet[i]) << " ";

    }


    return 0;
}

