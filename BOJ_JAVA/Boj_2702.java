package BOJ_JAVA;
import java.util.Scanner;

public class Boj_2702{

    public int gcd(int a,  int b)
    {
        while(b != 0)
        {
            int temp = a;
            a = b;
            b = temp % b;
        }
        
        return a;
    }

    public int lcm(int a , int b)
    {
        return (int)((a * b) / gcd(a , b));
    }
    
    public void run()
    {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();

        for(int i = 0 ; i < N ; i++)
        {
            int a = scanner.nextInt();
            int b = scanner.nextInt();

            System.out.println(lcm(a , b) + " " + gcd(a , b));
        }

        scanner.close();
    }

    public static void main(String[] args)
    {
        Boj_2702 boj = new Boj_2702();

        boj.run();
    }
    
}