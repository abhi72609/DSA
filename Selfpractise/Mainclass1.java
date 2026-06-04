// package Selfpractise;
// class Delta{
//     void test(){
//         System.out.println("System Testing");
//     }
// }
// class Beta extends Delta{
//     void run(){
//         System.out.println("System Run");
//     }
// }
// class Alpha extends Beta{
//     void stop(){
//         System.out.println("System stop");
//     }
// }

// public class Mainclass1{
//     public static void main(String[] args) {
//         Delta d = new Alpha();
//         d.test();
//         Beta b = (Beta)d;
//         b.test();
//         b.run();
//         Alpha a = (Alpha)d;
//         a.run();
//         a.stop();
//         a.test();
//     }
// }



// Method Overloading
// class Delta{
//     void test(int t){
//         System.out.println(t+t);
//     }
//     void test(double t){
//         System.out.println(t+t);
//     }
//     void test(int t,int d){
//         System.out.println(t+d);
//     }
//     void test(int t, double d){
//         System.out.println(t+d);
//     }
// }

// public class Mainclass1{
//     public static void main(String[] args) {
//         Delta d = new Delta();
//         d.test(1);
//         d.test(1.2);
//         d.test(1,3);
//         d.test(1,2.0);
//     }
// }

// method Overriding
// class Delta{
//     void test(){
//         System.out.println("Normal Test");
//     }
// }
// class Beta extends Delta{
//     @Override
//     void test(){
//         System.out.println("written Test");
//     }
// }

// public class Mainclass1{
//     public static void main(String[] args) {
//         Delta d = new Beta();
//         d.test();

//     }
// }


//  CUSTOM EXCEPTION
// class MyCustomException extends Exception
// {
//     MyCustomException(){

//     }
//     MyCustomException(String arg){
//         super("msg");
//     }
// }

// class Triggers
// {
//     static void logic (int num) throws MyCustomException{
//         if(num % 5 == 0)
//         {
//             throw new MyCustomException("/ By Five");
//         }
//     }
// }

// public class Mainclass1{
//     public static void main(String[] args){
//         try{
//             Triggers.logic(10);
//         }
//         catch(MyCustomException e){
//             e.printStackTrace();
//         }
//     }
// }




// Boxing
// import java.lang.reflect.Type;

// public class Mainclass1 {
//     public static void main(String[] args) {
//         int a = 10;
//         Integer ref = new Integer(a);
//         System.out.println(ref);

//         double d = 4.5;
//         double obj = new Double(d);
//         System.out.println(obj);
//     }
// }


// import java.lang.reflect.Type;

// public class Mainclass1 {
//     public static void main(String[] args) {
//         Integer ref = 45;
//         int r = ref;
//         System.out.println(r);

//         double obj = 4.5;
//         Double d = obj;
//         System.out.println(d);
//     }
// }

// Extending the thread class
// class ThreadDemo extends Thread{
//     @Override
//     public void run(){
//         for(int i=0; i<=4; i++){
//             System.out.println("Demo Thread...");
//         }
//     }
// }

// public class Mainclass1 {
//     public static void main(String[] args) {
//         System.out.println("Start Execution");
//         ThreadDemo td = new ThreadDemo();
//         td.start();
//         // td.run();
//         System.out.println("End Execution");
//     }
// }


// By implementing the runnable interface
// class SampleThread implements Runnable{
//     @Override
//     public void run(){
//         for(int i=0; i<=4; i++){
//             System.out.println("Demo Thread...");
//         }
//     }
// }

// public class Mainclass1 {
//     public static void main(String[] args) {
//         System.out.println("Start Execution");
//         SampleThread st = new SampleThread();
//         Thread th = new Thread(st);
//         th.start();
//         System.out.println("End Execution");
//         System.out.println("Id : "+th.getId() + " " +
//                             "Name : "+th.getName() + " " +
//                             "Priority: "+th.getPriority());
//     }
// }


// toString without override
// class Student2{
//     String name = "Abhi";
// }

// public class Mainclass1{
//     public static void main(String[] args) {
//         Student2 s =  new Student2();
//         System.out.println(s);
//     }
// }

// toString with override
// class Student2{
//     String name = "Abhi";
//     @Override
//     public String toString(){
//         return name;
//     }
// }

// public class Mainclass1{
//     public static void main(String[] args) {
//         Student2 s =  new Student2();
//         System.out.println(s);
//     }
// }