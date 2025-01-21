## Length of the Longest Subsequence that Sums to Target
**Problem Link:** https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/description

**Problem Statement:**
- Input: An array of integers `arr` and an integer `target`.
- Constraints: $1 \leq n \leq 10^5$, $-10^5 \leq arr_i \leq 10^5$, and $-10^9 \leq target \leq 10^9$.
- Expected Output: The length of the longest subsequence that sums up to `target`.
- Key Requirements: 
  - A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.
  - The subsequence must sum exactly to `target`.
- Example Test Cases:
  - For `arr = [1,2,3,4,5]` and `target = 5`, the longest subsequence that sums up to `target` is `[2,3]`, so the answer is `2`.
  - For `arr = [1,2,3,7,9,5,10]` and `target = 12`, the longest subsequence that sums up to `target` is `[2,3,7]`, so the answer is `3`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible subsequences of the given array and check each one to see if its sum equals the target.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences using bit manipulation (each bit corresponds to whether an element is included in the subsequence or not).
  2. For each subsequence, calculate its sum.
  3. If the sum equals the target, update the maximum length found so far.
- Why this approach comes to mind first: It's straightforward and ensures that all possibilities are considered.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int longestSubsequence(vector<int>& arr, int target) {
    int n = arr.size();
    int maxLen = 0;
    
    for (int mask = 0; mask < (1 << n); ++mask) {
        int sum = 0;
        int len = 0;
        
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) != 0) {
                sum += arr[i];
                len++;
            }
        }
        
        if (sum == target) {
            maxLen = max(maxLen, len);
        }
    }
    
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, because we generate $2^n$ subsequences and for each, we potentially iterate through all $n$ elements to calculate its sum.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, as we only use a constant amount of space to store the current subsequence sum and the maximum length found.
> - **Why these complexities occur:** The exponential time complexity is due to generating all possible subsequences, and the linear factor within the exponential is due to calculating the sum of each subsequence.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Use dynamic programming to store the lengths of the longest subsequences that sum up to each possible value up to the target.
- Detailed breakdown of the approach:
  1. Initialize a dynamic programming table `dp` of size `target + 1` with all elements set to 0, except for `dp[0]` which is set to 0 (since the sum of 0 can be achieved with an empty subsequence).
  2. Iterate through each element in the array.
  3. For each element, update the `dp` table in reverse order to avoid overwriting previously computed values.
  4. The value at `dp[target]` will represent the length of the longest subsequence that sums up to the target.
- Proof of optimality: This approach ensures that we consider all possible subsequences in a more efficient manner than the brute force approach by avoiding redundant calculations and directly storing the results of subproblems.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int longestSubsequence(vector<int>& arr, int target) {
    int n = arr.size();
    vector<int> dp(target + 1, 0);
    dp[0] = 0;
    
    for (int i = 0; i < n; ++i) {
        for (int j = target; j >= arr[i]; --j) {
            if (dp[j - arr[i]] != 0 || j - arr[i] == 0) {
                dp[j] = max(dp[j], dp[j - arr[i]] + 1);
            }
        }
    }
    
    return dp[target];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot target)$, because we iterate through each element in the array and for each element, we potentially update the dynamic programming table up to the target value.
> - **Space Complexity:** $O(target)$, because we use a dynamic programming table of size `target + 1`.
> - **Optimality proof:** This approach is optimal because it solves the problem in polynomial time relative to the input size and the target value, avoiding the exponential complexity of the brute force approach by cleverly using dynamic programming to store and reuse the results of subproblems.