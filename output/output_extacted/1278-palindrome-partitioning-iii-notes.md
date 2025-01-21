## Palindrome Partitioning III

**Problem Link:** https://leetcode.com/problems/palindrome-partitioning-iii/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Constraints: `1 <= k <= s.length <= 1000`.
- Expected Output: The minimum number of moves to make `s` a palindrome by changing at most one character in each of the `k` substrings.
- Key Requirements:
  - The input string `s` must be partitioned into `k` non-empty substrings.
  - For each substring, at most one character can be changed to make the substring a palindrome.
- Edge Cases:
  - If `k` is 1, the problem reduces to finding the minimum number of moves to make the entire string a palindrome.
  - If `k` equals the length of `s`, each character can be considered as a separate substring, and no changes are needed.

**Example Test Cases:**
- For `s = "abc", k = 2`, one possible partition is `"ab"`, `"c"`, and the minimum number of moves is 1 (change `"ab"` to `"aa"`).
- For `s = "abccba", k = 2`, a possible partition is `"abcc"`, `"ba"`, and the minimum number of moves is 1 (change `"abcc"` to `"abbb"`).

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible partitions of the string into `k` substrings.
- For each partition, calculate the minimum number of moves required to make each substring a palindrome.
- The brute force approach involves generating all possible partitions and calculating the moves for each, which is highly inefficient for large strings and values of `k`.

```cpp
#include <vector>
#include <string>

int palindromePartitioningIII(const std::string& s, int k) {
    int n = s.length();
    // Generate all possible partitions of s into k substrings
    std::vector<std::vector<std::string>> partitions;
    // ... (omitted for brevity, as this step is complex and inefficient)
    
    int minMoves = INT_MAX;
    for (const auto& partition : partitions) {
        int moves = 0;
        for (const auto& substring : partition) {
            // Calculate the minimum moves to make the substring a palindrome
            int left = 0, right = substring.length() - 1;
            while (left < right) {
                if (substring[left] != substring[right]) {
                    moves++;
                }
                left++;
                right--;
            }
        }
        minMoves = std::min(minMoves, moves);
    }
    
    return minMoves;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot k \cdot n)$, where $n$ is the length of the string. The reason is that we generate all possible partitions (exponential in $n$), and for each partition, we calculate the moves for each substring (linear in $n$ and $k$).
> - **Space Complexity:** $O(2^n \cdot k)$, for storing all possible partitions.
> - **Why these complexities occur:** The exponential time complexity comes from generating all possible partitions, which is inherently inefficient for large inputs.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to efficiently calculate the minimum moves for each possible substring of `s`.
- We maintain a 2D array `dp` where `dp[i][j]` represents the minimum moves to make the substring `s[i..j]` a palindrome.
- We fill `dp` in a bottom-up manner, starting with substrings of length 1 and increasing up to the full string length.
- For each substring, we consider two cases: whether the first and last characters are the same or not. If they are the same, we simply look at the moves needed for the substring without these characters. If they are different, we consider changing one of them to match the other and calculate the moves for the remaining substring.

```cpp
int palindromePartitioningIII(const std::string& s, int k) {
    int n = s.length();
    std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
    
    // Initialize dp for substrings of length 1
    for (int i = 0; i < n; i++) {
        dp[i][i] = 0;
    }
    
    // Fill dp for substrings of length 2 to n
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i <= n - length; i++) {
            int j = i + length - 1;
            if (s[i] == s[j]) {
                dp[i][j] = (length == 2) ? 0 : dp[i + 1][j - 1];
            } else {
                dp[i][j] = (length == 2) ? 1 : dp[i + 1][j - 1] + 1;
            }
        }
    }
    
    // Now, dp[i][j] contains the minimum moves to make s[i..j] a palindrome
    // We need to partition s into k substrings and minimize the total moves
    std::vector<int> dpK(n + 1, INT_MAX);
    dpK[0] = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            if (dpK[j] != INT_MAX) {
                dpK[i] = std::min(dpK[i], dpK[j] + dp[j][i - 1]);
            }
        }
    }
    
    return dpK[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string. The reason is that we fill the `dp` array in a bottom-up manner, which takes $O(n^2)$ time, and then we use this array to find the minimum moves for partitioning into `k` substrings, which takes $O(n)$ time. However, the outer loop for filling `dp` and the inner loop for partitioning give us $O(n^3)$.
> - **Space Complexity:** $O(n^2)$, for storing the `dp` array.
> - **Optimality proof:** This approach is optimal because it efficiently calculates the minimum moves for each substring and then uses these values to find the minimum total moves for partitioning into `k` substrings, avoiding the need to generate all possible partitions.

---

### Final Notes

**Learning Points:**
- The importance of dynamic programming in solving problems that involve overlapping subproblems.
- How to efficiently calculate the minimum moves to make a substring a palindrome.
- The approach to partition a string into `k` substrings with minimum total moves.

**Mistakes to Avoid:**
- Generating all possible partitions of the string, which leads to exponential time complexity.
- Not using dynamic programming to store and reuse the results of subproblems.
- Incorrectly calculating the minimum moves for each substring, which affects the overall result.