package BOJ_JAVA_3;

import java.util.Scanner;
import java.util.HashMap;

public class Boj_1351 {
    private static HashMap<Integer , Integer> dp = new HashMap<>();
    
    public int calculation(int i , int p , int q)
    {
        if(dp.containsKey(i))
            return dp.get(i);
        dp.put(i , (calculation((int) i / p , p , q) + calculation((int) i / q , p , q)));
        return dp.get(i);
    }
    
    public void run()
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int p = scan.nextInt();
        int q = scan.nextInt();

        dp.put(0 , 1);
        System.out.println(calculation(n, p, q));
        
        scan.close();
    }
    
    public static void main(String[] args)
    {
        new Boj_1351().run();
    }
}
