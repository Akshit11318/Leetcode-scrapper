## Longest Unequal Adjacent Groups Subsequence II
**Problem Link:** https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/description

**Problem Statement:**
- Input: A string `s` consisting of lowercase English letters.
- Output: The length of the longest subsequence where no two adjacent groups are equal.
- Key requirements: 
  - A group is a sequence of one or more of the same character.
  - The goal is to find the longest subsequence that satisfies the condition.
- Edge cases: 
  - An empty string returns 0.
  - A string with a single character returns 1.

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all possible subsequences of the input string and check each one to see if it meets the condition of not having two adjacent groups of the same character.
- Step-by-step breakdown:
  1. Generate all possible subsequences.
  2. For each subsequence, identify groups of the same character.
  3. Check if any two adjacent groups are the same.
  4. If not, calculate the length of this subsequence.
- Why this approach comes to mind first: It's a straightforward, exhaustive approach to ensure we don't miss any possible subsequences.

```cpp
class Solution {
public:
    int longestSubsequence(string s) {
        int n = s.size();
        int maxLen = 0;
        
        // Generate all possible subsequences
        for (int mask = 0; mask < (1 << n); mask++) {
            string subsequence = "";
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    subsequence += s[i];
                }
            }
            
            // Check if the subsequence meets the condition
            bool valid = true;
            char prevGroup = '\0';
            char currChar = '\0';
            for (char c : subsequence) {
                if (c != currChar) {
                    if (c == prevGroup) {
                        valid = false;
                        break;
                    }
                    prevGroup = currChar;
                    currChar = c;
                }
            }
            
            if (valid) {
                maxLen = max(maxLen, (int)subsequence.size());
            }
        }
        
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string. This is because we generate $2^n$ subsequences and for each, we potentially iterate over its length.
> - **Space Complexity:** $O(n)$, for storing the subsequence and other variables.
> - **Why these complexities occur:** The exponential time complexity comes from generating all possible subsequences, and the linear space complexity is due to the need to store each subsequence and variables for checking the condition.

### Optimal Approach (Required)
**Explanation:**
- The optimal approach involves using dynamic programming to keep track of the longest subsequence ending at each position and whether the last character is part of a group or not.
- Key insight: Instead of generating all subsequences, we can build up the solution by considering each character one by one and deciding whether to include it in the current group or start a new group.
- Detailed breakdown:
  1. Initialize a DP table to store the length of the longest subsequence up to each position.
  2. Iterate through the string, for each character:
     - Decide whether to include it in the current group or start a new group based on the previous character.
     - Update the DP table accordingly.
- Why further optimization is impossible: This approach considers each character's contribution to the solution exactly once, making it optimal.

```cpp
class Solution {
public:
    int longestSubsequence(string s) {
        int n = s.size();
        vector<vector<int>> dp(n + 1, vector<int>(26, 0));
        
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < 26; j++) {
                dp[i][j] = dp[i - 1][j];
            }
            int idx = s[i - 1] - 'a';
            for (int j = 0; j < 26; j++) {
                if (j != idx) {
                    dp[i][idx] = max(dp[i][idx], dp[i - 1][j] + 1);
                }
            }
        }
        
        int maxLen = 0;
        for (int j = 0; j < 26; j++) {
            maxLen = max(maxLen, dp[n][j]);
        }
        
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 26)$, where $n$ is the length of the string. This is because we iterate over the string once and for each character, we perform a constant amount of work.
> - **Space Complexity:** $O(n \cdot 26)$, for the DP table.
> - **Optimality proof:** This approach is optimal because it considers each character's contribution to the solution exactly once, avoiding redundant work.

---

### Final Notes

**Learning Points:**
- The importance of dynamic programming in solving problems involving subsequences or subarrays.
- How to approach problems that require finding the longest subsequence with certain properties.
- The trade-off between brute force and optimal approaches in terms of time and space complexity.

**Mistakes to Avoid:**
- Not considering the exponential growth of subsequences in brute force approaches.
- Not identifying the key insight that leads to an optimal dynamic programming solution.
- Failing to initialize DP tables correctly or update them based on the problem's constraints.