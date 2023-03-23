package BOJ_JAVA;
import java.util.Scanner;
import java.util.ArrayList;

public class Boj_1449{
    private ArrayList<Integer> arr = new ArrayList<>();
    private ArrayList<Integer> range_arr = new ArrayList<>();

    public boolean check(int value , ArrayList<Integer> range_arr)
    {
        for(int i = 0 ; i < range_arr.size() ; i++)
        {
            if (value == range_arr.get(i))
            {
                return true;
            }
            else
            {
                continue;
            }
        }
        return false;
    }

    public int solution(int N , int L)
    {
        int count = 1;
        int start_location = arr.get(0);

        for(int i = 1 ; i < arr.size() ; i++)
        {
            for(int j = start_location ; j < start_location + L ; j++)
            {
                range_arr.add(j);
            }

            if(check(arr.get(i) , range_arr))
            {
                continue;
            }
            else
            {
                start_location = arr.get(i);
                count ++;
                range_arr = new ArrayList<>();
            }
        }

        return count;
    }
    
    public void run()
    {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int L = scanner.nextInt();

        for(int i = 0 ; i < N ; i++)
        {
            int value = scanner.nextInt();
            arr.add(value);
        }

        int result = solution(N, L);

        System.out.println(result);
        scanner.close();
    }
    
    public static void main(String[] args)
    {
        Boj_1449 boj = new Boj_1449();
        boj.run();
    }
}