//  palindrome
import java.util.Scanner;
public class SDT {

    public static boolean isPalindrome(int numb){
        int org = numb;
        int temp = numb;
        int rev = 0;
        while(temp > 0){
            int last = temp % 10;
            rev = (rev * 10) + last;
            temp /= 10;
        }
        if(org == rev) return true;
        else return false;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter Number : ");
        int numb = sc.nextInt();

        if(isPalindrome(numb)){
            System.out.println("Palindrome");
        } 
        else{
            System.out.println("Not Palindrome");
        }

        sc.close();
    }
}