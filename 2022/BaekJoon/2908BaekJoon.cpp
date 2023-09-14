#include <iostream>

using namespace std;

int reverse(int num){
    int reversedNum = 0, remainder;
    while(num != 0){
        remainder = num % 10;
        reversedNum = reversedNum * 10 + remainder;
        num /= 10;

    }
    return reversedNum;
}


int main()
{
    int num1, num2;
    int reversedNumber1, reversedNumber2;
    cin >> num1>> num2;

    reversedNumber1 = reverse(num1);
    reversedNumber2 = reverse(num2);

    if (reversedNumber1 > reversedNumber2){
        cout << reversedNumber1;
    }else{
        cout << reversedNumber2;
    }


    return 0;
}
