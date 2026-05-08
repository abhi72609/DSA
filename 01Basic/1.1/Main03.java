import java.util.Scanner;

public class Main03 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        
        // 1. Check Adult or Not
        
        System.out.print("Enter Your Age: ");
        int age = sc.nextInt();

        if(age >= 18) {
            System.out.println("You are Adult");
        } else {
            System.out.println("You are Not Adult");
        }


        
        // 2. Grade System
        
        System.out.print("Enter Marks: ");
        int marks = sc.nextInt();

        if(marks < 25) {
            System.out.println("F");
        }
        else if(marks <= 44) {
            System.out.println("E");
        }
        else if(marks <= 49) {
            System.out.println("D");
        }
        else if(marks <= 59) {
            System.out.println("C");
        }
        else if(marks <= 79) {
            System.out.println("B");
        }
        else if(marks <= 100) {
            System.out.println("A");
        }


        
        // 3. Job Eligibility
        
        System.out.print("Enter Age: ");
        int Age = sc.nextInt();

        if(Age < 18) {
            System.out.println("Not Eligible for Job");
        }
        else if(Age <= 57) {
            System.out.println("Eligible for Job");

            if(Age >= 55) {
                System.out.println("Eligible for job but retirement soon");
            }
        }
        else {
            System.out.println("Retirement Time");
        }

        sc.close();
    }
}