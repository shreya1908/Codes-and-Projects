package test;

//importing packages
import java.util.*;
public class minutes {
	public static void main(String args[]){
		//creating an object of Scanner class
		Scanner sc = new Scanner(System.in);
		//taking input from user
		System.out.println("Enter the number of minutes: ");
		int mins = Integer.valueOf(sc.nextLine());
		
		//conversion of minutes to years
		int years = mins / 525600;
		int remaining_mins = mins % 525600;
		int days = remaining_mins / 1440;
		
		//printing the total number of years and days
		System.out.println(mins+" minutes converted into number of years and days is approximately "+years+" years and "+days+ " days");
	}
}
