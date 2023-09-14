#include<iostream>

using namespace std;

int main(void){
    int t;
    cin >> t;
    string word;

    cin.ignore();

    while(t--){
        getline(cin, word);
        cout << word[0]<< word[word.length()-1]<<endl;
    }

    return 0;
}
