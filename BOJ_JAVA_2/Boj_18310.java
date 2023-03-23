package BOJ_JAVA_2;
import java.util.Scanner;
import java.util.Arrays;

public class Boj_18310{
    public void run()
    {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int[] arr = new int[n];

        for(int i = 0 ; i < n ; i++)
            arr[i] = scanner.nextInt();

        Arrays.sort(arr);

        int length = arr.length;

        if(length % 4 == 0)
            System.out.println(arr[(int)((length - 1) / 2)]);
        else
            System.out.println(arr[(int)(length / 2)]);

        scanner.close();
    }
 
    public static void main(String[] args)
    {
        Boj_18310 boj = new Boj_18310();
        boj.run();
    }
}