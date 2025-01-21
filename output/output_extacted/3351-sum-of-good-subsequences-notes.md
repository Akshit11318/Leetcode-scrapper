## Sum of Good Subsequences
**Problem Link:** https://leetcode.com/problems/sum-of-good-subsequences/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums`, return the sum of all the good subsequences of `nums`. A good subsequence is a sequence that starts with a 0, ends with a 0, and has at least one 1 in it.
- Expected output format: The sum of all good subsequences.
- Key requirements and edge cases to consider: 
  - Empty array
  - Array with no zeros
  - Array with no ones
- Example test cases with explanations:
  - `[1, 0, 1]`: One good subsequence is `[0]`, but since it does not contain a 1, the sum is `0`.
  - `[1, 0, 1, 0, 1]`: Good subsequences include `[0, 1, 0]`, `[0, 1, 0, 1, 0]`, etc.

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of the array and check each one to see if it starts and ends with a 0 and contains at least one 1.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of the input array.
  2. For each subsequence, check if it starts and ends with a 0 and contains at least one 1.
  3. If a subsequence meets these conditions, add the sum of its elements to the total sum.
- Why this approach comes to mind first: It's a straightforward way to ensure all possible subsequences are considered.

```cpp
#include <vector>
#include <numeric>

int sumGoodSubsequences(std::vector<int>& nums) {
    int n = nums.size();
    int totalSum = 0;
    
    // Generate all possible subsequences
    for (int mask = 0; mask < (1 << n); ++mask) {
        std::vector<int> subsequence;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                subsequence.push_back(nums[i]);
            }
        }
        
        // Check if the subsequence is good
        if (!subsequence.empty() && subsequence[0] == 0 && subsequence.back() == 0) {
            bool hasOne = false;
            for (int num : subsequence) {
                if (num == 1) {
                    hasOne = true;
                    break;
                }
            }
            if (hasOne) {
                totalSum += std::accumulate(subsequence.begin(), subsequence.end(), 0);
            }
        }
    }
    
    return totalSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the input array. The reason is that we generate $2^n$ subsequences and for each, we potentially iterate through all $n$ elements to check the conditions and sum the elements.
> - **Space Complexity:** $O(n)$, because in the worst case, we might store a subsequence of size $n$.
> - **Why these complexities occur:** The brute force approach involves generating all possible subsequences, which inherently leads to exponential time complexity. The space complexity is linear because we only need to store one subsequence at a time.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all subsequences, we can use dynamic programming to keep track of the sum of good subsequences ending at each position.
- Detailed breakdown of the approach:
  1. Initialize a dynamic programming table `dp` where `dp[i]` represents the sum of good subsequences ending at index `i`.
  2. Iterate through the array, updating `dp[i]` based on whether the current element is 0 or 1 and the values of previous elements.
  3. Finally, sum up all the values in the `dp` table to get the total sum of good subsequences.
- Proof of optimality: This approach avoids the exponential complexity of generating all subsequences by only considering the relevant information (the sum of good subsequences ending at each position).

```cpp
int sumGoodSubsequences(std::vector<int>& nums) {
    int n = nums.size();
    int totalSum = 0;
    int mod = 1e9 + 7;
    
    std::vector<int> dp(n, 0);
    for (int i = 0; i < n; ++i) {
        if (nums[i] == 0) {
            // For a 0, consider all previous 1s and the current 0
            for (int j = 0; j < i; ++j) {
                if (nums[j] == 1) {
                    dp[i] = (dp[i] + dp[j] + 1) % mod;
                }
            }
        } else {
            // For a 1, consider all previous good subsequences
            for (int j = 0; j < i; ++j) {
                if (nums[j] == 0) {
                    dp[i] = (dp[i] + dp[j]) % mod;
                }
            }
        }
        totalSum = (totalSum + dp[i]) % mod;
    }
    
    return totalSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, because for each element, we potentially iterate through all previous elements.
> - **Space Complexity:** $O(n)$, for storing the dynamic programming table.
> - **Optimality proof:** This approach is optimal because it avoids the exponential complexity of the brute force approach by only considering the necessary information for each element, leading to a polynomial time complexity.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, avoiding brute force by considering only relevant information.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and solving them efficiently.
- Optimization techniques learned: Using dynamic programming to store and reuse the results of sub-problems.
- Similar problems to practice: Other dynamic programming problems involving sequences or arrays.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect initialization of the dynamic programming table, forgetting to update the table correctly.
- Edge cases to watch for: Empty array, array with no zeros or ones.
- Performance pitfalls: Using the brute force approach for large inputs.
- Testing considerations: Thoroughly test the function with various inputs, including edge cases.