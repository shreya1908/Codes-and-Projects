package test;
import java.util.*;
public class Employee {
	int year;
	double salary;
	String name, address;
	//creating a method for taking inputs
	public void getInput() {
		//creating an object of Scanner class
		Scanner sc = new Scanner(System.in);
		System.out.println("Employee's name: ");
		name = sc.nextLine();
		System.out.println("Employee's year of joining: ");
		year = Integer.valueOf(sc.nextLine());
		System.out.println("Employee's salary: ");
		salary = Double.valueOf(sc.nextLine());
		System.out.println("Employee's address: ");
		address = sc.nextLine();
	}
	//creating a method for displaying the inputs
	public void display() {
		System.out.println("Employee's name is: "+name);
		System.out.println("Employee's year of joining is: "+year);
		System.out.println("Employee's salary is: "+salary);
		System.out.println("Employee's address is: "+address);
	}
	//creating the main method
	public static void main(String[] args) {
		//creating an array object of class Employee
		Employee emp[] = new Employee[3];
		for (int i=0;i<3;i++) {
			emp[i] = new Employee();
			emp[i].getInput();
		}
		for (int j=0;j<3;j++) {
			emp[j].display(); 
		}
	}
}
