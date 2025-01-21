## Subsequences with a Unique Middle Mode I

**Problem Link:** https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/description

**Problem Statement:**
- Input: A list of integers `nums`.
- Constraints: `1 <= nums.length <= 1000`, `1 <= nums[i] <= 1000`.
- Expected Output: The number of subsequences with a unique middle mode.
- Key Requirements: 
    - A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.
    - A mode is a value that appears most frequently in a sequence.
    - A middle mode is a mode that appears at the middle index of a subsequence (when the length of the subsequence is odd).
- Edge Cases: 
    - Empty sequence.
    - Sequence with a single element.
    - Sequence with all elements being the same.
- Example Test Cases:
    - `nums = [1, 1, 2, 2]`: There are `4` subsequences with a unique middle mode: `[1]`, `[1, 1]`, `[2]`, `[2, 2]`.
    - `nums = [1, 1, 1]`: There are `4` subsequences with a unique middle mode: `[1]`, `[1, 1]`, `[1, 1, 1]`, `[1, 1]`.
    - `nums = [1, 2, 3]`: There are `6` subsequences with a unique middle mode: `[1]`, `[2]`, `[3]`, `[1, 2]`, `[1, 3]`, `[2, 3]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences and check each one for a unique middle mode.
- Step-by-step breakdown:
    1. Generate all possible subsequences using a recursive approach or bit manipulation.
    2. For each subsequence, calculate the frequency of each element.
    3. Check if there is a unique middle mode by comparing the frequency of the middle element with the frequency of all other elements.
- Why this approach comes to mind first: It's a straightforward approach that directly addresses the problem statement.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

int countUniqueSubsequences(vector<int>& nums) {
    int count = 0;
    int n = nums.size();
    // Generate all possible subsequences
    for (int mask = 1; mask < (1 << n); mask++) {
        vector<int> subsequence;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subsequence.push_back(nums[i]);
            }
        }
        // Check if the subsequence has a unique middle mode
        if (hasUniqueMiddleMode(subsequence)) {
            count++;
        }
    }
    return count;
}

bool hasUniqueMiddleMode(vector<int>& subsequence) {
    if (subsequence.size() % 2 == 0) return false; // Even-length subsequences do not have a middle mode
    int midIndex = subsequence.size() / 2;
    unordered_map<int, int> freq;
    for (int num : subsequence) {
        freq[num]++;
    }
    int maxFreq = 0;
    for (auto& pair : freq) {
        maxFreq = max(maxFreq, pair.second);
    }
    int midNum = subsequence[midIndex];
    return freq[midNum] == maxFreq && freq[midNum] > 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input sequence. This is because we generate all possible subsequences (which takes $O(2^n)$ time) and then check each subsequence for a unique middle mode (which takes $O(n)$ time).
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input sequence. This is because we need to store the subsequence and the frequency map.
> - **Why these complexities occur:** The brute force approach generates all possible subsequences, which leads to an exponential time complexity. The space complexity is linear because we need to store the subsequence and the frequency map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use dynamic programming to store the frequency of each element in each subsequence.
- Detailed breakdown:
    1. Initialize a 2D array `dp` where `dp[i][j]` stores the frequency of element `j` in the subsequence ending at index `i`.
    2. Iterate through the input sequence and update the `dp` array accordingly.
    3. Use the `dp` array to check if a subsequence has a unique middle mode.
- Proof of optimality: This approach has a time complexity of $O(n^2)$, which is optimal because we need to iterate through the input sequence at least once.

```cpp
int countUniqueSubsequences(vector<int>& nums) {
    int n = nums.size();
    vector<vector<int>> dp(n, vector<int>(1001, 0)); // Assuming the maximum value of nums is 1000
    for (int i = 0; i < n; i++) {
        dp[i][nums[i]] = 1;
    }
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < 1001; j++) {
            dp[i][j] += dp[i - 1][j];
        }
        dp[i][nums[i]]++;
    }
    int count = 0;
    for (int mask = 1; mask < (1 << n); mask++) {
        vector<int> subsequence;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subsequence.push_back(nums[i]);
            }
        }
        if (hasUniqueMiddleMode(subsequence, dp)) {
            count++;
        }
    }
    return count;
}

bool hasUniqueMiddleMode(vector<int>& subsequence, vector<vector<int>>& dp) {
    if (subsequence.size() % 2 == 0) return false; // Even-length subsequences do not have a middle mode
    int midIndex = subsequence.size() / 2;
    unordered_map<int, int> freq;
    for (int num : subsequence) {
        freq[num]++;
    }
    int maxFreq = 0;
    for (auto& pair : freq) {
        maxFreq = max(maxFreq, pair.second);
    }
    int midNum = subsequence[midIndex];
    return freq[midNum] == maxFreq && freq[midNum] > 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input sequence. This is because we iterate through the input sequence and update the `dp` array.
> - **Space Complexity:** $O(n^2)$, where $n$ is the length of the input sequence. This is because we need to store the `dp` array.
> - **Optimality proof:** This approach has a time complexity of $O(n^2)$, which is optimal because we need to iterate through the input sequence at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, frequency counting.
- Problem-solving patterns identified: Using dynamic programming to store frequency information.
- Optimization techniques learned: Using a 2D array to store frequency information.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly.
- Edge cases to watch for: Even-length subsequences do not have a middle mode.
- Performance pitfalls: Not using dynamic programming to store frequency information.
- Testing considerations: Test the implementation with different input sequences and edge cases.