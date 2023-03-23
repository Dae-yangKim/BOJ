package BOJ_JAVA_2;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class Boj_13702{
    public int binary_search(int k , ArrayList<Integer> arr , int num)
    {
        int left = 1;
        int right = num;
        int result = 0;
        
        while(left <= right)
        {
            int mid = (int)((left + right) / 2);
            int ml = 0;

            for(int i = 0 ; i < arr.size() ; i++)
                ml += (int)(arr.get(i) / mid);

            if(ml >= k)
            {
                result = mid;
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }

        return result;
    }

    public void run()
    {
        Scanner scanner = new Scanner(System.in);
        
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        
        ArrayList<Integer> arr = new ArrayList<Integer>();
        
        for(int i = 0 ; i < n ; i++)
        {
            int usrInput = scanner.nextInt();
            arr.add(usrInput);
        }

        System.out.println(binary_search(k , arr , Collections.max(arr)));

        scanner.close();
    }
    
    public static void main(String[] args)
    {
        Boj_13702 boj = new Boj_13702();
        boj.run();
    }
}