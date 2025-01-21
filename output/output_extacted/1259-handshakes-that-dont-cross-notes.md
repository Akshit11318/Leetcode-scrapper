## Handshakes That Don't Cross
**Problem Link:** https://leetcode.com/problems/handshakes-that-dont-cross/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `n` as input, representing the number of people. The constraint is that `n` is an even number and `0 <= n <= 30`.
- Expected output format: The expected output is the number of ways `n` people can shake hands without crossing hands.
- Key requirements and edge cases to consider: The key requirement is that no two people can cross hands while shaking. An edge case is when `n` is `0`, in which case there is only one way (no one shakes hands).
- Example test cases with explanations: For `n = 2`, there is only one way (the two people shake hands directly). For `n = 4`, there are two ways (either the first and second people shake hands and the third and fourth people shake hands, or the first and third people shake hands and the second and fourth people shake hands).

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The initial thought process is to generate all possible pairs of people shaking hands and then check if any pair crosses another pair.
- Step-by-step breakdown of the solution:
  1. Generate all possible pairs of people.
  2. For each pair, check if it crosses any other pair.
  3. If a pair does not cross any other pair, count it as a valid handshake.
- Why this approach comes to mind first: This approach comes to mind first because it directly addresses the problem statement and seems straightforward.

```cpp
int countWays(int n) {
    if (n == 0) return 1; // Base case: no one shakes hands
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            // Check if the pair (i, j) crosses any other pair
            bool isValid = true;
            for (int k = 0; k < n; k++) {
                for (int l = k + 1; l < n; l++) {
                    if (i < k && k < j && l < i && l > j) {
                        isValid = false;
                        break;
                    }
                }
                if (!isValid) break;
            }
            if (isValid) count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$, where $n$ is the number of people. This is because we have four nested loops.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the count and loop variables.
> - **Why these complexities occur:** The time complexity is high because we are generating all possible pairs of people and checking each pair against all other pairs. The space complexity is low because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use dynamic programming to store the number of ways to arrange `i` pairs of people.
- Detailed breakdown of the approach:
  1. Create a dynamic programming table `dp` of size `n/2 + 1`, where `dp[i]` represents the number of ways to arrange `i` pairs of people.
  2. Initialize `dp[0] = 1`, because there is one way to arrange no pairs of people (i.e., no one shakes hands).
  3. For each `i` from `1` to `n/2`, calculate `dp[i]` by considering all possible ways to add a new pair of people to the existing arrangement.
- Proof of optimality: This approach is optimal because it avoids the redundant calculations of the brute force approach and has a much lower time complexity.

```cpp
int countWays(int n) {
    vector<int> dp(n / 2 + 1);
    dp[0] = 1;
    for (int i = 1; i <= n / 2; i++) {
        for (int j = 0; j < i; j++) {
            dp[i] += dp[j] * dp[i - j - 1] * (2 * j + 1);
        }
    }
    return dp[n / 2];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of people. This is because we have two nested loops.
> - **Space Complexity:** $O(n)$, because we use a dynamic programming table of size `n/2 + 1`.
> - **Optimality proof:** This approach is optimal because it has a much lower time complexity than the brute force approach and avoids redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and memoization.
- Problem-solving patterns identified: Avoiding redundant calculations and using dynamic programming to store intermediate results.
- Optimization techniques learned: Using dynamic programming to reduce the time complexity of the algorithm.
- Similar problems to practice: Other dynamic programming problems, such as the Fibonacci sequence and the longest common subsequence problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming table correctly or not considering all possible cases.
- Edge cases to watch for: The case where `n` is `0` or the case where `n` is an odd number.
- Performance pitfalls: Using a brute force approach or not using dynamic programming to store intermediate results.
- Testing considerations: Testing the algorithm with different input sizes and edge cases to ensure correctness and efficiency.