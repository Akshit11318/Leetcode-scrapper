## Alternating Groups II

**Problem Link:** https://leetcode.com/problems/alternating-groups-ii/description

**Problem Statement:**
- Input: A binary array `nums` of length `n`.
- Constraints: `1 <= n <= 10^5`, `nums[i]` is either `0` or `1`.
- Expected Output: The length of the longest alternating subsequence.
- Key Requirements: Find the longest subsequence where each element is different from its previous one.
- Edge Cases: Handle sequences with all `0`s or all `1`s, and sequences with a single element.
- Example Test Cases:
  - `nums = [0,1,0,1,0,1,0,1]`, Expected Output: `8`.
  - `nums = [1,1,0,0,1,1,0,0]`, Expected Output: `4`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subsequence to see if it alternates.
- Step-by-step breakdown:
  1. Generate all possible subsequences of the input array.
  2. For each subsequence, check if it alternates by comparing each element with its previous one.
  3. Keep track of the longest alternating subsequence found.
- This approach comes to mind first because it directly addresses the problem statement without considering optimizations.

```cpp
class Solution {
public:
    int longestAlternatingSubsequence(vector<int>& nums) {
        int n = nums.size();
        int maxLength = 0;
        
        // Generate all possible subsequences
        for (int mask = 1; mask < (1 << n); mask++) {
            vector<int> subsequence;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i))) {
                    subsequence.push_back(nums[i]);
                }
            }
            
            // Check if the subsequence alternates
            bool alternates = true;
            for (int i = 1; i < subsequence.size(); i++) {
                if (subsequence[i] == subsequence[i-1]) {
                    alternates = false;
                    break;
                }
            }
            
            if (alternates) {
                maxLength = max(maxLength, (int)subsequence.size());
            }
        }
        
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. This is because we generate $2^n$ subsequences and for each, we potentially check all $n$ elements.
> - **Space Complexity:** $O(n)$, for storing the current subsequence being checked.
> - **Why these complexities occur:** The brute force approach involves checking every possible subsequence, which leads to an exponential number of operations. The space complexity is linear because we only need to store one subsequence at a time.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all subsequences, we can use dynamic programming to keep track of the longest alternating subsequences ending at each position.
- Detailed breakdown:
  1. Initialize two arrays, `dp0` and `dp1`, where `dp0[i]` is the length of the longest alternating subsequence ending at `i` with `0`, and `dp1[i]` is the length of the longest alternating subsequence ending at `i` with `1`.
  2. Iterate through the input array. For each element, update `dp0` and `dp1` based on whether the current element is `0` or `1`.
  3. The length of the longest alternating subsequence is the maximum value in `dp0` and `dp1`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input array, resulting in a linear time complexity.

```cpp
class Solution {
public:
    int longestAlternatingSubsequence(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp0(n, 1), dp1(n, 1);
        
        for (int i = 1; i < n; i++) {
            if (nums[i] == 0) {
                dp0[i] = max(dp0[i], dp1[i-1] + 1);
            } else {
                dp1[i] = max(dp1[i], dp0[i-1] + 1);
            }
        }
        
        int maxLength = 0;
        for (int i = 0; i < n; i++) {
            maxLength = max(maxLength, max(dp0[i], dp1[i]));
        }
        
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we make a single pass through the array.
> - **Space Complexity:** $O(n)$, for storing the `dp0` and `dp1` arrays.
> - **Optimality proof:** This approach is optimal because it achieves the best possible time complexity for the problem, which is linear. It only requires a single pass through the input array and uses a constant amount of extra space per element.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming for solving problems with overlapping subproblems.
- Problem-solving patterns identified: Using arrays to keep track of solutions to subproblems.
- Optimization techniques learned: Avoiding redundant computations by storing solutions to subproblems.
- Similar problems to practice: Other dynamic programming problems involving sequences or arrays.

**Mistakes to Avoid:**
- Common implementation errors: Failing to initialize arrays or variables correctly.
- Edge cases to watch for: Handling sequences with all `0`s or all `1`s, and sequences with a single element.
- Performance pitfalls: Using brute force approaches for problems that can be solved more efficiently with dynamic programming.
- Testing considerations: Testing with a variety of input sequences, including edge cases.