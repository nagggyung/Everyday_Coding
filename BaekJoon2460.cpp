#include <iostream>
#include <cmath>

using namespace std;


int searchTrainCompartment(int trainCompartment[]){
    int maxPeople = trainCompartment[9];
    for (int i = 0; i<10; i++){
        if(maxPeople < trainCompartment[i]){
            maxPeople = trainCompartment[i];
        }
    }
    return maxPeople;
}


int main()
{
    int trainCompartment[10];
    int in, out, total=0;

    for(int i = 0; i<10; i++){
        cin >> out >> in;
        total = abs(total + in - out);

        trainCompartment[i] = total;
    }

    cout << searchTrainCompartment(trainCompartment);



    return 0;
}
