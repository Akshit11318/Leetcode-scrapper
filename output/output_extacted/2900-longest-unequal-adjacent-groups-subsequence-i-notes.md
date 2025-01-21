## Longest Unequal Adjacent Groups Subsequence I
**Problem Link:** https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description

**Problem Statement:**
- Input format: A string `s` consisting of lowercase English letters.
- Constraints: $1 \leq s.length \leq 10^5$.
- Expected output format: The length of the longest subsequence with no two adjacent groups being equal.
- Key requirements and edge cases to consider: The subsequence should be formed by deleting characters from the input string, and a group is defined as a sequence of identical characters.
- Example test cases with explanations:
    - Input: `s = "abc"`
      Output: `3`
      Explanation: The subsequence `"abc"` has three groups: `"a"`, `"b"`, and `"c"`.
    - Input: `s = "aabaa"`
      Output: `3`
      Explanation: The subsequence `"aba"` has three groups: `"a"`, `"b"`, and `"a"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible subsequences and check if they meet the condition of having no two adjacent groups being equal.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of the input string.
  2. For each subsequence, identify the groups of identical characters.
  3. Check if any two adjacent groups are equal. If so, discard this subsequence.
  4. Keep track of the longest subsequence that meets the condition.
- Why this approach comes to mind first: It is a straightforward way to solve the problem by trying all possibilities.

```cpp
int longestSubsequence(string s) {
    int n = s.size();
    int maxLen = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        string subsequence = "";
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i))) {
                subsequence += s[i];
            }
        }
        bool valid = true;
        char prevGroup = '\0';
        char currGroup = '\0';
        for (char c : subsequence) {
            if (c != currGroup) {
                if (c == prevGroup) {
                    valid = false;
                    break;
                }
                prevGroup = currGroup;
                currGroup = c;
            }
        }
        if (valid) {
            maxLen = max(maxLen, (int)subsequence.size());
        }
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input string. This is because we generate all possible subsequences (which takes $O(2^n)$ time) and then process each subsequence (which takes $O(n)$ time).
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we store the subsequence, which can have up to $n$ characters.
> - **Why these complexities occur:** The brute force approach tries all possible subsequences, which leads to an exponential time complexity. The space complexity is linear because we only need to store the current subsequence.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to keep track of the longest subsequence ending at each position.
- Detailed breakdown of the approach:
  1. Initialize a dynamic programming table `dp` of size $n$, where $dp[i]$ represents the length of the longest subsequence ending at position $i$.
  2. For each position $i$, check if the current character is different from the previous group. If so, update $dp[i]$ to be the maximum of its current value and $dp[i-1] + 1$.
  3. If the current character is the same as the previous group, update $dp[i]$ to be the maximum of its current value and $dp[i-2] + 1$ (if $i-2$ is a valid position).
- Proof of optimality: This approach ensures that we consider all possible subsequences and choose the longest one that meets the condition.
- Why further optimization is impossible: This approach has a linear time complexity, which is optimal because we need to at least read the input string once.

```cpp
int longestSubsequence(string s) {
    int n = s.size();
    int maxLen = 0;
    int prev = 0, curr = 0;
    for (int i = 0; i < n; i++) {
        if (i == 0 || s[i] != s[i-1]) {
            prev = curr;
            curr = curr + 1;
        } else {
            prev = curr;
            curr = prev + 1;
        }
        maxLen = max(maxLen, curr);
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we only need to process each character once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the dynamic programming table.
> - **Optimality proof:** This approach ensures that we consider all possible subsequences and choose the longest one that meets the condition. The time complexity is linear, which is optimal because we need to at least read the input string once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and greedy algorithms.
- Problem-solving patterns identified: The problem can be solved using a dynamic programming approach, where we keep track of the longest subsequence ending at each position.
- Optimization techniques learned: We can optimize the solution by using a dynamic programming table to store the longest subsequence ending at each position.
- Similar problems to practice: Longest Increasing Subsequence, Longest Common Subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming table correctly, or not updating the table correctly.
- Edge cases to watch for: The input string may be empty, or it may contain only one character.
- Performance pitfalls: Using a brute force approach can lead to an exponential time complexity, which can be avoided by using a dynamic programming approach.
- Testing considerations: We should test the solution with different input strings, including edge cases such as an empty string or a string with only one character.