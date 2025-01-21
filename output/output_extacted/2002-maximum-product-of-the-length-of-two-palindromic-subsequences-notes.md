## Maximum Product of the Length of Two Palindromic Subsequences

**Problem Link:** https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/description

**Problem Statement:**
- Input: A string `s`.
- Expected Output: The maximum product of the lengths of two non-overlapping palindromic subsequences.
- Key Requirements:
  - A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.
  - A palindromic subsequence is a subsequence that reads the same backward as forward.
  - Two subsequences are non-overlapping if there is no index at which both subsequences have a character.
- Edge Cases:
  - If `s` is empty, return 0.
  - If `s` has only one character, return 0 because there cannot be two non-overlapping palindromic subsequences.
- Example Test Cases:
  - For `s = "abc"`, the maximum product is 1 because the only palindromic subsequences are single characters.
  - For `s = "abcd"`, the maximum product is 1 for the same reason.
  - For `s = "aa"`, the maximum product is 1 * 1 = 1, since we can choose two non-overlapping palindromic subsequences of length 1.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible subsequences of the input string `s`.
- Then, for each subsequence, check if it is palindromic.
- After identifying all palindromic subsequences, find all pairs of non-overlapping subsequences.
- Finally, calculate the product of the lengths of each pair and find the maximum.

```cpp
int maxProduct(string s) {
    int n = s.size();
    int maxProduct = 0;
    // Generate all possible subsequences
    for (int mask = 0; mask < (1 << n); mask++) {
        string sub1;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i))) {
                sub1 += s[i];
            }
        }
        // Check if sub1 is palindromic
        if (isPalindrome(sub1)) {
            for (int mask2 = 0; mask2 < (1 << n); mask2++) {
                string sub2;
                bool overlap = false;
                for (int i = 0; i < n; i++) {
                    if ((mask2 & (1 << i))) {
                        if ((mask & (1 << i))) {
                            overlap = true;
                            break;
                        }
                        sub2 += s[i];
                    }
                }
                if (!overlap && isPalindrome(sub2)) {
                    maxProduct = max(maxProduct, (int)sub1.size() * (int)sub2.size());
                }
            }
        }
    }
    return maxProduct;
}

bool isPalindrome(string s) {
    int left = 0, right = s.size() - 1;
    while (left < right) {
        if (s[left] != s[right]) return false;
        left++, right--;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n^2)$, where $n$ is the length of the string `s`. This is because for each of the $2^n$ possible subsequences, we check if it's palindromic, which takes $O(n)$ time, and we do this for each of the $2^n$ possible subsequences again to find non-overlapping pairs.
> - **Space Complexity:** $O(n)$ for storing the subsequences.
> - **Why these complexities occur:** The brute force approach generates all possible subsequences and checks each one, leading to exponential time complexity. The space complexity is linear because we only need to store one subsequence at a time.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using dynamic programming to store the lengths of the longest palindromic subsequences ending at each position and the maximum product of lengths of two non-overlapping palindromic subsequences seen so far.
- This approach avoids the exponential time complexity of the brute force method by only considering each subsequence once.

```cpp
int maxProduct(string s) {
    int n = s.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++) {
        dp[i][i] = 1; // Single character is always a palindrome
    }
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i <= n - length; i++) {
            int j = i + length - 1;
            if (s[i] == s[j] && length == 2) {
                dp[i][j] = 2;
            } else if (s[i] == s[j]) {
                dp[i][j] = dp[i + 1][j - 1] + 2;
            } else {
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
    }
    int maxProduct = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            maxProduct = max(maxProduct, dp[0][i] * dp[i + 1][j]);
        }
    }
    return maxProduct;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string `s`. This is because we fill the `dp` table in $O(n^2)$ time and then find the maximum product in $O(n^2)$ time.
> - **Space Complexity:** $O(n^2)$ for the `dp` table.
> - **Optimality proof:** This approach is optimal because it avoids the exponential time complexity of the brute force method by using dynamic programming to store and reuse the results of subproblems.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, palindromic subsequences.
- Problem-solving patterns identified: Avoiding brute force by using dynamic programming to solve subproblems only once.
- Optimization techniques learned: Using a `dp` table to store the lengths of the longest palindromic subsequences.
- Similar problems to practice: Longest Palindromic Subsequence, Partition Equal Subset Sum.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly initializing the `dp` table, not considering the base case for single characters.
- Edge cases to watch for: Empty string, string with only one character.
- Performance pitfalls: Using brute force instead of dynamic programming.
- Testing considerations: Test with strings of varying lengths, including empty string and single character string.