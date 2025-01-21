## Maximum Length of Repeated Subarray

**Problem Link:** https://leetcode.com/problems/maximum-length-of-repeated-subarray/description

**Problem Statement:**
- Input: Two integer arrays `A` and `B`.
- Constraints: `1 <= A.length <= 1000`, `1 <= B.length <= 1000`, `0 <= A[i], B[i] <= 9`.
- Expected output: The length of the longest common subarray between `A` and `B`.
- Key requirements: Find the maximum length of a contiguous subarray common to both `A` and `B`.
- Example test cases:
  - `A = [1,2,3,2,1]`, `B = [3,2,1,4,7]`, Output: `3` because `[1,2,3]` is the longest common subarray.
  - `A = [0,0,0,0,0]`, `B = [0,0,0,0,0]`, Output: `5` because the entire array is common.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subarray of `A` against every possible subarray of `B`.
- Step-by-step breakdown:
  1. Generate all possible subarrays for `A` and `B`.
  2. Compare each subarray of `A` with each subarray of `B`.
  3. Keep track of the maximum length of matching subarrays.
- Why this approach comes to mind first: It is straightforward and ensures that no possible common subarray is overlooked.

```cpp
int findLength(vector<int>& A, vector<int>& B) {
    int maxLen = 0;
    for (int i = 0; i < A.size(); i++) {
        for (int j = 0; j < B.size(); j++) {
            int k = 0;
            while (i + k < A.size() && j + k < B.size() && A[i + k] == B[j + k]) {
                k++;
            }
            maxLen = max(maxLen, k);
        }
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m^2)$, where $n$ and $m$ are the sizes of `A` and `B`, respectively. This is because for each element in `A`, we potentially compare with each element in `B`, and for each comparison, we might check up to the length of the smaller array.
> - **Space Complexity:** $O(1)$, excluding the input arrays, as we only use a constant amount of space to store the maximum length and indices.
> - **Why these complexities occur:** The nested loops over `A` and `B` and the inner while loop checking for matches contribute to the high time complexity. The space complexity is low because we do not allocate any additional data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Utilize dynamic programming to efficiently compute the lengths of common subarrays.
- Detailed breakdown:
  1. Create a 2D array `dp` where `dp[i][j]` represents the length of the common subarray ending at index `i` in `A` and index `j` in `B`.
  2. Initialize `dp` with zeros.
  3. Iterate through `A` and `B`, updating `dp[i][j]` based on whether `A[i]` equals `B[j]`. If they are equal, `dp[i][j] = dp[i-1][j-1] + 1`.
  4. Keep track of the maximum value in `dp`, which represents the length of the longest common subarray.
- Proof of optimality: This approach ensures that each pair of elements from `A` and `B` is compared exactly once, leading to a significant reduction in time complexity compared to the brute force approach.

```cpp
int findLength(vector<int>& A, vector<int>& B) {
    int n = A.size(), m = B.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    int maxLen = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (A[i - 1] == B[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
                maxLen = max(maxLen, dp[i][j]);
            }
        }
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the sizes of `A` and `B`, respectively. This is because we perform a constant amount of work for each cell in the `dp` array.
> - **Space Complexity:** $O(n \cdot m)$, as we need to store the `dp` array.
> - **Optimality proof:** This approach is optimal because it achieves a linear time complexity with respect to the input sizes, which is the best possible for this problem given the need to compare elements between the two arrays.

---

### Final Notes

**Learning Points:**
- The importance of dynamic programming in solving problems that have overlapping subproblems.
- How to apply dynamic programming to find the longest common subarray between two arrays.
- The trade-off between time and space complexity in algorithm design.

**Mistakes to Avoid:**
- Not considering the dynamic programming approach, which can lead to inefficient solutions.
- Failing to initialize the `dp` array correctly, which can cause incorrect results.
- Not keeping track of the maximum length found during the iteration, which is necessary for finding the longest common subarray.