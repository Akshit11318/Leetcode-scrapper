## Uncrossed Lines
**Problem Link:** https://leetcode.com/problems/uncrossed-lines/description

**Problem Statement:**
- Input format and constraints: Given two arrays of integers `A` and `B`, both of length `n` and `m` respectively, find the maximum number of lines that can be drawn such that no two lines cross.
- Expected output format: The maximum number of lines that can be drawn.
- Key requirements and edge cases to consider: `A` and `B` can have duplicate elements, and the lines should be drawn between elements of `A` and `B`.
- Example test cases with explanations:
  - `A = [1,4,2], B = [1,2,4]`: The maximum number of lines that can be drawn is `2`.
  - `A = [2,5,1,2,5], B = [10,5,2,1,5,2]`: The maximum number of lines that can be drawn is `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can try all possible combinations of drawing lines between elements of `A` and `B`.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of drawing lines between elements of `A` and `B`.
  2. For each combination, check if any two lines cross.
  3. If no lines cross, update the maximum number of lines that can be drawn.
- Why this approach comes to mind first: It is a straightforward approach to try all possible combinations and check if they satisfy the condition.

```cpp
#include <vector>
#include <algorithm>

int maxUncrossedLines(vector<int>& A, vector<int>& B) {
    int maxLines = 0;
    for (int mask = 0; mask < (1 << A.size()); mask++) {
        for (int mask2 = 0; mask2 < (1 << B.size()); mask2++) {
            int lines = 0;
            bool valid = true;
            vector<pair<int, int>> linesDrawn;
            for (int i = 0; i < A.size(); i++) {
                if ((mask & (1 << i)) != 0) {
                    for (int j = 0; j < B.size(); j++) {
                        if ((mask2 & (1 << j)) != 0 && A[i] == B[j]) {
                            linesDrawn.push_back({i, j});
                            lines++;
                        }
                    }
                }
            }
            for (int i = 0; i < linesDrawn.size(); i++) {
                for (int j = i + 1; j < linesDrawn.size(); j++) {
                    if (linesDrawn[i].first < linesDrawn[j].first && linesDrawn[i].second > linesDrawn[j].second) {
                        valid = false;
                        break;
                    }
                }
            }
            if (valid) {
                maxLines = max(maxLines, lines);
            }
        }
    }
    return maxLines;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot 2^m \cdot n \cdot m)$, where $n$ and $m$ are the sizes of `A` and `B` respectively.
> - **Space Complexity:** $O(n \cdot m)$, for storing the lines drawn.
> - **Why these complexities occur:** The brute force approach generates all possible combinations of drawing lines between elements of `A` and `B`, which results in a time complexity of $O(2^n \cdot 2^m)$. For each combination, it checks if any two lines cross, which results in a time complexity of $O(n \cdot m)$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to solve this problem. The idea is to maintain a 2D array `dp` where `dp[i][j]` represents the maximum number of lines that can be drawn between the first `i` elements of `A` and the first `j` elements of `B`.
- Detailed breakdown of the approach:
  1. Initialize a 2D array `dp` with size `(n + 1) x (m + 1)`, where `n` and `m` are the sizes of `A` and `B` respectively.
  2. For each element `A[i]` in `A`, iterate over all elements `B[j]` in `B`. If `A[i] == B[j]`, update `dp[i + 1][j + 1]` to be the maximum of `dp[i + 1][j + 1]` and `dp[i][j] + 1`.
  3. For each element `A[i]` in `A`, update `dp[i + 1][j]` to be the maximum of `dp[i + 1][j]` and `dp[i][j]`.
  4. For each element `B[j]` in `B`, update `dp[i][j + 1]` to be the maximum of `dp[i][j + 1]` and `dp[i][j]`.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible combinations of drawing lines between elements of `A` and `B`, and it does so in an efficient manner.

```cpp
int maxUncrossedLines(vector<int>& A, vector<int>& B) {
    int n = A.size(), m = B.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (A[i - 1] == B[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[n][m];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the sizes of `A` and `B` respectively.
> - **Space Complexity:** $O(n \cdot m)$, for storing the dynamic programming table.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible combinations of drawing lines between elements of `A` and `B`, and it does so in an efficient manner. The time complexity of $O(n \cdot m)$ is optimal because we need to consider each element of `A` and `B` at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, and how to apply it to solve a problem.
- Problem-solving patterns identified: The problem can be solved by maintaining a 2D array `dp` where `dp[i][j]` represents the maximum number of lines that can be drawn between the first `i` elements of `A` and the first `j` elements of `B`.
- Optimization techniques learned: The dynamic programming approach ensures that we consider all possible combinations of drawing lines between elements of `A` and `B`, and it does so in an efficient manner.
- Similar problems to practice: Other problems that can be solved using dynamic programming, such as the Longest Common Subsequence problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming table correctly, or not updating the table correctly.
- Edge cases to watch for: The case where `A` or `B` is empty, or the case where `A` and `B` have different sizes.
- Performance pitfalls: Using a brute force approach, which can result in a time complexity of $O(2^n \cdot 2^m \cdot n \cdot m)$.
- Testing considerations: Testing the solution with different inputs, including edge cases, to ensure that it works correctly.