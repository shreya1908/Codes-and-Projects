#include <iostream>
using namespace std;

int main() 
{    
	cout << "\nProgram to check if a person is eligible to vote or not" << endl;
	cout << "\nLegal age for voting is 18 years" << endl;
	int age;
	cout << "\nEnter a person's age: " << endl;
	cin >> age;
	if (age>=18){
		cout << "\nPerson is eligible to vote" <<endl;
	}else{
		cout << "\nPerson is not eligible to vote" <<endl;
	}
    return 0;
}
