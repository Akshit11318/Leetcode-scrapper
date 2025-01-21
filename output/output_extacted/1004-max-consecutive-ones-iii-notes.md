## Max Consecutive Ones III
**Problem Link:** https://leetcode.com/problems/max-consecutive-ones-iii/description

**Problem Statement:**
- Input: An array of integers `A` and an integer `K`.
- Constraints: `1 <= A.length <= 10^5`, `1 <= K <= A.length`, `A[i]` is either `0` or `1`.
- Expected Output: The maximum number of consecutive ones in an array if you can flip at most `K` zeros.
- Key Requirements: Find the longest subarray that contains at most `K` zeros.
- Example Test Cases:
  - Input: `A = [1,1,1,0,0,0,1,1,1,1,0]`, `K = 2`
  - Output: `6`
  - Explanation: You can flip two zeros in the subarray `[1,1,1,0,0,1]` to get six consecutive ones.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For every possible subarray, count the number of zeros. If the count of zeros is less than or equal to `K`, calculate the length of the subarray.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays.
  2. For each subarray, count the number of zeros.
  3. If the number of zeros is less than or equal to `K`, calculate the length of the subarray.
  4. Keep track of the maximum length found so far.

```cpp
class Solution {
public:
    int longestOnes(vector<int>& A, int K) {
        int n = A.size();
        int maxLength = 0;
        
        for (int i = 0; i < n; i++) {
            int zeros = 0;
            for (int j = i; j < n; j++) {
                if (A[j] == 0) zeros++;
                if (zeros <= K) {
                    maxLength = max(maxLength, j - i + 1);
                }
            }
        }
        
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the array `A`. This is because for each element in `A`, we potentially scan the rest of the array.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, as we only use a constant amount of space.
> - **Why these complexities occur:** The brute force approach involves generating all possible subarrays and checking each one, leading to a quadratic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a sliding window approach to efficiently scan the array and keep track of the number of zeros within the current window.
- Detailed breakdown:
  1. Initialize two pointers, `left` and `right`, to represent the sliding window.
  2. Expand the window to the right by incrementing `right`.
  3. If a zero is encountered, increment a `zeros` counter.
  4. When the number of zeros exceeds `K`, shrink the window from the left by incrementing `left` until the number of zeros is less than or equal to `K`.
  5. Keep track of the maximum length of the window seen so far.

```cpp
class Solution {
public:
    int longestOnes(vector<int>& A, int K) {
        int n = A.size();
        int maxLength = 0;
        int zeros = 0;
        int left = 0;
        
        for (int right = 0; right < n; right++) {
            if (A[right] == 0) zeros++;
            while (zeros > K) {
                if (A[left] == 0) zeros--;
                left++;
            }
            maxLength = max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array `A`, because each element is visited at most twice (once by `right` and once by `left`).
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it ensures that we consider all possible subarrays with at most `K` zeros in a single pass through the array, without redundant calculations.

---

### Final Notes

**Learning Points:**
- The importance of the sliding window technique in solving array and string problems.
- How to apply the sliding window technique to problems involving constraints on subarrays.
- The trade-off between brute force and optimal solutions in terms of time complexity.

**Mistakes to Avoid:**
- Failing to consider the edge case where `K` equals the length of the array.
- Not initializing variables correctly before use.
- Not updating the `maxLength` variable correctly within the loop.

This problem demonstrates the power of the sliding window technique in solving problems that involve finding the maximum or minimum of some property (in this case, length) within a subarray that satisfies certain constraints. By efficiently scanning the array and adjusting the window boundaries based on the constraints, we can achieve a significant reduction in time complexity compared to brute force approaches.