#include<iostream>

using namespace std;

int main(void){
   int alph[26]={0,}, t, x, y, n;
   string word;
   cin >> t;
   for(int i=0; i<26; i++){
    alph[i] = i+1;
   }
   cin.ignore();

   while(t--){
        getline(cin, word);
        n = word.length()/2;
        cout << "Distances: ";
        for(int i=0; i<n; i++){
            y = alph[word[word.length()+i-n]-'A'];
            x = alph[word[i]-'A'];
            if(y >= x){
                cout << y-x << " ";
            }else{
                cout << (y+26) - x <<" ";
            }

        }
        cout << endl;

   }

    return 0;
}
