package Q2;
import java.io.*;
import java.util.Scanner;
public class Main {

    /*
     * NOTE: Create helper functions here if required
     */
    static int findSum(int A[], int N)
    {
        if (N <= 0)
            return 0;
        return (findSum(A, N - 1) + A[N - 1]*A[N - 1]);
    }
    static void store(int A[],int i,int N,Scanner keyboard)
    {
      if( i == N)
      	return;
      A[i] = keyboard.nextInt();
      store(A,i+1,N,keyboard);
      	
    }
    static int[] printer(int t,int i,int arr[])
    {
    	if (t == 0)
    		return arr;
        Scanner keyboard = new Scanner(System.in);
    	int N = keyboard.nextInt();
    	int A[] = new int[N];
    	store(A,0,N,keyboard);
    	arr[i]=findSum(A,N);
    	return printer(t-1,i+1,arr);
    }
    static void PrintList(int A[],int i,int T){
        if(i == T)
            return;
        System.out.println(A[i]);
        PrintList(A,i+1,T);
    }
    public static void main(String args[]) {
        /*
         * TODO: Complete this method
         * NOTE: Take input from STDIN and print the output to STDOUT
         */
         Scanner keyboard = new Scanner(System.in);
         int T = keyboard.nextInt();
         int arr[] = new int[T];
         int arr1[] = printer(T,0,arr);
         PrintList(arr1,0,T);
    }
}
