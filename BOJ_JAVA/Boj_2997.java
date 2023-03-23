package BOJ_JAVA;
import java.util.Scanner;
import java.util.Arrays;

public class Boj_2997{
    public int min(int[] arr)
    {
        int min = arr[0];

        for(int i = 1 ; i < arr.length ; i++)
        {
            if(arr[i] < min)
            {
                min = arr[i];
            }
        }

        return min;
    }

    public int check_minimum_size(int[] arr)
    {
        int firstNumber = arr[0] - arr[1];
        int secondNumber = arr[1] - arr[2];

        if(firstNumber < 0)
        {
            firstNumber = -1 * firstNumber;
        }

        if(secondNumber < 0)
        {
            secondNumber = -1 * secondNumber;
        }

        if(firstNumber < secondNumber)
        {
            return firstNumber;
        }
        else
        {
            return secondNumber;
        }
    }

    public int sum(int[] arr)
    {
        int result = 0;
        
        for(int i = 0 ; i < arr.length ; i++)
        {
            result += arr[i];
        }

        return result;
    }

    public void run()
    {
        Scanner scanner = new Scanner(System.in);

        int[] arr = new int[3];

        for(int i = 0 ; i < 3 ; i++)
        {
            arr[i] = scanner.nextInt();
        }

        Arrays.sort(arr);

        int a = min(arr);
        int d = check_minimum_size(arr);

        int s = 2 * (2 * a + 3 * d);

        int result = s - sum(arr);

        if(result < 0)
        {
            result = -1 * result;
        }

        System.out.println(result);

        scanner.close();
    }
    
    public static void main(String[] args)
    {
        Boj_2997 boj = new Boj_2997();

        boj.run();
    }
}