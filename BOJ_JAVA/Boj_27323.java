package BOJ_JAVA;
import java.util.Scanner;

public class Boj_27323{
    public void run()
    {
        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();
        int b = scanner.nextInt();

        System.out.println(a * b);

        scanner.close();
    }
    
    public static void main(String[] args)
    {

        Boj_27323 boj = new Boj_27323();

        boj.run();
    }
}