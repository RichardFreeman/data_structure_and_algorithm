// C program to print all permutations with duplicates allowed
#include <stdio.h>

void display(int *arr, int length)
{
    for(int i=0; i<length; i++)
    {
        printf("%i", arr[i]);
    }

    printf("\n");
}

void swap(int *arr, int x, int y)
{
    int tmp = arr[x];
    arr[x] = arr[y];
    arr[y] = tmp;
}

void permute(int *arr, int start, int length)
{

    int i;

    if(start == length)
    {
        display(arr, length+1);
    }
    else
    {
        for(i = start; i <= length; i++)
        {
            swap(arr, start, i);

            permute(arr, start+1, length);

            swap(arr, start, i);
        }
    }
}

int main()
{
    int arr[] = {1, 2, 3};

    permute(arr, 0, 2);

    return 0;
}
