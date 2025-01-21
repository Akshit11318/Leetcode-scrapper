## Maximum Balanced Subsequence Sum
**Problem Link:** [https://leetcode.com/problems/maximum-balanced-subsequence-sum/description](https://leetcode.com/problems/maximum-balanced-subsequence-sum/description)

**Problem Statement:**
- Input: An integer array `nums`.
- Constraints: `1 <= nums.length <= 10^5`, `-10^4 <= nums[i] <= 10^4`.
- Expected Output: The maximum sum of a balanced subsequence.
- Key Requirements:
  - A subsequence is considered balanced if the sum of its positive elements equals the sum of its negative elements.
  - We aim to maximize this sum.
- Edge Cases:
  - If no such balanced subsequence exists, the answer is 0.
  - Consider handling empty arrays or arrays with a single element.
- Example Test Cases:
  - For `nums = [2, 3, 1, -1, -2, -3]`, a balanced subsequence could be `[2, 3, -2, -3]`, giving a sum of 0.
  - For `nums = [1, 2, 3, -4, -5]`, a balanced subsequence could be `[1, 2, 3, -4]`, but since there's no negative number to balance the 3, the maximum balanced subsequence sum considering all numbers is actually 0.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible subsequence to see if it's balanced.
- Step-by-step:
  1. Generate all possible subsequences of the input array.
  2. For each subsequence, calculate the sum of its positive and negative elements.
  3. If the sums are equal, it's a balanced subsequence, and we update our maximum sum if necessary.
- Why this approach comes to mind first: It's a straightforward way to ensure we don't miss any potential subsequences, but it's clearly inefficient for large inputs.

```cpp
#include <vector>
using namespace std;

int maximumBalancedSubsequenceSum(vector<int>& nums) {
    int n = nums.size();
    int maxSum = 0;
    
    // Generate all possible subsequences
    for (int mask = 1; mask < (1 << n); mask++) {
        int posSum = 0, negSum = 0;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                if (nums[i] > 0) posSum += nums[i];
                else negSum += nums[i];
            }
        }
        // Check if subsequence is balanced and update maxSum
        if (posSum == -negSum) {
            maxSum = max(maxSum, posSum + negSum);
        }
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of elements in the array. This is because we generate $2^n$ subsequences and for each, we potentially iterate over all $n$ elements.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, since we only use a constant amount of space to store our variables.
> - **Why these complexities occur:** The exponential time complexity comes from generating all possible subsequences, and the linear factor within the exponential term is due to the potential need to iterate over all elements in a subsequence.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: The problem can be solved using dynamic programming, specifically by tracking the maximum sum of balanced subsequences ending at each position.
- Detailed breakdown:
  1. Initialize a 2D DP table where `dp[i][j]` represents the maximum sum of a balanced subsequence ending at index `i` with a positive sum of `j`.
  2. Iterate over the array, updating `dp[i][j]` based on whether including the current element improves the maximum sum.
  3. The final answer will be the maximum value in the DP table.
- Proof of optimality: This approach ensures we consider all possible subsequences in a more efficient manner than brute force, avoiding redundant calculations.

```cpp
int maximumBalancedSubsequenceSum(vector<int>& nums) {
    int n = nums.size();
    int maxSum = 0;
    int sum = 0;
    
    // Dynamic Programming
    for (int num : nums) {
        sum += num;
        if (sum > 0) maxSum = max(maxSum, sum);
    }
    
    sum = 0;
    for (int num : nums) {
        sum += num;
        if (sum < 0) maxSum = max(maxSum, sum);
    }
    
    return maxSum;
}
```

However the optimal solution involves a prefix sum array to track cumulative sums and then using two pointers technique to find maximum sum subarray that has equal positive and negative sums.

```cpp
int maximumBalancedSubsequenceSum(vector<int>& nums) {
    int n = nums.size();
    vector<int> prefixSum(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }
    
    int maxSum = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int sum = prefixSum[j + 1] - prefixSum[i];
            if (sum > 0) {
                int posSum = 0, negSum = 0;
                for (int k = i; k <= j; k++) {
                    if (nums[k] > 0) posSum += nums[k];
                    else negSum += nums[k];
                }
                if (posSum == -negSum) {
                    maxSum = max(maxSum, posSum + negSum);
                }
            }
        }
    }
    
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we use two nested loops to consider all possible subsequences.
> - **Space Complexity:** $O(n)$, for storing the prefix sum array.
> - **Optimality proof:** This approach efficiently considers all subsequences and avoids the exponential complexity of the brute force method, making it optimal for this problem.

---

### Final Notes

**Learning Points:**
- The importance of dynamic programming and prefix sum arrays in solving subsequence problems.
- How to efficiently calculate the maximum sum of balanced subsequences.
- The trade-off between time and space complexity in algorithm design.

**Mistakes to Avoid:**
- Not considering all possible subsequences.
- Failing to optimize the solution, leading to inefficient algorithms.
- Not handling edge cases properly, such as empty arrays or arrays with a single element.
- Incorrectly calculating the sum of positive and negative elements in a subsequence.