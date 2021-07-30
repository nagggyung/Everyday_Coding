#include<iostream>
#include<string>
using namespace std;

int main(void){
    string word;
    getline(cin, word);
    int alph[26] ={0,}, maxNum=0, index, cnt=0;
    for(int i=0; i< word.length(); i++){
        if(word[i]>='a' && word[i] <='z'){
            word[i] = word[i]-32;
        }
        alph[word[i]-'A']++;
    }

    for(int j=0; j<26; j++){
        if(maxNum < alph[j]){
            maxNum = alph[j];
            index =j;
        }
    }

    for(int m=0; m<26; m++){
        if(maxNum == alph[m]) cnt++;
    }
    if(cnt!=1){
        printf("?");
    }else{
        printf("%c", index+'A');
    }

    return 0;
}
