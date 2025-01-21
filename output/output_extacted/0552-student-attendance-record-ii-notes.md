## Student Attendance Record II
**Problem Link:** https://leetcode.com/problems/student-attendance-record-ii/description

**Problem Statement:**
- Input format and constraints: The input `n` is an integer representing the number of days in the attendance record.
- Expected output format: The output should be an integer representing the number of ways to keep a record of `n` days without having more than one `A` and no consecutive `L`s.
- Key requirements and edge cases to consider: The attendance record can contain `P` (present), `A` (absent), and `L` (late). We need to consider cases where `n` is small (e.g., 1, 2) and cases where `n` is large.
- Example test cases with explanations:
  - For `n = 1`, there are 3 ways: `P`, `A`, `L`.
  - For `n = 2`, there are 8 ways: `PP`, `PA`, `PL`, `AP`, `AA` is not allowed, `AL`, `LP`, `LL` is not allowed.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible attendance records of length `n` and count the valid ones.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for valid records.
  2. Generate all possible records of length `n` using a recursive function or a loop.
  3. For each record, check if it is valid (no more than one `A` and no consecutive `L`s).
  4. If the record is valid, increment the counter.
- Why this approach comes to mind first: It is a straightforward way to solve the problem, but it is inefficient for large `n` due to the exponential number of possible records.

```cpp
int checkRecord(int n) {
    int count = 0;
    for (int i = 0; i < (1 << (2 * n)); i++) {
        string record = "";
        for (int j = 0; j < n; j++) {
            int k = (i >> (2 * j)) & 3;
            if (k == 0) record += 'P';
            else if (k == 1) record += 'A';
            else if (k == 2) record += 'L';
        }
        if (isValid(record)) count++;
    }
    return count;
}

bool isValid(string record) {
    int aCount = 0;
    for (int i = 0; i < record.size(); i++) {
        if (record[i] == 'A') aCount++;
        if (record[i] == 'L' && i > 0 && record[i - 1] == 'L') return false;
    }
    return aCount <= 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(3^n)$, where $n$ is the number of days. This is because there are $3^n$ possible records (each day can be `P`, `A`, or `L`).
> - **Space Complexity:** $O(n)$, where $n$ is the number of days. This is because we need to store the current record being checked.
> - **Why these complexities occur:** The brute force approach generates all possible records, which leads to an exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the number of valid records of length `i` ending with `P`, `A`, and `L`, respectively.
- Detailed breakdown of the approach:
  1. Initialize arrays `dp` to store the number of valid records of length `i` ending with `P`, `A`, and `L`, respectively.
  2. For each day `i` from 1 to `n`, update the `dp` arrays based on the previous day's values.
  3. The final answer is the sum of the values in the `dp` arrays for the last day.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is the best possible complexity for this problem.
- Why further optimization is impossible: We need to consider all possible records, and the dynamic programming approach does this in the most efficient way possible.

```cpp
int checkRecord(int n) {
    long long dp[2][3] = {{1, 1, 1}, {0, 0, 0}};
    for (int i = 1; i < n; i++) {
        long long newDp[2][3] = {{0, 0, 0}, {0, 0, 0}};
        newDp[0][0] = (dp[0][0] + dp[0][1] + dp[0][2]) % 1000000007;
        newDp[0][1] = dp[0][0];
        newDp[0][2] = dp[0][1];
        newDp[1][0] = (dp[1][0] + dp[1][1] + dp[1][2]) % 1000000007;
        newDp[1][1] = dp[1][0];
        newDp[1][2] = dp[1][1];
        memcpy(dp, newDp, sizeof(newDp));
    }
    return (int)((dp[0][0] + dp[0][1] + dp[0][2] + dp[1][0]) % 1000000007);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of days.
> - **Space Complexity:** $O(1)$, since the space usage does not grow with the size of the input.
> - **Optimality proof:** This approach has a time complexity of $O(n)$, which is the best possible complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization.
- Problem-solving patterns identified: Using arrays to store intermediate results, updating these arrays iteratively.
- Optimization techniques learned: Avoiding redundant calculations by storing intermediate results.
- Similar problems to practice: Other dynamic programming problems, such as the Fibonacci sequence or the knapsack problem.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize arrays, using incorrect indices.
- Edge cases to watch for: Handling the base case (e.g., when `n` is 1), avoiding overflow.
- Performance pitfalls: Using inefficient algorithms, such as the brute force approach.
- Testing considerations: Testing the function with different inputs, including edge cases.