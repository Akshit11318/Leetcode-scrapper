## Hash Divided String

**Problem Link:** https://leetcode.com/problems/hash-divided-string/description

**Problem Statement:**
- Input: Two strings `s` and `t`.
- Constraints: `1 <= s.length <= 10^5`, `1 <= t.length <= 10^5`.
- Expected Output: `true` if `s` can be divided into non-overlapping substrings, each of which is a prefix of `t`, `false` otherwise.
- Key Requirements: Substrings must not overlap and must be prefixes of `t`.
- Edge Cases: Empty strings, single-character strings, and cases where `s` is longer than `t`.

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible division of `s` into substrings and verify if each is a prefix of `t`.
- Step-by-step breakdown:
  1. Generate all possible divisions of `s` into substrings.
  2. For each division, check if each substring is a prefix of `t`.
  3. If a division where all substrings are prefixes of `t` is found, return `true`.
  4. If no such division is found after checking all possibilities, return `false`.

```cpp
#include <string>
using namespace std;

bool isPrefixOfAll(const string& s, const string& t) {
    int n = s.length();
    int m = t.length();
    
    for (int mask = 1; mask < (1 << n); ++mask) {
        bool isValid = true;
        int start = 0;
        while (start < n) {
            bool found = false;
            for (int end = start + 1; end <= n; ++end) {
                if ((mask & (1 << (end - 1))) && t.find(s.substr(start, end - start)) == 0) {
                    found = true;
                    start = end;
                    break;
                }
            }
            if (!found) {
                isValid = false;
                break;
            }
        }
        if (isValid && start == n) {
            return true;
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m)$, where $n$ is the length of `s` and $m` is the length of `t`, due to generating all possible divisions and checking each substring against `t`.
> - **Space Complexity:** $O(1)$, not counting the space needed for input strings, as we only use a constant amount of space to store the bitmask and indices.
> - **Why these complexities occur:** The brute force approach checks every possible division of `s`, leading to exponential time complexity due to the number of divisions being $2^n$. For each division, we potentially check against `t`, leading to the additional $n \cdot m$ factor.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking all possible divisions, use a dynamic programming approach to build up a solution by checking prefixes of `s` against `t`.
- Detailed breakdown:
  1. Initialize a dynamic programming table `dp` where `dp[i]` is `true` if the substring from the start of `s` to index `i` can be divided into prefixes of `t`.
  2. For each index `i` in `s`, check all prefixes of `s` ending at `i` to see if any are prefixes of `t`.
  3. If a prefix of `s` ending at `i` is a prefix of `t`, and the substring before this prefix can also be divided into prefixes of `t`, then `dp[i]` is `true`.

```cpp
#include <string>
#include <vector>
using namespace std;

bool isPrefixOfAll(const string& s, const string& t) {
    int n = s.length();
    vector<bool> dp(n + 1, false);
    dp[0] = true;
    
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (dp[j] && t.find(s.substr(j, i - j)) == 0) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the length of `s` and $m$ is the length of `t`, due to the nested loops checking all prefixes of `s` against `t`.
> - **Space Complexity:** $O(n)$, for the dynamic programming table.
> - **Optimality proof:** This approach is optimal because it checks the minimum necessary number of prefixes to determine if `s` can be divided into prefixes of `t`, avoiding the exponential complexity of the brute force approach.

### Final Notes

**Learning Points:**
- Dynamic programming can significantly reduce the time complexity of problems involving overlapping subproblems.
- Prefix matching can be efficiently performed using the `find` method of strings in C++.
- Always consider the trade-offs between time and space complexity when choosing an approach.

**Mistakes to Avoid:**
- Not considering the exponential growth of possible divisions in the brute force approach.
- Not initializing the dynamic programming table correctly.
- Not checking all prefixes of `s` against `t` in the optimal approach.