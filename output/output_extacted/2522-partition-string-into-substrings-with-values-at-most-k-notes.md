## Partition String into Substrings with Values at Most K
**Problem Link:** https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/description

**Problem Statement:**
- Input: a string `s` and an integer `k`.
- Constraints: `1 <= s.length <= 10^5`, `1 <= k <= 10^5`.
- Expected Output: the number of ways to partition the string `s` into substrings such that the value of each substring is at most `k`.
- Key Requirements: 
  - The value of a substring is the sum of the ASCII values of its characters.
  - A substring is a contiguous sequence of characters in the string `s`.
- Edge Cases:
  - Empty string `s`.
  - `k` is 0 or negative.
  - `k` is larger than the sum of ASCII values of all characters in `s`.
- Example Test Cases:
  - Input: `s = "abc", k = 25`, Output: `1`
  - Input: `s = "abc", k = 26`, Output: `2`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible partitions of the string `s` and count the number of valid partitions.
- Step-by-step breakdown:
  1. Generate all possible partitions of the string `s`.
  2. For each partition, calculate the sum of ASCII values of each substring.
  3. If the sum of ASCII values of a substring is at most `k`, consider it a valid substring.
  4. Count the number of valid partitions.
- Why this approach comes to mind first: it is a straightforward and intuitive way to solve the problem.

```cpp
int partitionString(string s, int k) {
    int n = s.length();
    int count = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> substrings;
        int start = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                substrings.push_back(i - start);
                start = i + 1;
            }
        }
        substrings.push_back(n - start);
        bool valid = true;
        for (int len : substrings) {
            int sum = 0;
            for (int j = 0; j < len; j++) {
                sum += s[start + j];
            }
            if (sum > k) {
                valid = false;
                break;
            }
            start += len;
        }
        if (valid) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string `s`. This is because we generate all possible partitions of the string `s`, and for each partition, we calculate the sum of ASCII values of each substring.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we store the lengths of the substrings in a vector.
> - **Why these complexities occur:** The time complexity is high because we generate all possible partitions of the string `s`, which is exponential in the length of the string. The space complexity is linear because we store the lengths of the substrings in a vector.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to count the number of valid partitions.
- Detailed breakdown:
  1. Initialize a dynamic programming table `dp` of size `n + 1`, where `dp[i]` represents the number of valid partitions of the substring `s[0..i]`.
  2. For each position `i` in the string `s`, calculate the sum of ASCII values of the substring `s[j..i]` for all `j < i`.
  3. If the sum of ASCII values is at most `k`, update `dp[i]` with the number of valid partitions of the substring `s[0..j]`.
  4. Return `dp[n]`, which represents the number of valid partitions of the entire string `s`.
- Why further optimization is impossible: this approach has a time complexity of $O(n^2)$, which is optimal because we need to calculate the sum of ASCII values of all substrings of the string `s`.

```cpp
int partitionString(string s, int k) {
    int n = s.length();
    vector<int> dp(n + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            int sum = 0;
            for (int x = j; x < i; x++) {
                sum += s[x];
            }
            if (sum <= k) {
                dp[i] += dp[j];
            }
        }
    }
    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string `s`. This is because we calculate the sum of ASCII values of all substrings of the string `s`.
> - **Space Complexity:** $O(n)$, where $n` is the length of the string `s`. This is because we store the dynamic programming table `dp` of size `n + 1`.
> - **Optimality proof:** This approach is optimal because we need to calculate the sum of ASCII values of all substrings of the string `s`, which requires a time complexity of at least $O(n^2)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, string manipulation.
- Problem-solving patterns identified: counting, partitioning.
- Optimization techniques learned: memoization, dynamic programming.
- Similar problems to practice: partitioning, counting, string manipulation.

**Mistakes to Avoid:**
- Common implementation errors: incorrect initialization of dynamic programming table, incorrect calculation of sum of ASCII values.
- Edge cases to watch for: empty string, `k` is 0 or negative, `k` is larger than the sum of ASCII values of all characters in `s`.
- Performance pitfalls: high time complexity, incorrect use of dynamic programming.
- Testing considerations: test with different inputs, including edge cases, to ensure correctness and efficiency.