package BOJ_JAVA;
import java.util.Scanner;

public class Boj_27433{
    public int factorial(int n)
    {
        int result = 1;
        
        for(int i = n ; i > 0 ; i--)
        {
            result = result * i;
        }

        return result;
    }

    public void run()
    {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int result = factorial(n);

        System.out.println(result);

        scanner.close();
    }
   
    public static void main(String[] args)
    {
        Boj_27433 boj = new Boj_27433();

        boj.run();
    }
}