#include <iostream>
using namespace std;

int saltDelivery(int n)
{
    int *arr = new int[n+1];
    arr[0] = -1;
    arr[1] = -1;
    arr[2] = -1;
    arr[3] = 1;
    arr[4] = -1;
    arr[5] = 1;

    int i=0, k=0;
    for(i=6; i<=n; i++)
    {
        arr[i] = arr[5] + arr[i-5];
        if(arr[i-5] == -1)
        {
            arr[i] = arr[3] + arr[i-3];
            if(arr[i-3] == -1)
            {
                arr[i] = -1;
            }
        }
    }
    k = arr[n];

    delete[] arr;
    return k;
}

int main()
{
    int input_n = 0;
    cin >> input_n;

    cout<<saltDelivery(input_n);

    return 0;
}