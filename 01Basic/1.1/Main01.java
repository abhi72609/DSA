import java.util.Scanner;

public class Main01 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter Number: ");
        int number = sc.nextInt();
        
        System.out.println(number);
        
        sc.close();
    }
}