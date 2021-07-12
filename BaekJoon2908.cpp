#include <iostream>
#include <sstream>
#include <string>

using namespace std;


int main()
{
    int num, mul=1, check = 0;
    string com = "0123456789";
    string res;
    int cres[10] ={0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    while(check < 3)
    { 
        cin >> num;
        if(num>100 && num <1000){
            mul *= num;
        }else{
            continue;
        }
        check++;
    }
    stringstream ss;
    ss << mul;
    ss >> res;

    for(long unsigned int i=0; i< res.length(); i++){
        for(long unsigned int j=0; j<com.length(); j++){
            if(res[i] == com[j])
                cres[j] += 1 ;
        }
    }

    for(int i=0; i<10; i++){
        cout << cres[i] << endl;
    }
    return 0;
}
