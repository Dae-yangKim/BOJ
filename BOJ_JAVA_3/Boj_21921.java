package BOJ_JAVA_3;
import java.util.Scanner;
import java.util.ArrayList;

public class Boj_21921{
    public int max(ArrayList<Integer> blog_arr)
    {
        int maxx = 0;
        for(int i = 0 ; i < blog_arr.size() ; i++)
            if(blog_arr.get(i) > maxx)
                maxx = blog_arr.get(i);
        return maxx;
    }

    public void run()
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int x = scanner.nextInt();

        ArrayList<Integer> arr = new ArrayList<>();
        for(int i = 0 ; i < n ; i++)
            arr.add(scanner.nextInt());
        
        ArrayList<Integer> prefix_sum = new ArrayList<>();
        for(int i = 0 ; i < n+1 ; i++)
            prefix_sum.add(0);
        
        ArrayList<Integer> blog_arr = new ArrayList<>();
        for(int i = x ; i < n+1 ; i++)
            blog_arr.add(prefix_sum.get(i) - prefix_sum.get(i - x));
        
        int maxx = max(blog_arr);
        int count = 0;
        for(int i = 0 ; i < blog_arr.size() ; i++)
            if(blog_arr.get(i) == maxx)
                count++;
        
        System.out.println(maxx);
        System.out.println(count);

        scanner.close();
    }
    
    public static void main(String[] args)
    {
        new Boj_21921().run();
    }
}