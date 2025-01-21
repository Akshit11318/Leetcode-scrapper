## Longest Continuous Increasing Subsequence

**Problem Link:** https://leetcode.com/problems/longest-continuous-increasing-subsequence/description

**Problem Statement:**
- Input format and constraints: Given an unsorted array of integers, find the length of the longest continuous increasing subsequence.
- Expected output format: The length of the longest continuous increasing subsequence.
- Key requirements and edge cases to consider: The subsequence must be continuous, and the array can contain duplicate elements.
- Example test cases with explanations: 
    - Input: `[1,3,5,4,7]`
      Output: `3`
      Explanation: The longest continuous increasing subsequence is `[1,3,5]`.
    - Input: `[2,2,2,2,2]`
      Output: `1`
      Explanation: The longest continuous increasing subsequence is `[2]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One way to solve this problem is to check every possible subsequence of the array and see if it is increasing.
- Step-by-step breakdown of the solution:
    1. Generate all possible subsequences of the array.
    2. For each subsequence, check if it is increasing by comparing each element with its previous element.
    3. Keep track of the longest increasing subsequence found so far.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible solutions.

```cpp
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int n = nums.size();
        int maxLength = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                vector<int> subsequence;
                for (int k = i; k <= j; k++) {
                    subsequence.push_back(nums[k]);
                }
                bool isIncreasing = true;
                for (int k = 0; k < subsequence.size() - 1; k++) {
                    if (subsequence[k] >= subsequence[k + 1]) {
                        isIncreasing = false;
                        break;
                    }
                }
                if (isIncreasing) {
                    maxLength = max(maxLength, (int)subsequence.size());
                }
            }
        }
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. This is because we are generating all possible subsequences of the array, which has $2^n$ possible subsequences, and for each subsequence, we are checking if it is increasing, which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we are storing the subsequence in a vector, which can have at most $n$ elements.
> - **Why these complexities occur:** The brute force approach has high time complexity because it generates all possible subsequences of the array and checks if each one is increasing. The space complexity is relatively low because we only need to store one subsequence at a time.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible subsequences, we can keep track of the length of the longest increasing subsequence ending at each position in the array.
- Detailed breakdown of the approach:
    1. Initialize a vector `dp` of the same length as the input array, where `dp[i]` will store the length of the longest increasing subsequence ending at position `i`.
    2. For each position `i` in the array, check if the previous element is smaller than the current element. If it is, then the length of the longest increasing subsequence ending at position `i` is one more than the length of the longest increasing subsequence ending at position `i - 1`.
    3. Otherwise, the length of the longest increasing subsequence ending at position `i` is 1.
- Proof of optimality: This approach is optimal because it only needs to iterate through the array once, and it keeps track of the length of the longest increasing subsequence ending at each position, which allows it to find the longest continuous increasing subsequence.

```cpp
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        int n = nums.size();
        vector<int> dp(n, 1);
        int maxLength = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                dp[i] = dp[i - 1] + 1;
            }
            maxLength = max(maxLength, dp[i]);
        }
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we only need to iterate through the array once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we need to store the length of the longest increasing subsequence ending at each position in the array.
> - **Optimality proof:** This approach is optimal because it only needs to iterate through the array once, and it keeps track of the length of the longest increasing subsequence ending at each position, which allows it to find the longest continuous increasing subsequence.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, iteration through an array.
- Problem-solving patterns identified: Keeping track of the length of the longest increasing subsequence ending at each position in the array.
- Optimization techniques learned: Instead of generating all possible subsequences, keep track of the length of the longest increasing subsequence ending at each position.
- Similar problems to practice: Longest Increasing Subsequence, Shortest Path.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` vector correctly, not updating the `maxLength` variable correctly.
- Edge cases to watch for: Empty input array, array with only one element.
- Performance pitfalls: Generating all possible subsequences, not using dynamic programming.
- Testing considerations: Test with different input arrays, including edge cases.