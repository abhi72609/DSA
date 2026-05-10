//      Patterns Problem
import java.util.Scanner;
//       1
//       *  *  *  * 
//       *  *  *  * 
//       *  *  *  * 
//       *  *  *  * 
// public class MainPattern02 {
//     public static void main(String[] args) {
//         for(int i=1;i<=4;i++){
//             for(int j=1;j<=4;j++){
//                 System.out.print(" * ");
//             }
//             System.out.println();
//         }
//     }
// }



//       2
//       * 
//       *  * 
//       *  *  * 
//       *  *  *  * 
//       *  *  *  *  * 

// public class MainPattern02 {
//     public static void pattern(int n){
//         for(int i=1;i<=n;i++){
//             for(int j=1;j<=i;j++){
//                 System.out.print(" * ");
//             }
//             System.out.println();
//         }
//     }
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Enter no of rows : ");
//         int n = sc.nextInt();
//         pattern(n);
//         sc.close();
//     }
// }









public class MainPattern02 {
    public static void pattern(int n){
        for(int i=1;i<=n;i++){
            for(int j=1;j<=(n+1)-i;j++){
                System.out.print(" * ");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter no of rows : ");
        int n = sc.nextInt();
        pattern(n);
        sc.close();
    }
}