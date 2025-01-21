## Longest Arithmetic Subsequence

**Problem Link:** https://leetcode.com/problems/longest-arithmetic-subsequence/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums`, find the length of the longest arithmetic subsequence.
- Expected output format: The length of the longest arithmetic subsequence.
- Key requirements and edge cases to consider: The subsequence must have at least two elements, and the difference between any two successive elements must be constant.
- Example test cases with explanations:
  - `nums = [3,6,9,12]`: The longest arithmetic subsequence is `[3,6,9,12]`, with a common difference of `3`.
  - `nums = [9,4,7,2,10]`: The longest arithmetic subsequence is `[4,7,10]`, with a common difference of `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences and check if each one is an arithmetic sequence.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of the input array.
  2. For each subsequence, calculate the differences between consecutive elements.
  3. Check if all differences are equal. If they are, it's an arithmetic sequence.
  4. Keep track of the longest arithmetic subsequence found.
- Why this approach comes to mind first: It's a straightforward way to solve the problem, but it's not efficient for large inputs.

```cpp
#include <vector>
using namespace std;

int longestArithmeticSubsequence(vector<int>& nums) {
    int n = nums.size();
    int maxLength = 0;
    for (int mask = 1; mask < (1 << n); mask++) {
        vector<int> subsequence;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subsequence.push_back(nums[i]);
            }
        }
        if (subsequence.size() < 2) continue;
        bool isArithmetic = true;
        int diff = subsequence[1] - subsequence[0];
        for (int i = 2; i < subsequence.size(); i++) {
            if (subsequence[i] - subsequence[i-1] != diff) {
                isArithmetic = false;
                break;
            }
        }
        if (isArithmetic) {
            maxLength = max(maxLength, (int)subsequence.size());
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. This is because we generate all possible subsequences and check each one.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we store each subsequence.
> - **Why these complexities occur:** The brute force approach has high time complexity because it generates all possible subsequences, which is exponential in the length of the input array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to store the length of the longest arithmetic subsequence ending at each position with a given difference.
- Detailed breakdown of the approach:
  1. Initialize a map to store the length of the longest arithmetic subsequence ending at each position with a given difference.
  2. Iterate over the input array and for each element, iterate over all previous elements.
  3. Calculate the difference between the current element and the previous element.
  4. Update the length of the longest arithmetic subsequence ending at the current position with the given difference.
  5. Keep track of the maximum length found.
- Proof of optimality: This approach has a time complexity of $O(n^2)$, which is optimal because we need to compare each pair of elements.

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

int longestArithmeticSubsequence(vector<int>& nums) {
    int n = nums.size();
    int maxLength = 0;
    unordered_map<int, unordered_map<int, int>> dp;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            int diff = nums[i] - nums[j];
            dp[i][diff] = dp[j].count(diff) ? dp[j][diff] + 1 : 2;
            maxLength = max(maxLength, dp[i][diff]);
        }
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we iterate over the input array and for each element, we iterate over all previous elements.
> - **Space Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we store the length of the longest arithmetic subsequence ending at each position with a given difference.
> - **Optimality proof:** This approach is optimal because we need to compare each pair of elements to find the longest arithmetic subsequence.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, iteration over the input array.
- Problem-solving patterns identified: Using a map to store the length of the longest arithmetic subsequence ending at each position with a given difference.
- Optimization techniques learned: Reducing the time complexity from exponential to quadratic.
- Similar problems to practice: Longest increasing subsequence, longest common subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the map correctly, not updating the maximum length correctly.
- Edge cases to watch for: Empty input array, input array with a single element.
- Performance pitfalls: Using a brute force approach with high time complexity.
- Testing considerations: Test the solution with different input arrays, including edge cases.