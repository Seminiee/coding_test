#include <iostream>
using namespace std;

int make_1(int n)
{
    int *arr = new int[n+1];
    arr[0] = 0;
    arr[1] = 0;
    arr[2] = 1;
    arr[3] = 1;

    int i=0, k=0;
    int k1 = 0, k2 = 0;
    for(i=4; i<=n; i++)
    {
        if(i % 3 == 0)
        {
            k1 = 1 + arr[i/2];
            k2 = 1 + arr[i-1];
            if(k1 <= k2)
                k = k1;
            else
                k = k2;
        }
            
        else
        {
            if(i % 2 == 0)
            {
                k1 = 1 + arr[i/2];
                k2 = 1 + arr[i-1];
                if(k1 <= k2)
                    k = k1;
                else
                    k = k2;
            }
            else
                k = 1 + arr[i-1];
        }
        arr[i] = k;
    }
    int res = arr[n];
    delete[] arr;
    return res;
}

int main()
{
    int input_n = 0;
    cin >> input_n;
    cout << make_1(input_n);
    return 0;
}