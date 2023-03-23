package BOJ_JAVA_2;
import java.util.Scanner;

public class Boj_4563{
    public int ccw(int[][] points)
    {
        int vec_a = points[0][0] * points[1][1] + points[1][0] * points[2][1] + points[2][0] * points[0][1];
        int vec_b = points[1][0] * points[0][1] + points[2][0] * points[1][1] + points[0][0] * points[2][1];

        return vec_a - vec_b;
    }

    public void run()
    {
        Scanner scanner = new Scanner(System.in);
        int[][] points = new int[3][2];
        for(int i = 0 ; i < 3 ; i++)
        {
            int[] point = new int[2];
            point[0] = scanner.nextInt();
            point[1] = scanner.nextInt();

            points[i] = point;
        }

        int outer_product = ccw(points);
        
        if(outer_product < 0)
            System.out.println(-1);
        else if(outer_product > 0)
            System.out.println(1);
        else
            System.out.println(0);
        
        scanner.close();
    }
    
    public static void main(String[] args)
    {
        Boj_4563 boj = new Boj_4563();
        boj.run();
    }
}