class Solution {
    public int reverse(int x) {
            int rev=0;
            while(x!=0){
                int lastDigit=x%10;
                if (rev > Integer.MAX_VALUE/10 || rev < Integer.MIN_VALUE/10) {
                return 0;
                }
                rev=(rev*10)+lastDigit;
                x=x/10;
            }
            return rev;
    }
        
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("x = ");
        int x=sc.nextInt();
        Solution obj=new Solution();
           int result=obj.reverse(x);
           System.out.print(result);
    }
    }
