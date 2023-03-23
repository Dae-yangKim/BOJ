import java.util.Scanner;

public class Boj_15886 {
    public void run()
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        String graph = scan.next();

        char[] arr = graph.toCharArray();
        int count = 0;
        for(int idx = 0 ; idx < n - 1 ; idx++)
        {
            if(arr[idx] == 'E' && arr[idx + 1] == 'W')
                count++;
        }

        System.out.println(count);
        scan.close();
    }
    
    public static void main(String[] args)
    {
        new Boj_15886().run();
    }
}
