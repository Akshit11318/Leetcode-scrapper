## Find the Original Typed String II

**Problem Link:** https://leetcode.com/problems/find-the-original-typed-string-ii/description

**Problem Statement:**
- Input: Two strings `s` and `t` where `s` is the original typed string and `t` is the typed string after removing some characters.
- Constraints: `1 <= s.length <= 100`, `1 <= t.length <= 100`, `s` and `t` consist only of lowercase English letters.
- Expected Output: The original typed string `s` if it matches the typed string `t`, otherwise return an empty string.
- Key Requirements and Edge Cases: 
  - If `s` matches `t`, return `s`.
  - If `s` does not match `t`, return an empty string.
  - The matching process involves comparing characters of `s` and `t` from left to right and considering the possibility of removing characters from `s` to match `t`.
- Example Test Cases:
  - `s = "abcb", t = "abc"` returns an empty string because `s` does not match `t` after removing any characters.
  - `s = "xgyzzdr", t = "xyz"` returns an empty string because `s` does not match `t` after removing any characters.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible substring of `s` to see if it matches `t` by removing characters from `s`.
- This approach involves generating all possible substrings of `s` and comparing them with `t`.
- The brute force approach comes to mind first because it directly addresses the problem statement without requiring deep insight into string matching algorithms.

```cpp
#include <iostream>
#include <string>

std::string findOriginalString(std::string s, std::string t) {
    for (int mask = 0; mask < (1 << s.length()); ++mask) {
        std::string candidate;
        for (int i = 0; i < s.length(); ++i) {
            if (!(mask & (1 << i))) {
                candidate += s[i];
            }
        }
        if (candidate == t) {
            return s;
        }
    }
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of `s`, because we generate all possible subsets of `s` (which is $2^n$) and for each subset, we construct a string of length up to $n$.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `s`, because we need to store the current subset of characters being considered.
> - **Why these complexities occur:** The brute force approach involves exponential time complexity due to generating all possible subsets of `s`, and linear space complexity for storing the current subset.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a two-pointer technique to compare `s` and `t` directly without generating all possible subsets of `s`.
- We maintain two pointers, one for `s` and one for `t`, and move them based on whether the current characters match or not.
- If the characters match, we move both pointers. If they do not match, we move the pointer for `s` but keep the pointer for `t` at the same position, effectively "removing" the character from `s`.
- This approach is optimal because it directly addresses the problem statement in a linear pass through `s` and `t`.

```cpp
#include <iostream>
#include <string>

std::string findOriginalString(std::string s, std::string t) {
    int i = 0, j = 0;
    while (i < s.length() && j < t.length()) {
        if (s[i] == t[j]) {
            ++i;
            ++j;
        } else {
            ++i;
        }
    }
    if (j == t.length()) {
        return s;
    }
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `s`, because we make a single pass through `s` and `t`.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the pointers and do not allocate any additional space that scales with input size.
> - **Optimality proof:** This is the optimal solution because we cannot do better than a linear pass through the input strings to determine if `s` can be transformed into `t` by removing characters.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include the use of brute force and two-pointer techniques.
- Problem-solving patterns identified include recognizing when a problem can be simplified from an exponential solution to a linear one through clever observation.
- Optimization techniques learned include avoiding unnecessary computation by directly addressing the problem statement.
- Similar problems to practice include other string matching and modification problems.

**Mistakes to Avoid:**
- Common implementation errors include incorrect handling of edge cases, such as when `s` or `t` is empty.
- Performance pitfalls include using exponential time complexity solutions for problems that can be solved in linear time.
- Testing considerations include thoroughly testing the function with various inputs, including edge cases and large inputs, to ensure correctness and efficiency.