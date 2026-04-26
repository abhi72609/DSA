//  palindrome
// import java.util.Scanner;
// public class SDT {

//     public static boolean isPalindrome(int numb){
//         int org = numb;
//         int temp = numb;
//         int rev = 0;
//         while(temp > 0){
//             int last = temp % 10;
//             rev = (rev * 10) + last;
//             temp /= 10;
//         }
//         if(org == rev) return true;
//         else return false;
//     }
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);

//         System.out.println("Enter Number : ");
//         int numb = sc.nextInt();

//         if(isPalindrome(numb)){
//             System.out.println("Palindrome");
//         } 
//         else{
//             System.out.println("Not Palindrome");
//         }

//         sc.close();
//     }
// }



// import java.util.Scanner;

// public class SDT{
    
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int t = sc.nextInt();
//         while(t>0){
//             int ini = sc.nextInt();
//             int fin = sc.nextInt();
//             for(int i = ini; i<=fin; i++){
//                 if(i % 2 != 0){
//                     System.out.println(i);
//                 }
//             }
//         }
//         sc.close();
//     }
// }







//  sum of the digit
// import java.util.Scanner;

// public class SDT{

//     public static int addNum(int num){
//         int temp = num;
//         int add = 0;
//         while(temp > 0){
//             int rem = temp % 10;
//             add += rem;
//             temp /= 10;
//         }
//         return add;
//     }

//     public static void main(String[] args){
//         Scanner sc = new Scanner(System.in);
//         int t = sc.nextInt();
//         while(t>0){
//             int num = sc.nextInt();
//             System.out.println(addNum(num));
//         }
//         sc.close();
//     }
// }


// Neon Number
import java.util.Scanner;

public class SDT{

    public static boolean neonNum(int num){
        int org = num;
        int sq = num * num;
        int fin = 0;
        while(sq > 0){
            int rem = sq % 10;
            fin += rem;
            sq /= 10;
        }
        return org == fin;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter No of times : ");
        int t = sc.nextInt();
        
        while (t > 0) {
            int num = sc.nextInt();
            if(neonNum(num)){
                System.out.println("Neon "+ num);
            }
            else{
                System.out.println("Not a Neon "+ num);
            }
            t--;
        }
        sc.close();
    }
}





