## Apply Operations to Make Two Strings Equal

**Problem Link:** https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/description

**Problem Statement:**
- Input: Two strings `s` and `t`.
- Constraints: The length of `s` and `t` is at most $10^5$.
- Expected Output: Determine if it is possible to make `s` equal to `t` by applying the following operations:
  - Swap two characters in `s`.
  - Reverse the string `s`.
- Key Requirements: We need to find out if it is possible to transform `s` into `t` using the given operations.
- Edge Cases: Consider when `s` and `t` have different lengths or when they have the same characters but in a different order.
- Example Test Cases:
  - Input: `s = "bank", t = "kanb"`
    - Output: `true` (We can reverse `s` to get `t`).
  - Input: `s = "attack", t = "defend"`
    - Output: `false` (It is not possible to transform `s` into `t`).

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of swapping characters in `s` and checking if any of these combinations result in `t`.
- However, this approach is highly inefficient due to its exponential time complexity.
- A step-by-step breakdown would involve generating all permutations of `s` and checking each permutation against `t`.

```cpp
#include <iostream>
#include <algorithm>
#include <string>

bool areAlmostEqual(const std::string& s, const std::string& t) {
    // If s and t are equal, return true
    if (s == t) return true;

    // Generate all permutations of s
    std::string temp = s;
    do {
        // Check if the current permutation is equal to t
        if (temp == t) return true;
    } while (std::next_permutation(temp.begin(), temp.end()));

    // If no permutation matches t, return false
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$ where $n$ is the length of `s`. This is because there are $n!$ permutations of a string of length $n$.
> - **Space Complexity:** $O(n)$ for storing the permutations.
> - **Why these complexities occur:** The brute force approach involves generating all permutations of `s`, which leads to an exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that we only need to check if the characters in `s` and `t` are the same, regardless of their order.
- We can do this by sorting the characters in both strings and comparing the results.
- If the sorted strings are equal, then it is possible to transform `s` into `t` by swapping characters.

```cpp
#include <iostream>
#include <algorithm>
#include <string>

bool areAlmostEqual(const std::string& s, const std::string& t) {
    // If s and t are not the same length, return false
    if (s.length() != t.length()) return false;

    // If s and t are equal, return true
    if (s == t) return true;

    // Sort the characters in s and t
    std::string sSorted = s;
    std::string tSorted = t;
    std::sort(sSorted.begin(), sSorted.end());
    std::sort(tSorted.begin(), tSorted.end());

    // If the sorted strings are equal, return true
    if (sSorted == tSorted) {
        // Check if there are at most two different characters between s and t
        int diffCount = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] != t[i]) diffCount++;
            if (diffCount > 2) return false;
        }
        return diffCount == 2 || diffCount == 0;
    }

    // If the sorted strings are not equal, return false
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the length of `s`. This is because we are sorting the characters in both strings.
> - **Space Complexity:** $O(n)$ for storing the sorted strings.
> - **Optimality proof:** This approach is optimal because it checks if the characters in `s` and `t` are the same, regardless of their order, and also checks if there are at most two different characters between `s` and `t`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, string comparison.
- Problem-solving patterns identified: checking if two strings are anagrams of each other.
- Optimization techniques learned: using sorting to compare strings.
- Similar problems to practice: anagram detection, string permutation.

**Mistakes to Avoid:**
- Common implementation errors: not checking for equal string lengths, not handling edge cases.
- Edge cases to watch for: strings with different lengths, strings with the same characters but in a different order.
- Performance pitfalls: using inefficient algorithms, such as brute force approaches.
- Testing considerations: testing with different input cases, including edge cases.