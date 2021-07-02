#include <stdio.h>
int main()
{
	//taking input of two numbers
	int num1,num2;
	printf("Enter first number:");
	scanf("%d",&num1);
	printf("Enter second number:");
	scanf("%d",&num2);
	printf("Number before swapping are: %d,%d",num1,num2);
	//performing the swapping
	num1=num1+num2; 
	num2=num1-num2;
	num1=num1-num2;
	printf("\nNumber after swapping are: %d,%d",num1,num2);
	return 0;
}
