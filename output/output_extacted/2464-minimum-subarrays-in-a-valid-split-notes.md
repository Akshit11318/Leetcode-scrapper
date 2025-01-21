## Minimum Subarrays in a Valid Split
**Problem Link:** https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Output: The minimum number of subarrays required to split the array such that the sum of the elements in each subarray is a perfect square.
- Key requirements:
  - Each subarray must have a non-negative sum.
  - The sum of each subarray must be a perfect square.
- Edge cases:
  - The input array can be empty.
  - The input array can contain negative numbers.

**Example Test Cases:**

* Input: `nums = [4,3,1,2,3,5,4,1]`
Output: `4`
Explanation: One possible way to split the array is `[4], [3,1,2], [3,5], [4,1]`. The sum of each subarray is a perfect square: `4`, `6`, `8`, and `5`.
* Input: `nums = [1,1,1,1,1,1,1]`
Output: `7`
Explanation: Each subarray must have a sum of `1`, so we need `7` subarrays.

---

### Brute Force Approach

**Explanation:**
The brute force approach involves trying all possible splits of the array and checking if the sum of each subarray is a perfect square.

```cpp
class Solution {
public:
    int minSubarrays(vector<int>& nums) {
        int n = nums.size();
        int res = n;
        
        for (int mask = 1; mask < (1 << n); mask++) {
            vector<int> sums;
            int sum = 0;
            for (int i = 0; i < n; i++) {
                sum += nums[i];
                if ((mask & (1 << i)) != 0) {
                    sums.push_back(sum);
                    sum = 0;
                }
            }
            sums.push_back(sum);
            
            bool valid = true;
            for (int num : sums) {
                int root = sqrt(num);
                if (root * root != num) {
                    valid = false;
                    break;
                }
            }
            
            if (valid) {
                res = min(res, (int)sums.size());
            }
        }
        
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the input array. This is because we are trying all possible splits of the array, and for each split, we are checking if the sum of each subarray is a perfect square.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we need to store the sums of the subarrays.
> - **Why these complexities occur:** The time complexity is exponential because we are trying all possible splits of the array. The space complexity is linear because we need to store the sums of the subarrays.

---

### Optimal Approach (Required)

**Explanation:**
The optimal approach involves using dynamic programming to find the minimum number of subarrays required to split the array such that the sum of the elements in each subarray is a perfect square.

```cpp
class Solution {
public:
    int minSubarrays(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n + 1, n + 1);
        dp[0] = 0;
        
        for (int i = 1; i <= n; i++) {
            int sum = 0;
            for (int j = i; j >= 1; j--) {
                sum += nums[j - 1];
                if (isPerfectSquare(sum)) {
                    dp[i] = min(dp[i], dp[j - 1] + 1);
                }
            }
        }
        
        return dp[n];
    }
    
    bool isPerfectSquare(int num) {
        int root = sqrt(num);
        return root * root == num;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array. This is because we are using dynamic programming to find the minimum number of subarrays required to split the array.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we need to store the minimum number of subarrays required to split the array up to each position.
> - **Optimality proof:** This approach is optimal because we are using dynamic programming to find the minimum number of subarrays required to split the array. We are also checking if the sum of each subarray is a perfect square, which is a necessary condition for the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, perfect squares.
- Problem-solving patterns identified: using dynamic programming to find the minimum number of subarrays required to split the array.
- Optimization techniques learned: using dynamic programming to reduce the time complexity of the problem.
- Similar problems to practice: problems involving dynamic programming and perfect squares.

**Mistakes to Avoid:**
- Common implementation errors: not checking if the sum of each subarray is a perfect square.
- Edge cases to watch for: the input array can be empty, the input array can contain negative numbers.
- Performance pitfalls: using a brute force approach instead of dynamic programming.
- Testing considerations: testing the problem with different input arrays, including edge cases.