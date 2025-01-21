## Number of Ways to Rearrange Sticks with K Sticks Visible
**Problem Link:** https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/description

**Problem Statement:**
- Input: An array of stick lengths and an integer `k`.
- Constraints: The array length is greater than `k`, and all elements are positive integers.
- Expected Output: The number of ways to rearrange sticks so that exactly `k` sticks are visible from the left.
- Key Requirements: A stick is considered visible if it is not blocked by a longer stick to its left.

### Brute Force Approach
**Explanation:**
- The initial thought process involves generating all permutations of the stick array and checking each permutation to see if exactly `k` sticks are visible.
- Step-by-step breakdown:
  1. Generate all permutations of the stick array.
  2. For each permutation, iterate from left to right and count the number of visible sticks.
  3. If the count of visible sticks equals `k`, increment the total count of valid arrangements.
- This approach comes to mind first because it directly addresses the problem statement by considering all possible arrangements.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int countVisibleSticks(vector<int>& sticks, int k) {
    int count = 0;
    // Generate all permutations
    do {
        int visible = 0;
        int maxStick = 0;
        for (int i = 0; i < sticks.size(); i++) {
            if (sticks[i] > maxStick) {
                maxStick = sticks[i];
                visible++;
            }
        }
        if (visible == k) {
            count++;
        }
    } while (next_permutation(sticks.begin(), sticks.end()));
    return count;
}

int main() {
    vector<int> sticks = {1, 2, 3, 4, 5};
    int k = 3;
    cout << "Number of ways to rearrange sticks: " << countVisibleSticks(sticks, k) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the number of sticks. This is because there are $n!$ permutations of the stick array, and we generate all of them.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output. The algorithm uses a constant amount of space to store variables like `count` and `maxStick`.
> - **Why these complexities occur:** The time complexity is high because generating all permutations is a computationally expensive operation. The space complexity is low because we only use a constant amount of extra space to store variables.

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can use a dynamic programming approach to store the number of ways to rearrange sticks for each possible number of visible sticks up to `k`.
- Detailed breakdown:
  1. Initialize a 2D array `dp` where `dp[i][j]` represents the number of ways to rearrange the first `i` sticks so that exactly `j` sticks are visible.
  2. Fill the `dp` array using the following recurrence relation: `dp[i][j] = dp[i-1][j] + dp[i-1][j-1]`, where the first term corresponds to the case where the current stick is not visible and the second term corresponds to the case where the current stick is visible.
  3. The final answer is stored in `dp[n][k]`, where `n` is the number of sticks.
- Proof of optimality: This approach is optimal because it uses a bottom-up dynamic programming approach to store and reuse the results of subproblems, avoiding the need to generate all permutations.

```cpp
#include <iostream>
#include <vector>

using namespace std;

int rearrangeSticks(int n, int k) {
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
    dp[0][0] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= min(i, k); j++) {
            if (j > 0) {
                dp[i][j] += dp[i - 1][j - 1];
            }
            dp[i][j] += dp[i - 1][j];
        }
    }
    return dp[n][k];
}

int main() {
    int n = 5;
    int k = 3;
    cout << "Number of ways to rearrange sticks: " << rearrangeSticks(n, k) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(nk)$, where $n$ is the number of sticks and $k$ is the number of visible sticks. This is because we fill a 2D array of size $n \times k$.
> - **Space Complexity:** $O(nk)$, because we use a 2D array of size $n \times k$ to store the `dp` values.
> - **Optimality proof:** This approach is optimal because it uses a bottom-up dynamic programming approach to store and reuse the results of subproblems, avoiding the need to generate all permutations.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming and combinatorics.
- Problem-solving patterns identified: using a bottom-up approach to store and reuse the results of subproblems.
- Optimization techniques learned: avoiding the generation of all permutations by using a dynamic programming approach.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the `dp` array correctly or not using the correct recurrence relation.
- Edge cases to watch for: when `k` is greater than `n` or when `n` is 0.
- Performance pitfalls: using a top-down approach with memoization instead of a bottom-up approach.
- Testing considerations: testing the function with different values of `n` and `k` to ensure it works correctly.