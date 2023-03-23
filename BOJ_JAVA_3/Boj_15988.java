package BOJ_JAVA_3;

import java.util.Scanner;
import java.util.ArrayList;

public class Boj_15988{
    private ArrayList<Integer> dp = new ArrayList<>();
    
    public void run()
    {
        Scanner scan = new Scanner(System.in);
        
        int n = scan.nextInt();
        final int NUM = 1000000009;
        
        dp.add(1);
        dp.add(1);
        dp.add(2);

        for(int i = 3 ; i < 1000001 ; i++)
            dp.add((dp.get(i - 1) + dp.get(i - 2) + dp.get(i - 3)) % NUM);
        
        for(int i = 0 ; i < n ; i++)
        {
            int usrInput = scan.nextInt();
            System.out.println(dp.get(usrInput));
        }

        scan.close();
    }
    
    public static void main(String[] args)
    {
        new Boj_15988().run();
    }
}