#include <iostream>
#include <string>
using namespace std;




int main()
{
    string words;
    getline(cin, words);

    for(int i=0; i<words.size(); i++){
        if(words[i]>='A' && words[i]<= 'Z'){
            words[i]+= 32;
        }else if(words[i]>='a' && words[i]<='z'){
            words[i]-=32;
        }else continue;
    }
    cout << words << endl;

     return 0;
}
