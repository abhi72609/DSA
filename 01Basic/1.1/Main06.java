public class Main06 {
    public static void main(String[] args) {
        
        String str1 = "ABHISHEK";

        // Type
        System.out.println(str1.getClass().getName());

        // Print string
        System.out.println(str1);

        // Access from back
        System.out.println(str1.charAt(str1.length() - 1));

        // Replace
        String str2 = str1.replace('I', 'S');
        System.out.println(str2);

        // Traverse string
        int i = 0;

        while(i < str1.length()) {
            System.out.println(str1.charAt(i));
            i++;
        }
    }
}