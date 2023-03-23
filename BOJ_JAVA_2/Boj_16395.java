package BOJ_JAVA_2;
import java.util.Scanner;

public class Boj_16395{
    public void run()
    {
        Scanner scanner = new Scanner(System.in);
        
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        
        int[][] dp = new int[n + 1][];
        
        dp[1] = new int[1];
        dp[2] = new int[2];

        dp[1][0] = 1;
        dp[2][0] = 1;
        dp[2][1] = 1;
        
        for(int i = 3 ; i < n + 1 ; i++)
        {
            dp[i] = new int[i];
            dp[i][0] = 1;
            for(int j = 1 ; j < i - 1 ; j++)
            {
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
            }
            dp[i][i - 1] = 1;
        }

        System.out.println(dp[n][k-1]);

        scanner.close();
    }
    
    public static void main(String[] args)
    {
        Boj_16395 boj = new Boj_16395();
        boj.run();
    }
}