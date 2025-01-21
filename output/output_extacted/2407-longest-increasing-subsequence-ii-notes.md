## Longest Increasing Subsequence II

**Problem Link:** https://leetcode.com/problems/longest-increasing-subsequence-ii/description

**Problem Statement:**
- Input format and constraints: Given a list of integers `nums`, find the length of the longest increasing subsequence where each element is used at most once.
- Expected output format: The length of the longest increasing subsequence.
- Key requirements and edge cases to consider: The input list can be empty, and the integers can be negative or positive.
- Example test cases with explanations:
  - `nums = [10, 9, 2, 5, 3, 7, 101, 18]`: The longest increasing subsequence is `[2, 3, 7, 101]`, so the output is `4`.
  - `nums = [0, 1, 0, 3, 2, 3]`: The longest increasing subsequence is `[0, 1, 2, 3]`, so the output is `4`.
  - `nums = [7, 7, 7, 7]`: The longest increasing subsequence is `[7]`, so the output is `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible subsequences of the input list and check if they are increasing.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of the input list.
  2. For each subsequence, check if it is increasing by comparing each element with its previous element.
  3. Keep track of the length of the longest increasing subsequence found so far.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that checks all possible solutions.

```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        int maxLength = 0;
        for (int mask = 1; mask < (1 << n); mask++) {
            vector<int> subsequence;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    subsequence.push_back(nums[i]);
                }
            }
            if (isIncreasing(subsequence)) {
                maxLength = max(maxLength, (int)subsequence.size());
            }
        }
        return maxLength;
    }

    bool isIncreasing(vector<int>& subsequence) {
        for (int i = 1; i < subsequence.size(); i++) {
            if (subsequence[i] <= subsequence[i - 1]) {
                return false;
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input list. This is because we generate all possible subsequences of the input list, and for each subsequence, we check if it is increasing.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input list. This is because we store the subsequence in a vector.
> - **Why these complexities occur:** The time complexity occurs because we generate all possible subsequences of the input list, and the space complexity occurs because we store the subsequence in a vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the length of the longest increasing subsequence ending at each position.
- Detailed breakdown of the approach:
  1. Initialize a vector `dp` of length `n`, where `dp[i]` stores the length of the longest increasing subsequence ending at position `i`.
  2. For each position `i`, iterate over all previous positions `j` and update `dp[i]` if the subsequence ending at position `i` is increasing.
  3. The length of the longest increasing subsequence is the maximum value in the `dp` vector.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible increasing subsequences, and the time complexity is optimal because we only iterate over the input list once.

```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) {
            return 0;
        }
        vector<int> dp(n, 1);
        int maxLength = 1;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            maxLength = max(maxLength, dp[i]);
        }
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input list. This is because we iterate over the input list once and for each position, we iterate over all previous positions.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input list. This is because we store the `dp` vector.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible increasing subsequences, and the time complexity is optimal because we only iterate over the input list once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, iteration over all possible subsequences.
- Problem-solving patterns identified: Using dynamic programming to store the length of the longest increasing subsequence ending at each position.
- Optimization techniques learned: Using dynamic programming to reduce the time complexity from exponential to quadratic.
- Similar problems to practice: Longest decreasing subsequence, longest common subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` vector correctly, not updating the `dp` vector correctly.
- Edge cases to watch for: Empty input list, input list with negative numbers.
- Performance pitfalls: Using the brute force approach for large input lists.
- Testing considerations: Testing the solution with different input lists, including edge cases.