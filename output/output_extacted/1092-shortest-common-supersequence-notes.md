## Shortest Common Supersequence

**Problem Link:** https://leetcode.com/problems/shortest-common-supersequence/description

**Problem Statement:**
- Input: Two strings `str1` and `str2`.
- Output: The shortest common supersequence of `str1` and `str2`.
- Key requirements: The supersequence should contain all characters of both `str1` and `str2` in the order they appear in the strings.
- Edge cases: Empty strings, strings of different lengths, strings with common and uncommon characters.

**Example Test Cases:**
- `str1 = "abc", str2 = "def"`: The shortest common supersequence is `"abcdef"`.
- `str1 = "abc", str2 = "abc"`: The shortest common supersequence is `"abc"`.
- `str1 = "", str2 = "abc"`: The shortest common supersequence is `"abc"`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible supersequences of the two input strings and checking which one is the shortest.
- This approach involves using recursion to generate all possible combinations of characters from both strings.
- It is not efficient due to the exponential number of possible supersequences.

```cpp
class Solution {
public:
    string shortestCommonSupersequence(string str1, string str2) {
        int m = str1.size();
        int n = str2.size();
        
        vector<string> supersequences;
        
        // Generate all possible supersequences using recursion
        generateSupersequences(str1, str2, "", 0, 0, supersequences);
        
        // Find the shortest supersequence
        string shortest = supersequences[0];
        for (int i = 1; i < supersequences.size(); i++) {
            if (supersequences[i].size() < shortest.size()) {
                shortest = supersequences[i];
            }
        }
        
        return shortest;
    }
    
    void generateSupersequences(string str1, string str2, string current, int i, int j, vector<string>& supersequences) {
        if (i == str1.size() && j == str2.size()) {
            supersequences.push_back(current);
            return;
        }
        
        if (i < str1.size()) {
            generateSupersequences(str1, str2, current + str1[i], i + 1, j, supersequences);
        }
        
        if (j < str2.size()) {
            generateSupersequences(str1, str2, current + str2[j], i, j + 1, supersequences);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{m+n})$, where $m$ and $n$ are the lengths of the input strings. This is because we generate all possible supersequences using recursion.
> - **Space Complexity:** $O(2^{m+n})$, as we store all generated supersequences.
> - **Why these complexities occur:** The exponential time and space complexities are due to the brute force approach of generating all possible supersequences.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using dynamic programming to find the longest common subsequence (LCS) of the two input strings.
- The shortest common supersequence can be constructed by inserting the non-common characters from both strings into the LCS.
- This approach has a time complexity of $O(mn)$, where $m$ and $n$ are the lengths of the input strings.

```cpp
class Solution {
public:
    string shortestCommonSupersequence(string str1, string str2) {
        int m = str1.size();
        int n = str2.size();
        
        // Create a 2D array to store the lengths of common subsequences
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
        // Fill the 2D array using dynamic programming
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (str1[i - 1] == str2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        // Construct the shortest common supersequence
        int i = m;
        int j = n;
        string supersequence = "";
        while (i > 0 && j > 0) {
            if (str1[i - 1] == str2[j - 1]) {
                supersequence = str1[i - 1] + supersequence;
                i--;
                j--;
            } else if (dp[i - 1][j] > dp[i][j - 1]) {
                supersequence = str1[i - 1] + supersequence;
                i--;
            } else {
                supersequence = str2[j - 1] + supersequence;
                j--;
            }
        }
        
        // Append any remaining characters from the input strings
        while (i > 0) {
            supersequence = str1[i - 1] + supersequence;
            i--;
        }
        while (j > 0) {
            supersequence = str2[j - 1] + supersequence;
            j--;
        }
        
        return supersequence;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(mn)$, where $m$ and $n$ are the lengths of the input strings. This is because we fill a 2D array using dynamic programming.
> - **Space Complexity:** $O(mn)$, as we store the lengths of common subsequences in a 2D array.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to find the longest common subsequence, which is the key to constructing the shortest common supersequence.

---

### Final Notes

**Learning Points:**
- The importance of dynamic programming in solving problems involving sequences and subsequences.
- The concept of longest common subsequences and how they can be used to construct shortest common supersequences.
- The trade-off between time and space complexity in different approaches.

**Mistakes to Avoid:**
- Not considering the base cases in recursive functions.
- Not using dynamic programming to optimize the solution.
- Not handling edge cases, such as empty input strings.
- Not testing the solution with different input scenarios.