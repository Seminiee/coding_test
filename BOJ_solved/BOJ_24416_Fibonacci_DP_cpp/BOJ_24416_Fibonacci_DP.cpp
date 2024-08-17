#include <iostream>
using namespace std;

int exec;

int recursive_Fibo(int n)
{
    if(n == 1 || n == 2)
    {
        exec+=1;
        return 1;
    }
    else
    {
        return recursive_Fibo(n-1) + recursive_Fibo(n-2);
    }
}

int dp_Fibo(int n)
{
    int *arr = new int[n+1];
    int res = 0;
    arr[0] = 0;
    arr[1] = 1;
    arr[2] = 2;

    int i = 0;
    for(i=3; i<=n; i++)
    {
        arr[i] = arr[i-1] + arr[i-2];
        exec+=1;
    }
    res = arr[n];
    delete[] arr;
    return res;
}

int main()
{
    int sharp1, sharp2;
    int input_n = 0;
    cin >> input_n;

    exec = 0;
    recursive_Fibo(input_n);
    sharp1 = exec;

    exec = 0;
    dp_Fibo(input_n);
    sharp2 = exec;

    cout<<sharp1<<" "<<sharp2;
    return 0;
}