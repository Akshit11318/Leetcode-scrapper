## Find the Shortest Superstring
**Problem Link:** https://leetcode.com/problems/find-the-shortest-superstring/description

**Problem Statement:**
- Input: A list of strings `words`.
- Constraints: The number of strings is in the range `[1, 12]`.
- Expected Output: The shortest possible superstring that contains each string in `words` as a substring.
- Key Requirements: Find the shortest superstring with minimal overlap.
- Example Test Cases:
  - Input: `["alex","loves","leetcode"]`, Output: `"alexlovesleetcode"`
  - Input: `["catg","cta","atg","att"]`, Output: `"catgcta"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all permutations of the input strings and concatenate them with minimal overlap.
- Step-by-step breakdown:
  1. Generate all permutations of the input strings.
  2. For each permutation, concatenate the strings with minimal overlap.
  3. Keep track of the shortest superstring found.
- Why this approach comes to mind first: It is a straightforward way to explore all possible combinations of the input strings.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int overlap(const string& a, const string& b) {
    for (int i = min(a.size(), b.size()); i > 0; --i) {
        if (a.substr(a.size() - i) == b.substr(0, i)) {
            return i;
        }
    }
    return 0;
}

string shortestSuperstring(vector<string>& words) {
    int n = words.size();
    vector<int> perm(n);
    for (int i = 0; i < n; ++i) perm[i] = i;
    string shortest = "";
    do {
        string superstring = words[perm[0]];
        for (int i = 1; i < n; ++i) {
            int o = overlap(superstring, words[perm[i]]);
            superstring += words[perm[i]].substr(o);
        }
        if (shortest.empty() || superstring.size() < shortest.size()) {
            shortest = superstring;
        }
    } while (next_permutation(perm.begin(), perm.end()));
    return shortest;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string. The reason is that we generate all permutations of the input strings, and for each permutation, we concatenate the strings with minimal overlap.
> - **Space Complexity:** $O(n \cdot m)$, as we need to store the input strings and the permutation.
> - **Why these complexities occur:** The permutation generation and the overlap calculation are the main contributors to the time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a bitmask to represent the subset of strings included in the superstring, and use a dynamic programming approach to find the shortest superstring.
- Detailed breakdown:
  1. Initialize a bitmask `dp` to represent the subset of strings included in the superstring.
  2. Initialize a string `dp_str` to store the shortest superstring for each subset.
  3. Iterate over all possible subsets of strings.
  4. For each subset, iterate over all strings in the subset.
  5. For each string, calculate the overlap with the current superstring and update the superstring if necessary.
- Why further optimization is impossible: This approach has a time complexity of $O(n \cdot 2^n \cdot m^2)$, which is the best possible complexity for this problem.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int overlap(const string& a, const string& b) {
    for (int i = min(a.size(), b.size()); i > 0; --i) {
        if (a.substr(a.size() - i) == b.substr(0, i)) {
            return i;
        }
    }
    return 0;
}

string shortestSuperstring(vector<string>& words) {
    int n = words.size();
    vector<string> dp(1 << n);
    for (int mask = 0; mask < (1 << n); ++mask) {
        if (mask == 0) continue;
        int first = __builtin_ctz(mask);
        dp[mask] = words[first];
        for (int i = first + 1; i < n; ++i) {
            if ((mask >> i) & 1) {
                int o = overlap(dp[mask ^ (1 << i)], words[i]);
                dp[mask] = min(dp[mask], dp[mask ^ (1 << i)] + words[i].substr(o));
            }
        }
    }
    return dp[(1 << n) - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 2^n \cdot m^2)$, where $n$ is the number of strings and $m$ is the maximum length of a string.
> - **Space Complexity:** $O(2^n \cdot m)$, as we need to store the shortest superstring for each subset of strings.
> - **Optimality proof:** This approach is optimal because it explores all possible subsets of strings and finds the shortest superstring for each subset.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, bitmasking, and string manipulation.
- Problem-solving patterns identified: Using a bitmask to represent subsets and dynamic programming to find the shortest superstring.
- Optimization techniques learned: Using overlap calculation to reduce the length of the superstring.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the overlap between strings.
- Edge cases to watch for: Handling empty strings and strings with no overlap.
- Performance pitfalls: Using inefficient algorithms or data structures.
- Testing considerations: Thoroughly testing the implementation with different input cases.