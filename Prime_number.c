#include<stdio.h>
int Prime(int);
int i=0;
int main()
{
    int n=0,primeNo=0;	
    printf("Enter a number: ");
    scanf("%d",&n);
    i = n/2;
    primeNo = Prime(n);//calling the function Prime
    if(primeNo==1)
        printf("\n%d is a prime number ",n);
    else
        printf("\n%d is not a prime number ",n);
    return 0;
}

int Prime(int n)
{
    if(i==1){
        return 1;
    }
    else if(n % i == 0){
        return 0;
    }     
    else{
        i = i - 1; 
        Prime(n);//calling the function Prime itself recursively
    }
}
