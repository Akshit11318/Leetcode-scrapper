## Shortest Way to Form String

**Problem Link:** https://leetcode.com/problems/shortest-way-to-form-string/description

**Problem Statement:**
- Input format: Two strings `source` and `target`.
- Constraints: `1 <= source.length, target.length <= 10^5`.
- Expected output format: The minimum number of sub-sequences of `source` to form `target`.
- Key requirements and edge cases to consider: 
  - The function should return `-1` if it is impossible to form `target` from `source`.
  - The function should return the minimum number of sub-sequences if `target` can be formed from `source`.
- Example test cases with explanations:
  - If `source = "abc"` and `target = "abcbc"`, the function should return `2` because `"abcbc"` can be formed from `"abc"` in two sub-sequences: `"ab"` and `"cbc"`.
  - If `source = "abc"` and `target = "cd"` or `target = "xyz"`, the function should return `-1` because `"cd"` and `"xyz"` cannot be formed from `"abc"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can start by checking all possible sub-sequences of `source` to form `target`.
- Step-by-step breakdown of the solution:
  1. Generate all possible sub-sequences of `source`.
  2. For each sub-sequence, check if it can be used to form `target`.
  3. If a sub-sequence can be used to form `target`, update the minimum number of sub-sequences.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient because it generates all possible sub-sequences of `source`.

```cpp
int shortestWay(string source, string target) {
    int m = source.size(), n = target.size();
    vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
    dp[0][0] = true;
    
    for (int i = 1; i <= m; i++) {
        dp[i][0] = true;
        for (int j = 1; j <= n; j++) {
            if (source[i - 1] == target[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] || dp[i - 1][j];
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }
    
    if (!dp[m][n]) return -1;
    
    int count = 0;
    int i = m, j = n;
    while (i > 0 && j > 0) {
        if (source[i - 1] == target[j - 1]) {
            i--;
            j--;
        } else {
            i--;
        }
        if (j == 0) {
            count++;
            j = n;
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$ where $m$ and $n$ are the lengths of `source` and `target`, respectively. This is because we are using a nested loop to fill up the `dp` table.
> - **Space Complexity:** $O(m \cdot n)$ because we are using a 2D table of size $(m + 1) \times (n + 1)$ to store the dynamic programming state.
> - **Why these complexities occur:** The time and space complexities occur because we are using a dynamic programming approach to solve the problem, which requires us to store the state of the problem in a table and fill it up using a nested loop.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a two-pointer technique to solve this problem efficiently. We can iterate over `target` and for each character, we can find the next occurrence of that character in `source`.
- Detailed breakdown of the approach:
  1. Initialize two pointers, one for `source` and one for `target`.
  2. Iterate over `target` and for each character, find the next occurrence of that character in `source`.
  3. If the character is found in `source`, move the pointer for `source` to the next position.
  4. If the character is not found in `source`, return `-1` because it is impossible to form `target` from `source`.
- Proof of optimality: This approach is optimal because it only requires a single pass over `target` and `source`, resulting in a time complexity of $O(n \cdot m)$ where $n$ and $m$ are the lengths of `target` and `source`, respectively.

```cpp
int shortestWay(string source, string target) {
    int count = 0;
    int i = 0;
    while (i < target.size()) {
        int j = 0;
        bool found = false;
        for (; j < source.size(); j++) {
            if (source[j] == target[i]) {
                found = true;
                i++;
                if (i == target.size()) break;
            }
        }
        if (!found) return -1;
        count++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ and $m$ are the lengths of `target` and `source`, respectively. This is because we are using a nested loop to iterate over `target` and `source`.
> - **Space Complexity:** $O(1)$ because we are only using a constant amount of space to store the pointers and the count.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over `target` and `source`, resulting in a time complexity of $O(n \cdot m)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, dynamic programming.
- Problem-solving patterns identified: Using a two-pointer technique to solve problems that require finding the next occurrence of a character in a string.
- Optimization techniques learned: Using a single pass over the input strings to reduce the time complexity.
- Similar problems to practice: Problems that require finding the next occurrence of a character in a string, such as the "Find the Next Occurrence of a Character" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the case where the character is not found in `source`.
- Edge cases to watch for: The case where `target` is empty, the case where `source` is empty.
- Performance pitfalls: Using a brute force approach that generates all possible sub-sequences of `source`.
- Testing considerations: Testing the function with different inputs, such as an empty `target`, an empty `source`, and a `target` that cannot be formed from `source`.