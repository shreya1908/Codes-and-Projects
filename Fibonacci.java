package test;
import java.util.*;
public class Fibonacci {
	public static void main(String[] args) {
		//creating an object of Scanner class
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the limit: ");
		int n = Integer.valueOf(sc.nextLine());
		int a=0,b=1,c;
		System.out.print(a+" "+b);
		//starting the iteration from 3 as a and b are already counted within the limit
		for (int i=3;i<=n;i++) {
			c=a+b;
			System.out.print(" "+c);
			a=b;
			b=c;
		}//end of for
	}//end of main
}//end of class
