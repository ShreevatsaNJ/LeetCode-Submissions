import java.util.Scanner;
class Solution {

    public int fib(int n) {
        if(n<=1) return n;
        return fib(n-1)+fib(n-2);
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("n = ");
        int n=sc.nextInt();
        Solution s1=new Solution();
        System.out.println(s1.fib(n));
        sc.close();
    }
}