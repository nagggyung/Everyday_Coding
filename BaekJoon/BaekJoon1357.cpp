#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int Rev(int a){
    string A;
    A = to_string(a);
    reverse(A.begin(), A.end());
    a = stoi(A);
    return a;
}

int main()
{
    int x,y;
    string X,Y;

    cin >> x >> y;

    if(((x/10)>0 && (x%10)==0)){
        x/=10;
    }
    if(((y/10)>0 && (y%10)==0)){
        y/=10;
    }

    cout << Rev(Rev(x)+Rev(y))<< endl;


     return 0;
}
