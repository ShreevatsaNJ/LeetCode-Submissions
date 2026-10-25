import java.util.*;

class Solution {
    public int maxFrequency(int[] nums, int k) {
        Arrays.sort(nums);
        long sum = 0;
        int left = 0, result = 1;

        for (int right = 0; right < nums.length; right++) {
            sum += nums[right];

            while ((long)nums[right] * (right - left + 1) - sum > k) {
                sum -= nums[left];
                left++;
            }

            result = Math.max(result, right - left + 1);
        }
        return result;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 4};
        int k = 5;
        Solution sol = new Solution();
        System.out.println(sol.maxFrequency(nums, k)); 
    }
}
