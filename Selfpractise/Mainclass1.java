package Selfpractise;
class Delta{
    void test(){
        System.out.println("System Testing");
    }
}
class Beta extends Delta{
    void run(){
        System.out.println("System Run");
    }
}
class Alpha extends Beta{
    void stop(){
        System.out.println("System stop");
    }
}

public class Mainclass1{
    public static void main(String[] args) {
        Delta d = new Alpha();
        d.test();
        Beta b = (Beta)d;
        b.test();
        b.test();
        Alpha a = (Alpha)b;
        a.run();
        a.stop();
        a.test();
    }
}