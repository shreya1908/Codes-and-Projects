package test;
import java.util.*;
public class switch_case {
	public static void main(String[] args) {
		// creating an object of Scanner class
		Scanner sc = new Scanner(System.in);
		//taking user input
		System.out.println("Enter your choice: \n 1) Hi \n 2) Hey \n 3) Hello");
		int choice = Integer.valueOf(sc.nextLine());
		//program snippet for switch case
		switch(choice) {
			case 1 : System.out.println("You said Hi !");
					 break;
			case 2 : System.out.println("You said Hey !");	
					 break;
			case 3 : System.out.println("You said Hello !");
					 break;
			default : System.out.println("Invalid Choice !");
		} //end of switch case
	} //end of main
} //end of class
