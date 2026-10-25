class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
        return check(s, 0, s.length());
    }

    private boolean check(String s, int i, int n) {
        if (i >= n/2) return true;   
        if (s.charAt(i) != s.charAt(n - i - 1)) return false;
        return check(s, i + 1, n);   
    }
    
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("s = ");
        String s=sc.nextLine();
        Solution s1=new Solution();
        s1.isPalindrome(s);
    }
}