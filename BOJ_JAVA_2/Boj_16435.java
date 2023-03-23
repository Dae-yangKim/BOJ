package BOJ_JAVA_2;
import java.util.Scanner;
import java.util.ArrayList;

public class Boj_16435{
    public int solution(ArrayList<Integer> arr , int l)
    {
        int length = l;
        
        while(true)
        {
            int check_len = length;
            
            for(int idx = 0 ; idx < arr.size() ; idx++)
            {
                if(length >= arr.get(idx))
                {
                    length += 1;
                    arr.remove(idx);
                    break;
                }
            }

            if(length == check_len) break;
            else continue;
        }

        return length;
    }

    public void run()
    {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> arr = new ArrayList<Integer>();

        int n = scanner.nextInt();
        int l = scanner.nextInt();
        
        for(int i = 0 ; i < n ; i++)
        {
            int num = scanner.nextInt();
            arr.add(num);
        }

        System.out.println(solution(arr , l));

        scanner.close();
    }
    
    public static void main(String[] args)
    {
        Boj_16435 boj = new Boj_16435();
        boj.run();
    }
}