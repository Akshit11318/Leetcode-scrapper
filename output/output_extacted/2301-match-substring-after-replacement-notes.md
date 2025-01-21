## Match Substring After Replacement
**Problem Link:** https://leetcode.com/problems/match-substring-after-replacement/description

**Problem Statement:**
- Input: `s` and `sub`
- Constraints: `1 <= s.length <= 10^5`, `1 <= sub.length <= 10^5`
- Expected output: Return `true` if it is possible to make `sub` a substring of `s` by replacing zero or more characters in `s` with any character, and `false` otherwise.
- Key requirements: Determine if `sub` can be made a substring of `s` after replacing characters in `s`.
- Example test cases:
  - `s = "abcde", sub = "a"`: Return `true` because `sub` is already a substring of `s`.
  - `s = "abcde", sub = "aef"`: Return `false` because `sub` cannot be made a substring of `s` by replacing characters in `s`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible replacements of characters in `s` to see if `sub` can be made a substring.
- Step-by-step breakdown:
  1. Generate all possible strings that can be formed by replacing characters in `s`.
  2. For each generated string, check if `sub` is a substring.
- Why this approach comes to mind first: It is straightforward to consider all possible replacements, but this approach is inefficient due to its high time complexity.

```cpp
#include <string>
using namespace std;

bool matchSubstringAfterReplacement(string s, string sub) {
    int n = s.length();
    int m = sub.length();
    
    // Try all possible replacements
    for (int i = 0; i < (1 << n); i++) {
        string temp = s;
        // Replace characters in temp according to the current bit mask
        for (int j = 0; j < n; j++) {
            if ((i & (1 << j)) != 0) {
                temp[j] = '*'; // Mark for replacement
            }
        }
        
        // Check if sub is a substring of temp after replacement
        bool found = false;
        for (int j = 0; j <= n - m; j++) {
            bool match = true;
            for (int k = 0; k < m; k++) {
                if (temp[j + k] != '*' && temp[j + k] != sub[k]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                found = true;
                break;
            }
        }
        
        if (found) return true;
    }
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m \cdot (n - m + 1))$ because we generate $2^n$ possible strings and check each for the substring in $O(m \cdot (n - m + 1))$ time.
> - **Space Complexity:** $O(n)$ for the temporary string.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of replacements, leading to an exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of trying all possible replacements, we can use a sliding window approach to check if `sub` can be made a substring of `s` by replacing characters in `s`.
- Detailed breakdown:
  1. Initialize a window of size `m` in `s`.
  2. For each position of the window in `s`, count the number of characters that need to be replaced to match `sub`.
  3. If the number of replacements needed is less than or equal to the number of characters that can be replaced in the window, return `true`.
- Proof of optimality: This approach has a linear time complexity, which is optimal because we must at least read the input strings once.

```cpp
#include <string>
using namespace std;

bool matchSubstringAfterReplacement(string s, string sub) {
    int n = s.length();
    int m = sub.length();
    
    for (int i = 0; i <= n - m; i++) {
        int replacements = 0;
        for (int j = 0; j < m; j++) {
            if (s[i + j] != sub[j]) {
                replacements++;
            }
        }
        if (replacements <= m) return true;
    }
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ because we slide the window over `s` and for each position, we compare characters with `sub`.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the window boundaries and the number of replacements.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity with respect to the input size, and we must at least read the input once to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Sliding window technique, string matching.
- Problem-solving patterns: Instead of generating all possibilities, look for a way to reduce the problem size or use a more efficient algorithm.
- Optimization techniques: Use a sliding window to reduce the number of comparisons needed.
- Similar problems to practice: String matching problems, substring problems.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors in the window boundaries, incorrect counting of replacements.
- Edge cases to watch for: Empty strings, strings of different lengths.
- Performance pitfalls: Using a brute force approach for large inputs.
- Testing considerations: Test with different lengths of `s` and `sub`, test with different characters in `s` and `sub`.