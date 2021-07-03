#include <stdio.h>
int main()  
{
   int n,i,j;
   printf("Enter number of rows:");
   scanf("%d",&n);
   for(i=1;i<=n;i++)  //outer loop for counting the number of row iterations
   {
       for(j=1;j<=2*i;j++) //inner loop for doing the column iterations
           printf("%d",j%2);
       printf("\n");
   }
   return 0;
}

