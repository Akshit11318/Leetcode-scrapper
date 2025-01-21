## Get the Maximum Score
**Problem Link:** https://leetcode.com/problems/get-the-maximum-score/description

**Problem Statement:**
- Input format: You are given two arrays `nums1` and `nums2` of the same length.
- Constraints: The length of `nums1` and `nums2` will be between 1 and 10,000.
- Expected output format: The maximum score that can be achieved.
- Key requirements and edge cases to consider: The score is calculated as the sum of the product of the corresponding elements from `nums1` and `nums2` when the elements are in the same order.
- Example test cases with explanations: For example, if `nums1 = [1,2,3]` and `nums2 = [4,5,6]`, the maximum score is `1*6 + 2*5 + 3*4 = 32` when `nums1` is reversed.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all permutations of `nums1` and calculate the score for each permutation.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of `nums1`.
  2. For each permutation, calculate the score by multiplying the corresponding elements from the permutation and `nums2`, and summing the results.
  3. Keep track of the maximum score found.
- Why this approach comes to mind first: It is a straightforward way to consider all possible orderings of `nums1`.

```cpp
#include <algorithm>
#include <vector>

int maxScore(std::vector<int>& nums1, std::vector<int>& nums2) {
    int n = nums1.size();
    int maxScore = 0;
    std::vector<int> perm = nums1;
    do {
        int score = 0;
        for (int i = 0; i < n; i++) {
            score += perm[i] * nums2[i];
        }
        maxScore = std::max(maxScore, score);
    } while (std::next_permutation(perm.begin(), perm.end()));
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the length of `nums1`. This is because there are $n!$ permutations of `nums1`, and we calculate the score for each permutation.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `nums1`. This is because we need to store the current permutation of `nums1`.
> - **Why these complexities occur:** The brute force approach has high time complexity because it considers all possible permutations of `nums1`, which grows factorially with the length of `nums1`.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to solve this problem more efficiently. However, in this case, we can actually use a greedy approach to solve it in $O(n^2)$ time complexity by using a 2D array to store the maximum score for each subproblem.
- Detailed breakdown of the approach:
  1. Initialize a 2D array `dp` of size $(n+1) \times (n+1)$ to store the maximum score for each subproblem.
  2. Fill the `dp` array in a bottom-up manner by considering all possible pairs of elements from `nums1` and `nums2`.
  3. The maximum score is stored in the top-right corner of the `dp` array.
- Proof of optimality: This approach is optimal because it considers all possible pairs of elements from `nums1` and `nums2` exactly once, and it uses a 2D array to store the maximum score for each subproblem, which reduces the time complexity to $O(n^2)$.

```cpp
int maxScore(std::vector<int>& nums1, std::vector<int>& nums2) {
    int n = nums1.size();
    std::vector<std::vector<int>> dp(n+1, std::vector<int>(n+1, 0));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            dp[i][j] = std::max(dp[i-1][j-1] + nums1[i-1]*nums2[j-1], std::max(dp[i-1][j], dp[i][j-1]));
        }
    }
    return dp[n][n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `nums1`. This is because we fill the `dp` array in a bottom-up manner, and each cell in the `dp` array is filled in constant time.
> - **Space Complexity:** $O(n^2)$, where $n$ is the length of `nums1`. This is because we need to store the `dp` array.
> - **Optimality proof:** This approach is optimal because it considers all possible pairs of elements from `nums1` and `nums2` exactly once, and it uses a 2D array to store the maximum score for each subproblem, which reduces the time complexity to $O(n^2)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, greedy approach.
- Problem-solving patterns identified: Using a 2D array to store the maximum score for each subproblem.
- Optimization techniques learned: Reducing the time complexity from $O(n!)$ to $O(n^2)$ by using a greedy approach.
- Similar problems to practice: Other problems that involve finding the maximum score or minimum cost by considering all possible pairs of elements from two arrays.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` array correctly, not filling the `dp` array in a bottom-up manner.
- Edge cases to watch for: When `nums1` or `nums2` is empty, when `nums1` and `nums2` have different lengths.
- Performance pitfalls: Using a brute force approach that has high time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases.