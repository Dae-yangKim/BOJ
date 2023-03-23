package BOJ_JAVA;
import java.util.Scanner;

public class Boj_14490{
    public int gcd(int a , int b)
    {
        int tmp = a % b;

        while(tmp != 0)
        {
            a = b;
            b = tmp;

            tmp = a % b;
        }

        return b;

    }
    
    public void run()
    {
        Scanner scanner = new Scanner(System.in);

        String usrInput = scanner.next();
        String[] arr = usrInput.split(":");

        int a = Integer.parseInt(arr[0]);
        int b = Integer.parseInt(arr[1]);

        int result = gcd(a , b);

        System.out.println((int)(a / result) + ":" + (int)(b / result));

        scanner.close();
    }
    
    public static void main(String[] args)
    {
        Boj_14490 boj = new Boj_14490();
        boj.run();
    }
}