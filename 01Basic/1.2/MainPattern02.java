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



//       3
//       *  *  *  *  * 
//       *  *  *  * 
//       *  *  * 
//       *  * 
//       * 
// public class MainPattern02 {
//     public static void pattern(int n){
//         for(int i=1;i<=n;i++){
//             for(int j=1;j<=(n+1)-i;j++){
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


//       4
//       1  2  3  4  5 
//       1  2  3  4 
//       1  2  3 
//       1  2 
//       1 
// public class MainPattern02 {
//     public static void pattern(int n){
//         for(int i=1;i<=n;i++){
//             for(int j=1;j<=(n+1)-i;j++){
//                 System.out.print(" "+j+" ");
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




//       5
//               *
//             * * *
//           * * * * *
//         * * * * * * *
//       * * * * * * * * *
// public class MainPattern02 {
//     public static void pattern(int n){
//         int st = 1;
//         for(int i=1;i<=n;i++){ // row
//             int sp = n-i;
//             for(int j=1;j<=sp;j++){ // For Space
//                 System.out.print("  ");
//             }
//             for(int k=1;k<=st;k++){ // For Star
//                 System.out.print(" *");
//             }
//             st+=2;
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



//       6
//       * * * * * * * * *
//         * * * * * * *
//           * * * * *
//             * * *
//               *
// public class MainPattern02 {
//     public static void pattern(int n){
//         int st = (n*2)-1;
//         int sp = 0;
//         for(int i=1;i<=n;i++){ // row
//             for(int j=1;j<=sp;j++){ // For Space
//                 System.out.print("  ");
//             }
//             for(int k=1;k<=st;k++){ // For Star
//                 System.out.print(" *");
//             }
//             st-=2;
//             sp+=1;
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



//      7
//        *
//      * * *
//    * * * * *
//  * * * * * * *
//    * * * * *
//      * * *
//        *

// public class MainPattern02 {
//     public static void pattern(int n){
//         int st = 1;
//         int sp = n/2;

//         for(int i=1; i<=n; i++){

//             for(int j=1; j<=sp; j++){
//                 System.out.print("  ");
//             }

//             for(int k=1; k<=st; k++){
//                 System.out.print(" *");
//             }

//             if(i <= n/2){
//                 st += 2;
//                 sp -= 1;
//             }
//             else{
//                 st -= 2;
//                 sp += 1;
//             }
//             System.out.println();
//         }
//     }

//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Enter no of rows: ");
//         int n = sc.nextInt();
//         pattern(n);
//         sc.close();
//     }
// }


// 8
//  *    
//  * *  
//  * * *
//  * *  
// //  *  
// public class MainPattern02 {
//     public static void pattern(int n){
//         int st = 1;
//         int sp = n/2;

//         for(int i=1; i<=n; i++){
//             for(int k=1; k<=st; k++){
//                 System.out.print(" *");
//             }
//             for(int j=1; j<=sp; j++){
//                 System.out.print("  ");
//             }

//             if(i <= n/2){
//                 st += 1;
//                 sp -= 1;
//             }
//             else{
//                 st -= 1;
//                 sp += 1;
//             }
//             System.out.println();
//         }
//     }

//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.print("Enter no of rows: ");
//         int n = sc.nextInt();
//         pattern(n);
//         sc.close();
//     }
// }





// 9 

public class MainPattern02 {
    public static void pattern(int n){
        
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter no of rows: ");
        int n = sc.nextInt();
        pattern(n);
        sc.close();
    }

}

