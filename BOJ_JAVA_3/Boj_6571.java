package BOJ_JAVA_3;
import java.util.Scanner;
import java.util.ArrayList;

public class Boj_6571 {
    private ArrayList<Integer> arr = new ArrayList<>();
    
    public void run() 
    {
        Scanner scanner = new Scanner(System.in);

        arr.add(1);
        arr.add(1);
        int idx = 1;

        while(arr.get(arr.size() - 1) < Math.pow(10 , 100))
            arr.add(arr.get(idx) + arr.get(idx - 1));
        
        while(true)
        {
            int a = scanner.nextInt();
            int b = scanner.nextInt();

            if(a == 0 && b == 0)
                break;
            
            int result_a = 0 , result_b = 0;
            for(int i = 0 ; i < arr.size() ; i++)
            {
                if (arr.get(i) >= a && result_a == 0)
                    result_a = i;
                
                if (arr.get(i) >= b && result_b == 0)
                    result_b = i;
            }
            
            System.out.println(result_b - result_a);

            scanner.close();
        }
    }

    public static void main(String[] args) throws Exception
    {
        new Boj_6571().run();
    }
    
}
