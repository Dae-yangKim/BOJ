package BOJ_JAVA;
import java.util.Scanner;

public class Boj_2748 {
    public void run()
    {
        Scanner scanner = new Scanner(System.in);
        
        int n = scanner.nextInt();
        int[] dp = new int[n + 1];

        dp[0] = 0;
        dp[1] = 1;

        for(int i = 2 ; i < n + 1 ; i++)
        {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        System.out.println(dp[n]);

        scanner.close();
    }
    
    public static void main(String[] args)
    {
        Boj_2748 boj = new Boj_2748();
        
        boj.run();
    }
}
