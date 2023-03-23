import java.util.Scanner;

public class Boj_1629{
    public int power(int a , int b , int c)
    {
        if(b == 0)
            return 1;
        
        int x = power(a , (int)b / 2 , c);

        if(b % 2 == 0)
            return (x * x)%c;
        else
            return (x * x * a)%c;
    }

    public void solution()
    {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();

        System.out.println(power(a , b , c));
        
        scan.close();
    }
    
    public static void main(String[] args)
    {
        new Boj_1629().solution();
    }
}