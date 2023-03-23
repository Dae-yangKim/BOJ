package BOJ_JAVA_3;

import java.util.ArrayList;
import java.util.Scanner;

public class Boj_2644{
    int a , b;
    int n;
    ArrayList<Integer>[] graph = new ArrayList[n + 1];
    ArrayList<Integer> arr = new ArrayList<>();

    public void dfs(int v , int num , boolean[] visited)
    {
        num += 1;
        visited[v] = true;
        
        if(b == v)
            arr.add(num);
        
        for(int i : graph[v])
        {
            if(!visited[v])
                dfs(i , num , visited);
        }
    }

    public void run()
    {
        Scanner scan = new Scanner(System.in);
        n = scan.nextInt();
        a = scan.nextInt();
        b = scan.nextInt();
        int m = scan.nextInt();

        boolean[] visited = new boolean[n + 1];
        for(int i = 0 ; i < n + 1 ; i++)
            visited[i] = false;

        for(int i = 0 ; i < m ; i++)
        {
            int x = scan.nextInt();
            int y = scan.nextInt();

            graph[x].add(y);
            graph[y].add(x);
        }

        dfs(a , 0 , visited);

        if(arr.size() == 0)
            System.out.println(-1);
        else
            System.out.println(arr.get(0) - 1);

        scan.close();
    }
    
    public static void main(String[] args)
    {
        new Boj_2644().run();
    }
}