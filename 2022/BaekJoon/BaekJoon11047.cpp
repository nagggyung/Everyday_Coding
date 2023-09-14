#include <iostream>
#include <algorithm>
using namespace std;

bool desc(int a, int b){
    return a>b;
}


int main()
{
    int N, K, cal=0;
    cin >> N >> K;
    int cost[N]={0, };

    for(int i=0; i<N; i++){
        cin >> cost[i];
    }
    sort(cost, cost+N, desc);

    for(int j=0; j<N; j++){
        int m=0, r;
        m = K/cost[j];
        if(m==0) continue;
        K = K%cost[j];
        cal += m;
    }

    cout << cal << endl;


     return 0;
}
