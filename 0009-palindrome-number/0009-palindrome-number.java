import java.util.Scanner;
class Solution {
    public boolean isPalindrome(int x) {
        int temp=x,revNo=0;
        while(x>0){
            int lastDigit=x%10;
            revNo=(revNo*10)+lastDigit;
            x/=10;
        }
        if(revNo==temp){
            return true;
        }
        else{
            return false;
        }
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("x = ");
        int x=sc.nextInt();
        Solution s1=new Solution();
        boolean value=s1.isPalindrome(x);
        System.out.println(value);
    }
}