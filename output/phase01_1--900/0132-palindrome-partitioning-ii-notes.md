## Palindrome Partitioning II
**Problem Link:** https://leetcode.com/problems/palindrome-partitioning-ii/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` of length `n`, and we need to find the minimum number of cuts required to partition the string into palindromic substrings.
- Expected output format: The output should be an integer representing the minimum number of cuts.
- Key requirements and edge cases to consider: We need to handle empty strings, strings with a single character, and strings with multiple characters.
- Example test cases with explanations:
  - Input: `s = "aab"`
    Output: `1`
    Explanation: The optimal partitioning is `"aa"` and `"b"`, which requires one cut.
  - Input: `s = "abacddcaba"`
    Output: `0`
    Explanation: The entire string is a palindrome, so no cuts are required.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can try all possible partitions of the string and check if each partition is a palindrome.
- Step-by-step breakdown of the solution:
  1. Generate all possible partitions of the string.
  2. For each partition, check if each substring is a palindrome.
  3. If all substrings are palindromes, update the minimum number of cuts.
- Why this approach comes to mind first: It's a straightforward approach that involves checking all possible partitions.

```cpp
class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        vector<int> dp(n);
        for (int i = 0; i < n; i++) {
            dp[i] = i;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                string substr = s.substr(j, i - j + 1);
                if (isPalindrome(substr)) {
                    if (j == 0) {
                        dp[i] = 0;
                    } else if (dp[j - 1] + 1 < dp[i]) {
                        dp[i] = dp[j - 1] + 1;
                    }
                }
            }
        }
        return dp[n - 1];
    }

    bool isPalindrome(string s) {
        int left = 0;
        int right = s.size() - 1;
        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string. This is because we're generating all possible partitions of the string, and for each partition, we're checking if each substring is a palindrome using a nested loop.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because we're storing the minimum number of cuts for each prefix of the string.
> - **Why these complexities occur:** The time complexity is high because we're using a brute force approach that involves checking all possible partitions of the string. The space complexity is relatively low because we're only storing the minimum number of cuts for each prefix of the string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to store the minimum number of cuts for each prefix of the string.
- Detailed breakdown of the approach:
  1. Create a table `dp` where `dp[i]` represents the minimum number of cuts for the prefix `s[0..i]`.
  2. Initialize `dp[i] = i` for all `i`, because the worst-case scenario is that we need to make `i` cuts.
  3. Iterate over the string, and for each position `i`, check if the substring `s[j..i]` is a palindrome for all `j <= i`.
  4. If `s[j..i]` is a palindrome, update `dp[i]` with the minimum of its current value and `dp[j - 1] + 1`.
- Proof of optimality: This approach is optimal because it considers all possible partitions of the string and chooses the one with the minimum number of cuts.
- Why further optimization is impossible: This approach has a time complexity of $O(n^2)$, which is the best we can do because we need to check all possible substrings of the string.

```cpp
class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        vector<int> dp(n);
        for (int i = 0; i < n; i++) {
            dp[i] = i;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                string substr = s.substr(j, i - j + 1);
                if (isPalindrome(substr)) {
                    if (j == 0) {
                        dp[i] = 0;
                    } else if (dp[j - 1] + 1 < dp[i]) {
                        dp[i] = dp[j - 1] + 1;
                    }
                }
            }
        }
        return dp[n - 1];
    }

    bool isPalindrome(string s) {
        int left = 0;
        int right = s.size() - 1;
        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string. This is because we're iterating over the string and checking all possible substrings.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because we're storing the minimum number of cuts for each prefix of the string.
> - **Optimality proof:** This approach is optimal because it considers all possible partitions of the string and chooses the one with the minimum number of cuts.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, palindrome checking.
- Problem-solving patterns identified: Using dynamic programming to store the minimum number of cuts for each prefix of the string.
- Optimization techniques learned: Reducing the time complexity by using dynamic programming.
- Similar problems to practice: Other dynamic programming problems, such as the `Longest Palindromic Substring` problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the `dp` table correctly, not updating the `dp` table correctly.
- Edge cases to watch for: Empty strings, strings with a single character.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases.