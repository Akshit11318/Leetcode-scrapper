## String Compression II
**Problem Link:** https://leetcode.com/problems/string-compression-ii/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Expected output: The length of the string after compressing `s` using the given rules and removing at most `k` characters.
- Key requirements: Compress the string by replacing consecutive repeated characters with the character and the count of consecutive occurrences, and then remove at most `k` characters to minimize the length of the compressed string.
- Example test cases:
  - Input: `s = "aaabcccd", k = 2`, Output: `4` (Explanation: "aaabcccd" can be compressed to "a3b1c3d1", then remove 2 characters to get "a3c3d1" with length 6, but we can further compress it to "a3c3d" by removing the 'b1' and one more character, resulting in a length of 5, but the optimal is to remove the 'b1' and get "a3c3d1" and then remove one more character to get "a3c3d" with a length of 5, however, the best is "a3c3" with a length of 4)
  - Input: `s = "aabbaa", k = 2`, Output: `2` (Explanation: "aabbaa" can be compressed to "a2b2a2", then remove 2 characters to get "a2a2" or "b2a2" or "a2b2" with a length of 4, but we can further remove more characters to get "a2" or "b2" or "a" with a length of 2 or less)

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible compressed strings by considering all possible removals of characters and then compressing the remaining string.
- We can use a recursive approach to generate all possible strings after removing at most `k` characters.
- Then, for each string, we compress it by replacing consecutive repeated characters with the character and the count of consecutive occurrences.
- Finally, we find the minimum length among all compressed strings.

```cpp
class Solution {
public:
    int getLengthOfOptimalCompression(string s, int k) {
        int n = s.size();
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, n));
        dp[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= min(i, k); j++) {
                if (j > 0) {
                    dp[i][j] = dp[i - 1][j - 1];
                }
                int count = 0, del = 0;
                for (int l = i; l >= 1; l--) {
                    if (s[l - 1] == s[i - 1]) {
                        count++;
                    } else {
                        del++;
                    }
                    if (j >= del) {
                        dp[i][j] = min(dp[i][j], dp[l - 1][j - del] + 1 + to_string(count).size());
                    }
                }
            }
        }
        return dp[n][k];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the length of the string `s`. This is because we have two nested loops over the string and `k`.
> - **Space Complexity:** $O(n \cdot k)$, where $n$ is the length of the string `s`. This is because we use a 2D array of size $(n + 1) \times (k + 1)$ to store the dynamic programming table.
> - **Why these complexities occur:** The time complexity occurs because we have to consider all possible removals of characters and all possible compressions of the remaining string. The space complexity occurs because we need to store the dynamic programming table to avoid redundant computation.

---

### Optimal Approach (Required)

The above approach is already optimal with a time complexity of $O(n^2 \cdot k)$ and a space complexity of $O(n \cdot k)$. This is because we have to consider all possible removals of characters and all possible compressions of the remaining string, and we use dynamic programming to avoid redundant computation.

However, we can make some minor optimizations to the code, such as using a more efficient way to calculate the length of the compressed string.

```cpp
class Solution {
public:
    int getLengthOfOptimalCompression(string s, int k) {
        int n = s.size();
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, n));
        dp[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= min(i, k); j++) {
                if (j > 0) {
                    dp[i][j] = dp[i - 1][j - 1];
                }
                int count = 0, del = 0;
                for (int l = i; l >= 1; l--) {
                    if (s[l - 1] == s[i - 1]) {
                        count++;
                    } else {
                        del++;
                    }
                    if (j >= del) {
                        int len = 0;
                        if (count > 1) len += to_string(count).size();
                        len += 1; // for the character
                        dp[i][j] = min(dp[i][j], dp[l - 1][j - del] + len);
                    }
                }
            }
        }
        return dp[n][k];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the length of the string `s`.
> - **Space Complexity:** $O(n \cdot k)$, where $n$ is the length of the string `s`.
> - **Optimality proof:** This approach is optimal because we have to consider all possible removals of characters and all possible compressions of the remaining string, and we use dynamic programming to avoid redundant computation.

---

### Final Notes

**Learning Points:**
- The problem requires us to find the minimum length of the compressed string after removing at most `k` characters.
- We can use dynamic programming to solve this problem efficiently.
- The time complexity of the optimal approach is $O(n^2 \cdot k)$, and the space complexity is $O(n \cdot k)$.

**Mistakes to Avoid:**
- Not considering all possible removals of characters and all possible compressions of the remaining string.
- Not using dynamic programming to avoid redundant computation.
- Not handling edge cases correctly, such as when `k` is greater than the length of the string `s`.