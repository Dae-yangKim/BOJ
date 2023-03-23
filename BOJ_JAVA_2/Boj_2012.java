package BOJ_JAVA_2;
import java.util.Scanner;
import java.util.Arrays;

public class Boj_2012{
    public void run()
    {
        Scanner scanner = new Scanner(System.in);
        
        int n = scanner.nextInt();
        int[] arr = new int[n];

        for(int i = 0 ; i < arr.length ; i++)
        {
            arr[i] = scanner.nextInt();
        }

        Arrays.sort(arr);
        
        int result = 0;
        for(int i = 0 ; i < arr.length; i++)
        {
            result = result + Math.abs(arr[i] - (i + 1));
        }

        System.out.println(result);

        scanner.close();
    }
    
    public static void main(String[] args)
    {
        Boj_2012 boj = new Boj_2012();
        boj.run();
    }
}