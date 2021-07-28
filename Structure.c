#include<stdio.h>
#include<string.h>

//Declaration of structure employee
struct employee
{
	char name[30],deptname[30];
	int empno,age,phn,salary;
};
main()
{
//declaration of employee member as array
	struct employee employee[20];
	int n,i;
	printf("\nEnter the number of employees in your organization:\n");
	scanf("%d",&n);

//enter values using for loop
for(i=0;i<n;i++)
{
	printf("\nEnter Employee %d Name :",i+1);
	scanf("%s",&employee[i].name);
	printf("\nEmployee Department Name :");
	scanf("%s",&employee[i].deptname);
	printf("\nEmployee Id :");
	scanf("%d",&employee[i].empno);
	printf("\nEmployee Age :");
	scanf("%d",&employee[i].age);
	printf("\nEmployee Phn :");
	scanf("%d",&employee[i].phn);
	printf("\nEmployee Salary :");
	scanf("%d",&employee[i].salary);
}

//printing employee information
printf("\nEmployees Information\n");
for(i=0;i<n;i++)
{
	printf("\nEmployee %d",i+1);
	printf("\nName Department_Name Employee ID Age Phn No. Salary\n");
	printf("\n%s\t %s\t %d\t %d\t %d\t %d\n",employee[i].name,employee[i].deptname,employee[i].empno,employee[i].age,employee[i].phn,employee[i].salary);
	printf("\n");
}
}
