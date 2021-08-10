#include <iostream>
using namespace std;

int main() 
{ 	
	int n;
	cout << "Enter the limit: " << endl;
	cin >> n;
	int arr[n];
	cout << "Enter elements: " << endl;
	for (int i=0; i<n; i++){
		cin >> arr[i];
	}
	cout << "You entered: " << endl;
	for (int i=0; i<n; i++){
		cout << " " << arr[i];
	}
}
