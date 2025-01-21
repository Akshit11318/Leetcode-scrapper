## Find the Maximum Length of a Good Subsequence II
**Problem Link:** https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/description

**Problem Statement:**
- Input: `text` (a string) and `pattern` (a string)
- Constraints: 
  - `1 <= text.length <= 100`
  - `1 <= pattern.length <= 100`
- Expected Output: The maximum length of a good subsequence.
- Key Requirements:
  - A subsequence is considered good if it is not necessarily contiguous but follows the order of characters in the pattern.
  - The goal is to find the longest subsequence in the given text that matches the pattern.

### Brute Force Approach

**Explanation:**
- The brute force approach involves generating all possible subsequences of the text and checking each one to see if it matches the pattern.
- This approach comes to mind first because it is straightforward and does not require any advanced algorithms or data structures.
- However, it is inefficient because it generates all possible subsequences, which results in a high time complexity.

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int maxLength(string text, string pattern) {
    int maxLen = 0;
    int n = text.size();
    int m = pattern.size();
    
    // Generate all possible subsequences
    for (int mask = 0; mask < (1 << n); mask++) {
        string subsequence = "";
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subsequence += text[i];
            }
        }
        
        // Check if the subsequence matches the pattern
        int p = 0;
        for (char c : subsequence) {
            if (p < m && c == pattern[p]) {
                p++;
            }
        }
        
        // Update the maximum length if necessary
        if (p == m) {
            maxLen = max(maxLen, (int)subsequence.size());
        }
    }
    
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m)$, where $n$ is the length of the text and $m$ is the length of the pattern. The reason for this complexity is that we generate all possible subsequences of the text, which takes $O(2^n)$ time, and then check each one against the pattern, which takes $O(n \cdot m)$ time.
> - **Space Complexity:** $O(n)$, because we need to store the subsequence, which can be up to $n$ characters long.
> - **Why these complexities occur:** The high time complexity occurs because we generate all possible subsequences of the text, which is an exponential operation. The space complexity occurs because we need to store the subsequence.

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using dynamic programming to build up a solution.
- We create a 2D array, `dp`, where `dp[i][j]` represents the length of the longest good subsequence ending at index `i` in the text and matching the first `j` characters of the pattern.
- We fill in the `dp` array by iterating over the text and the pattern, and updating `dp[i][j]` based on whether the current character in the text matches the current character in the pattern.

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int maxLength(string text, string pattern) {
    int n = text.size();
    int m = pattern.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (text[i - 1] == pattern[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }
    
    return dp[n][m];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of the text and $m$ is the length of the pattern. The reason for this complexity is that we fill in the `dp` array by iterating over the text and the pattern.
> - **Space Complexity:** $O(n \cdot m)$, because we need to store the `dp` array, which has size $n \cdot m$.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to build up a solution, which avoids the exponential time complexity of the brute force approach.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, string matching.
- Problem-solving patterns identified: building up a solution using dynamic programming, avoiding exponential time complexity.
- Optimization techniques learned: using dynamic programming to avoid exponential time complexity.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the `dp` array correctly, not updating the `dp` array correctly.
- Edge cases to watch for: empty text or pattern, text or pattern with only one character.
- Performance pitfalls: using the brute force approach, which has exponential time complexity.
- Testing considerations: testing the function with different inputs, including edge cases.