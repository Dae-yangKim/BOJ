package BOJ_JAVA_2;
import java.util.Scanner;

public class Boj_15624{
    public void run()
    {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;

        for(int i = 2 ; i < n + 1; i++)
            dp[i] = dp[i - 1] + dp[i - 2];
        
        System.out.println(dp[n] % 1000000007);
        scanner.close();
    }
    
    public static void main(String[] args)
    {
        Boj_15624 boj = new Boj_15624();
        boj.run();
    }
}