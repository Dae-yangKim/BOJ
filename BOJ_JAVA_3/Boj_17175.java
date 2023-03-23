package BOJ_JAVA_3;
import java.util.Scanner;

public class Boj_17175{
    static int num = 1000000007;
    public void run()
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] dp = new int[51];
        
        dp[0] = 1;
        dp[1] = 1;

        for(int i = 2 ; i < 51 ; i++)
            dp[i] = (dp[i - 2] + dp[i - 1] + 1) % num;

        System.out.println(dp[n] % num);
        scan.close();
    }
    
    public static void main(String [] args)
    {
        new Boj_17175().run();
    }
}