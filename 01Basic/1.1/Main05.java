// public class Main05 {
//     public static void main(String[] args) {
        
//         int arr[] = {10, 20, 30, 40};

//         for(int i = 0; i < arr.length; i++) {
//             System.out.print(arr[i] + " ");
//         }
//     }
// }

// import java.util.Scanner;

// public class Main05 {
//     public static void main(String[] args) {
        
//         Scanner sc = new Scanner(System.in);

//         int arr1[] = new int[5];

//         for(int i = 0; i < 5; i++) {
//             arr1[i] = sc.nextInt();
//         }

//         for(int i = 0; i < 5; i++) {
//             System.out.print(arr1[i] + " ");
//         }

//         System.out.println("\nElement at index 3: " + arr1[3]);

//         sc.close();
//     }
// }


// 2D array
import java.util.Scanner;

public class Main05 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter rows: ");
        int rows = sc.nextInt();

        System.out.print("Enter cols: ");
        int cols = sc.nextInt();

        int arr2[][] = new int[rows][cols];

        for(int i = 0; i < rows; i++) {
            for(int j = 0; j < cols; j++) {
                arr2[i][j] = sc.nextInt();
            }
        }

        System.out.println("2D Array:");

        for(int i = 0; i < rows; i++) {
            for(int j = 0; j < cols; j++) {
                System.out.print(arr2[i][j] + " ");
            }
            System.out.println();
        }

        sc.close();
    }
}