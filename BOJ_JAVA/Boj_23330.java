package BOJ_JAVA;
import java.util.Scanner;
import java.util.Arrays;

public class Boj_23330{
    private int[] arr;

    public void solution()
    {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        arr = new int[n];

        for(int i = 0 ; i < n ; i++)
        {
            arr[i] = scanner.nextInt();
        }

        Arrays.sort(arr);

        int result = 0;

        for(int i = 0 ; i < n ; i++)
        {
            result += 2 * (n - 1 - 2 * i) * arr[i];
        }

        if(result < 0)
        {
            result = result * -1;
        }

        System.out.println(result);

        scanner.close();
    }
    
    public static void main(String[] args)
    {
        Boj_23330 boj = new Boj_23330();

        boj.solution();
    }
}