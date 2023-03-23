package BOJ_JAVA_4;
import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    private ArrayList<Integer> arr = new ArrayList<>();
    
    public int gcd(int a , int b)
    {
        while(b != 0)
        {
            int temp = a;
            a = b;
            b = temp % b;
        }

        return a;
    }

    public void run()
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int first = scan.nextInt();

        for(int i = 0 ; i < n - 1 ; i++)
        {
            int num = scan.nextInt();
            arr.add(num - first);
            first = num;
        }

        int g = arr.get(0);
        for(int i = 1 ; i < arr.size() ; i++)
            g = gcd(g , arr.get(i));

        int result = 0;
        for(int sub : arr)
        {
            result += ((int) sub / g) - 1;
        }

        System.out.println(result);
        
        scan.close();
    }
    
    public static void main(String[] args)
    {
        new Main().run();
    }
}
