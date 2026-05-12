// Tome Complexity
// public class Main01 {
//     // TC - O(N²)
//     public static void main(String[] args) {
//         int n = 5;

//         for(int i = 0; i < n; i++) {
//             for(int j = 0; j < n; j++) {
//                 System.out.println("Hello");
//             }
//         }
//     }
// }


public class Main01Space {
    // TC - O(N²) || // TC - O(N² / 2)
    public static void main(String[] args) {
        int n = 6;

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < i; j++) {
                System.out.print("Hello ");
            }
            System.out.println();
        }
    }
}