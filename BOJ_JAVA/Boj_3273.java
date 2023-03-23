package BOJ_JAVA;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Comparator;

public class Boj_3273{
    private ArrayList<Integer> arr = new ArrayList<Integer>();
    
    public int binary_search(ArrayList<Integer> arr , int x)
    {
        int left = 0;
        int right = arr.size() - 1;
        
        int count = 0;

        arr.sort(Comparator.naturalOrder());

        while(left < right)
        {
            if(arr.get(left) + arr.get(right) == x)
                count ++;


            if(arr.get(left) + arr.get(right) < x)
                left ++;
            else
                right --;
        }

        return count;
    }

    public void run()
    {
        Scanner scanner = new Scanner(System.in);
        
        int n = scanner.nextInt();
        for(int i = 0 ; i < n ; i++)
        {
            int num = scanner.nextInt();
            arr.add(num);
        }
        int x = scanner.nextInt();

        System.out.println(binary_search(arr , x));
        scanner.close();
    }
    
    public static void main(String[] args)
    {
        Boj_3273 boj = new Boj_3273();
        boj.run();
    }
}