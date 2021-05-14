package test;
import java.util.*;
public class prime {
	public static void main(String[] args) {
		//creating an object of Scanner class
		Scanner sc = new Scanner(System.in);
		int res,count=0;
		System.out.println("Please insert any number");
		int num = Integer.valueOf(sc.nextLine());
		//checking whether the number is prime or not
		for (int i=1;i<=num;i++) {
			res=num%i;
			if (res==0) {
				count++;
			}
		}//end of for
		if (count==2) {
			System.out.println(num+" is prime number");
		}
		else {
			System.out.println(num+" is not prime number");
		}
	}//end of main
}//end of class
