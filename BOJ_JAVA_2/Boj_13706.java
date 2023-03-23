package BOJ_JAVA_2;
import java.util.Scanner;

public class Boj_13706{
    public int binary_search(int n)
    {
        int left = 1;
        int right = n;
        int result = 0;

        while(left <= right)
        {
            int mid = (left + right) / 2;
            
            if(Math.pow(mid , 2) > n)
            {
                right = mid - 1;
                System.out.println(right);
            }
            else if(Math.pow(mid , 2) < n)
            {
                left = mid + 1;
                System.out.println(left);
            }
            else
                result = mid;
                break;
        }

        return result;
    }
    
    public void run()
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(binary_search(n));
        scanner.close();
    }
    
    public static void main(String[] args)
    {
        Boj_13706 boj = new Boj_13706();
        boj.run();
    }
}