package BOJ_JAVA_3;
import java.util.Scanner;

public class Boj_3474 {
    public void run()
    {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();

        for(int i = 0 ; i < t ; i++)
        {
            int n = scan.nextInt();
            int count = 0;
            int five = 5;

            while(five <= n)
            {
                count += ((int)n / five);
                five = five * 5;
            }

            System.out.println(count);
        }
        scan.close();
    }

    public static void main(String[] args)
    {
        new Boj_3474().run();
    }
}
