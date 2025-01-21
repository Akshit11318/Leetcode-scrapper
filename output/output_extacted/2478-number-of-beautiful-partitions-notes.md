## Number of Beautiful Partitions
**Problem Link:** https://leetcode.com/problems/number-of-beautiful-partitions/description

**Problem Statement:**
- Input: A string `s` consisting of digits and an integer `k`.
- Constraints: `1 <= k <= s.length <= 1000`.
- Expected output: The number of ways to partition `s` into `k` beautiful partitions.
- Key requirements: A beautiful partition is a substring that starts with a digit and does not contain any leading zeros.
- Edge cases: Handle cases where `s` starts with a zero or contains only zeros.

**Example Test Cases:**
- `s = "23541", k = 3`, output: `3` (partitions: ["2", "3", "541"], ["2", "35", "41"], ["23", "5", "41"])
- `s = "10", k = 2`, output: `1` (partition: ["1", "0"])

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves trying all possible partitions of the string `s` and checking if each partition is beautiful.
- We can use recursion to generate all possible partitions.
- We then check each partition to see if it's beautiful by ensuring it doesn't start with a zero (unless it's a single zero) and doesn't contain any leading zeros.

```cpp
int numberOfBeautifulPartitions(string s, int k) {
    int n = s.size();
    int count = 0;
    vector<string> currentPartition;
    
    function<void(int)> dfs = [&](int start) {
        if (currentPartition.size() == k) {
            bool isValid = true;
            for (const string& partition : currentPartition) {
                if (partition[0] == '0' && partition.size() > 1) {
                    isValid = false;
                    break;
                }
            }
            if (isValid) {
                count++;
            }
            return;
        }
        
        for (int i = start; i < n; i++) {
            string partition = s.substr(start, i - start + 1);
            currentPartition.push_back(partition);
            dfs(i + 1);
            currentPartition.pop_back();
        }
    };
    
    dfs(0);
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot k)$, where $n$ is the length of the string `s`. This is because we're generating all possible partitions of the string, which has $2^n$ possibilities, and for each partition, we're checking if it's beautiful, which takes $O(k)$ time.
> - **Space Complexity:** $O(n \cdot k)$, where $n$ is the length of the string `s`. This is because we're storing the current partition, which can have up to $n$ characters, and we're storing up to $k$ partitions.
> - **Why these complexities occur:** These complexities occur because we're using a brute force approach, which involves trying all possible partitions of the string. This results in exponential time complexity and linear space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to use dynamic programming to store the number of beautiful partitions for each prefix of the string `s`.
- We can use a 2D array `dp` where `dp[i][j]` represents the number of beautiful partitions of the prefix `s[0..i]` into `j` partitions.
- We can fill up the `dp` array by iterating over the string `s` and for each character, we check if it's a valid partition by ensuring it doesn't start with a zero (unless it's a single zero) and doesn't contain any leading zeros.
- If it's a valid partition, we update the `dp` array accordingly.

```cpp
int numberOfBeautifulPartitions(string s, int k) {
    int n = s.size();
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
    dp[0][0] = 1;
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= k; j++) {
            for (int x = 1; x <= i; x++) {
                string partition = s.substr(i - x, x);
                if (partition[0] != '0' || partition.size() == 1) {
                    dp[i][j] += dp[i - x][j - 1];
                }
            }
        }
    }
    
    return dp[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the length of the string `s`. This is because we're filling up the `dp` array, which has $n \cdot k$ entries, and for each entry, we're iterating over the string `s`, which takes $O(n)$ time.
> - **Space Complexity:** $O(n \cdot k)$, where $n$ is the length of the string `s`. This is because we're storing the `dp` array, which has $n \cdot k$ entries.
> - **Optimality proof:** This is the optimal solution because we're using dynamic programming to store the number of beautiful partitions for each prefix of the string `s`, which avoids redundant computation and reduces the time complexity from exponential to polynomial.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, recursion, and string manipulation.
- Problem-solving patterns identified: using dynamic programming to store intermediate results and avoiding redundant computation.
- Optimization techniques learned: using dynamic programming to reduce time complexity and using recursion to generate all possible partitions.
- Similar problems to practice: problems involving dynamic programming, recursion, and string manipulation.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, such as when the string `s` starts with a zero or contains only zeros.
- Edge cases to watch for: cases where the string `s` is empty or contains only zeros.
- Performance pitfalls: using a brute force approach, which can result in exponential time complexity.
- Testing considerations: testing the solution with different inputs, including edge cases, to ensure correctness and efficiency.