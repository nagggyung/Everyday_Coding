#include<iostream>
#include<list>

using namespace std;



int main(void){

   int n=45, A, B, sum=0, input;
   list<int> a;
   list<int>::iterator iter = a.begin();
   int arr[1001] = {0,};
   int m=0;

   for(int i=1; i<=n; i++){
    for(int j=0; j<i; j++){
        if(a.size()<1001){
            a.push_back(i);
        }
    }
   }

   for(iter=a.begin(); iter!=a.end(); iter++){
        arr[m++] = *iter;
    }
    cin >> A >> B;
   for(int j=A-1; j<=B-1; j++){
        sum += arr[j];
   }
   cout << sum;


    return 0;
}



