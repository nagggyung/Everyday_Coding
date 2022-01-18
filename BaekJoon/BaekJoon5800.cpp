#include <iostream>
#include <algorithm>

using namespace std;




int main() {
    int K;
    cin >> K;



    for(int i=0; i<K; i++){
        int N;
        cin >> N;
        int mathScore[N]={0,};
        int sum=0, Max=-1, Min=101, gap=0;

        for(int j=0; j< N; j++){
            cin >> mathScore[j];
            sum+=mathScore[j];
            if(Max<mathScore[j]){
                Max = mathScore[j];
            }
            if(Min>mathScore[j]){
                Min = mathScore[j];
            }
        }
        sort(mathScore, mathScore+N);

        for(int m=0; m<N-1; m++){
           if(gap < (mathScore[m+1]-mathScore[m])){
                gap=mathScore[m+1]-mathScore[m];
            }
        }


        cout << "Class "<< i+1 <<endl;
        cout << "Max " << Max<< ", " << "Min " << Min<< ", " << "Largest gap " << gap <<endl;

    }


    return 0;
}

