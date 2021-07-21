#include<stdio.h>
int lcm(int, int);  
int main()
{
    int a, b, lcm_num;
    printf("\nEnter first number: ");
    scanf("%d", &a);
    printf("\nEnter second number: ");
    scanf("%d", &b);
    lcm_num = lcm(a,b);    
    printf("\nLCM of %d and %d is: %d ", a, b, lcm_num);
    return 0;
}

int lcm(int a, int b)
{
    static int temp = 1;    
    if(temp%a == 0 && temp%b == 0)
    {
        return temp;
    }
    else
    {
        temp++;
        lcm(a,b);
        return temp;
    }
}
