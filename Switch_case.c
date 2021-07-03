#include <stdio.h>
int main()
{
	int choice;
	printf("Enter your choice \n1)Pizza \n2)Burger \n3)Pasta \n4)French Fries \n5)Sandwich\n");
	scanf("%d",&choice);
	switch(choice){
		case 1:printf("Food item - Pizza");
			   printf("\nPrice - Rs 239");
			   break;
		case 2:printf("Food item - Burger");
			   printf("\nPrice - Rs 129");
			   break;
		case 3:printf("Food item - Pasta");
			   printf("\nPrice - Rs 179");
			   break;
		case 4:printf("Food item - French Fries");
			   printf("\nPrice - Rs 99");
			   break;
		case 5:printf("Food item - Sandwich");
			   printf("\nPrice - Rs 149");
			   break;
		default:printf("Wrong Choice");
	}
	return 0;
}
