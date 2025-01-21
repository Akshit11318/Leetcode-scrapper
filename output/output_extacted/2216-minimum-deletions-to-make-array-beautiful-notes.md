## Minimum Deletions to Make Array Beautiful
**Problem Link:** https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/description

**Problem Statement:**
- Given an integer array `nums`, return the minimum number of deletions required to make the array beautiful.
- An array is considered beautiful if for every `i` in the range `[1, n - 1]`, `nums[i]` equals `nums[i - 1]` or `nums[i] + 1` equals `nums[i - 1]`.
- The input array `nums` has `n` integers in the range `[1, 100]`.
- The expected output is the minimum number of deletions required to make the array beautiful.

**Example Test Cases:**
- Input: `nums = [1, 2, 3, 4, 5]`
  - Output: `0` because the array is already beautiful.
- Input: `nums = [1, 1, 2, 3, 3, 3, 4, 5, 6, 7]`
  - Output: `2` because we can delete the first `1` and the second `3` to make the array beautiful.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to consider all possible subsets of the array and check if they are beautiful.
- This involves generating all possible subsets, checking each subset to see if it meets the condition of being beautiful, and keeping track of the minimum number of deletions required.
- This approach comes to mind first because it exhaustively considers all possibilities.

```cpp
#include <vector>
#include <algorithm>

int minDeletion(vector<int>& nums) {
    int n = nums.size();
    int minDeletions = n; // Initialize with the maximum possible deletions

    // Generate all possible subsets
    for (int mask = 0; mask < (1 << n); ++mask) {
        vector<int> subset;
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) != 0) {
                subset.push_back(nums[i]);
            }
        }

        // Check if the subset is beautiful
        bool isBeautiful = true;
        for (int i = 1; i < subset.size(); ++i) {
            if (subset[i] != subset[i - 1] && subset[i] - 1 != subset[i - 1]) {
                isBeautiful = false;
                break;
            }
        }

        // Update the minimum number of deletions if the subset is beautiful
        if (isBeautiful) {
            minDeletions = min(minDeletions, n - subset.size());
        }
    }

    return minDeletions;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the size of the input array. This is because we generate $2^n$ subsets and for each subset, we perform a check that takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, as we need to store each subset.
> - **Why these complexities occur:** The brute force approach is inherently expensive because it considers all possible subsets of the input array, leading to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to keep track of the longest beautiful subsequence ending at each position.
- We maintain two arrays, `dp` and `prev`, where `dp[i]` stores the length of the longest beautiful subsequence ending at index `i`, and `prev[i]` stores the previous index in this subsequence.
- We iterate through the array, updating `dp` and `prev` based on whether the current element can extend the beautiful subsequence ending at the previous index.
- Finally, we find the maximum length of the beautiful subsequence and subtract it from the total length of the array to get the minimum number of deletions required.

```cpp
#include <vector>
#include <algorithm>

int minDeletion(vector<int>& nums) {
    int n = nums.size();
    vector<int> dp(n, 1); // Initialize dp with 1s
    vector<int> prev(n, -1); // Initialize prev with -1s

    int maxLength = 1; // Initialize maxLength
    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if ((nums[i] == nums[j] || nums[i] == nums[j] + 1) && dp[i] < dp[j] + 1) {
                dp[i] = dp[j] + 1;
                prev[i] = j;
            }
        }
        maxLength = max(maxLength, dp[i]);
    }

    return n - maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array. This is because we have a nested loop structure.
> - **Space Complexity:** $O(n)$, as we need to store the `dp` and `prev` arrays.
> - **Optimality proof:** This approach is optimal because it considers all possible beautiful subsequences in a single pass, avoiding the exponential complexity of the brute force approach.

---

### Final Notes

**Learning Points:**
- The importance of dynamic programming in solving problems that involve finding optimal subsequences.
- How to identify and apply the concept of beautiful arrays.
- The trade-off between brute force and dynamic programming approaches.

**Mistakes to Avoid:**
- Not considering all possible subsets or subsequences.
- Failing to update the dynamic programming tables correctly.
- Not handling edge cases properly, such as empty arrays or arrays with a single element.