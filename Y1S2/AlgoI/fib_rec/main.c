#include <stdio.h>

int fib(int n)
{
    if(n == 0) return 0;
    if(n == 1) return 1;
    return fib(n-1) + fib(n-2);
}

int main()
{
    int n = 10;
    int ris = fib(n);
    printf("fib of [%d]: %d\n",n,ris);

    return 0;
}
