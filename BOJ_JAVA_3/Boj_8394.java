package BOJ_JAVA_3;
import java.util.Scanner;

public class Boj_8394{
    public void run()
    {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        if(n == 1)
            System.out.println(0);        
        else if(n < 3)
            System.out.println(n);
        else
        {
            int[] dp = new int[n + 1];
            dp[1] = 0;
            dp[2] = 2;
            dp[3] = 3;

            for(int i = 4 ; i < n + 1 ; i++)
                dp[i] = dp[i - 1] + dp[i - 2];

            System.out.println(dp[n]);
        }
        
        scanner.close();
    }
    
    public static void main(String[] args)
    {
        Boj_8394 boj = new Boj_8394();
        boj.run();
    }
}

/*
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    private void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] dp = new int[n][2];
        dp[0][0] = 1;
        for (int i = 1; i < n; i++) {
            dp[i][1] = dp[i-1][0];
            dp[i][0] = dp[i-1][0] + dp[i-1][1];
            dp[i][1] %= 10;
            dp[i][0] %= 10;
        }
        System.out.println((dp[n-1][0] + dp[n-1][1])%10);
    }
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}
 */

 // 이렇게 풀 수도 있다.