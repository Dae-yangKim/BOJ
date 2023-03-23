package BOJ_JAVA_2;
import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

public class Boj_5545{
    public int sum(Integer[] arr)
    {
        int result = 0;
        for(int i = 0 ; i < arr.length ; i++)
        {
            result = result + arr[i];
        }

        return result;
    }

    public void run()
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int a = scanner.nextInt();
        int b = scanner.nextInt();

        int c = scanner.nextInt();

        Integer[] kcal_arr = new Integer[n];

        for(int i = 0 ; i < n ; i++)
            kcal_arr[i] = scanner.nextInt();
        
        int result = c / a;

        Arrays.sort(kcal_arr , Collections.reverseOrder());

        for(int i = 1 ; i < kcal_arr.length + 1 ; i++)
        {
            int kcal = c + sum(Arrays.copyOfRange(kcal_arr , 0 , i));
            int price = a + (b * i);

            if(kcal / price > result)
                result = kcal / price;
            else
                break;
        }

        System.out.println(result);
        
        scanner.close();
    }
    
    public static void main(String[] args)
    {
        Boj_5545 boj = new Boj_5545();
        boj.run();
    }
}