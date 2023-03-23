package BOJ_JAVA_2;
import java.util.Scanner;
import java.util.Arrays;

public class Boj_4097{
    public void run()
    {
        Scanner scanner = new Scanner(System.in);
        
        while(true)
        {
            int n = scanner.nextInt();

            if(n == 0) break;
            
            int[] arr = new int[n];
            for(int i = 0 ; i < n ; i++)
            {
                arr[i] = scanner.nextInt();
            }

            int[] dp = new int[n];
            dp[0] = arr[0];

            for(int i = 1 ; i < n ; i++)
            {
                dp[i] = Math.max(dp[i - 1] + arr[i] , arr[i]);
            }

            Arrays.sort(dp);
            System.out.println(dp[dp.length - 1]);
        }

        scanner.close();
    }
    
    public static void main(String[] args)
    {
        Boj_4097 boj = new Boj_4097();
        boj.run();
    }
}