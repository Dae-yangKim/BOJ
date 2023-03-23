package BOJ_JAVA;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class Boj_1302{
    private ArrayList<String> arr = new ArrayList<>();
    
    public String run()
    {
        Scanner scanner = new Scanner(System.in);
        
        int n = scanner.nextInt();
        
        for(int idx = 0 ; idx < n ; idx++)
        {
            String word = scanner.next();
            arr.add(word);
        }

        HashSet<String> hash = new HashSet<String>(arr);
        int max = Collections.frequency(arr, arr.get(0));
        String result = arr.get(0);

        for(int idx = 1 ; idx < hash.size() ; idx++)
        {
            if(max < Collections.frequency(arr, arr.get(idx)))
            {
                max = Collections.frequency(arr, arr.get(idx));
                result = arr.get(idx);
            }
            else if(max == Collections.frequency(arr, arr.get(idx)))
            {
                if(result.compareTo(arr.get(idx)) > 0)
                {
                    result = arr.get(idx);
                }
            }
        }

        scanner.close();
        return result;
    }
    
    public static void main(String[] args)
    {
        Boj_1302 boj = new Boj_1302();

        String result = boj.run();

        System.out.println(result);
    }
}