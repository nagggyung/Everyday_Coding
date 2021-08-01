#include<iostream>
#include<string>
using namespace std;

int main(void){
    string words;
    getline(cin, words);

    for(int i=0; i<words.length(); i++){
        if(words[i] >= 'A' && words[i] <= 'Z'){
            if(words[i] + 13 <= 90){
                words[i] = words[i] + 13;
            }else{
                words[i] = words[i]+13 -26;
            }

        }else if(words[i] >='a' && words[i] <= 'z'){
           if(words[i] + 13 <= 122){
                words[i] = words[i] + 13;
            }else{
                words[i] = words[i]+13 -26;
            }
        }else continue;
    }

    cout << words << endl;

    return 0;
}

