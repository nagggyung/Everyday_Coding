#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
     int W[10]={0,}, K[10]={0,};
     int sumW=0, sumK=0;

     for(int i=0; i<10; i++){
        cin >> W[i];
     }
     for(int j=0; j<10; j++){
        cin >> K[j];
     }
     sort(W,W+10);
     sort(K, K+10);

     cout << W[9]+W[8]+W[7] <<" "<< K[9]+K[8]+K[7] <<endl;


     return 0;
}
