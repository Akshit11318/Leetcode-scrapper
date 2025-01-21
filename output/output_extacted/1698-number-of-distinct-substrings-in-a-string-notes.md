## Number of Distinct Substrings in a String

**Problem Link:** https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/description

**Problem Statement:**
- Input format: A string `s`.
- Constraints: `1 <= s.length <= 10^5`.
- Expected output format: The number of distinct substrings in `s`.
- Key requirements: Count all unique substrings in the given string.
- Edge cases: Empty string, single character string, and strings with repeated characters.
- Example test cases:
  - Input: `s = "abc"`, Output: `6` (Because: `["a", "ab", "abc", "b", "bc", "c"]`).
  - Input: `s = "aaa"`, Output: `3` (Because: `["a", "aa", "aaa"]`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible substrings of the input string `s` and store them in a set to eliminate duplicates. Then, return the size of the set as the number of distinct substrings.
- Step-by-step breakdown:
  1. Initialize an empty set `distinctSubstrings` to store unique substrings.
  2. Iterate over the string `s` using two nested loops to generate all substrings.
  3. For each substring, check if it's already in the set `distinctSubstrings`. If not, add it.
  4. After checking all substrings, return the size of `distinctSubstrings`.

```cpp
#include <iostream>
#include <string>
#include <unordered_set>

int countDistinctSubstrings(const std::string& s) {
    std::unordered_set<std::string> distinctSubstrings;
    for (int i = 0; i < s.length(); ++i) {
        for (int j = i + 1; j <= s.length(); ++j) {
            std::string substring = s.substr(i, j - i);
            distinctSubstrings.insert(substring);
        }
    }
    return distinctSubstrings.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string `s`. This is because generating all substrings takes $O(n^2)$ time, and inserting each substring into the set takes $O(n)$ time due to string comparison.
> - **Space Complexity:** $O(n^2)$, as in the worst case, we might store all substrings in the set.
> - **Why these complexities occur:** The brute force approach involves generating all possible substrings and storing them, leading to high time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Utilize a `std::unordered_set` to store unique substrings and iterate through the string using a sliding window approach to generate substrings efficiently.
- Detailed breakdown:
  1. Initialize an empty set `distinctSubstrings` to store unique substrings.
  2. Use a single loop to iterate over the string, considering each character as a starting point for substrings.
  3. For each starting point, generate substrings of varying lengths and add them to the set.
  4. Return the size of the set after processing the entire string.

```cpp
#include <iostream>
#include <string>
#include <unordered_set>

int countDistinctSubstrings(const std::string& s) {
    std::unordered_set<std::string> distinctSubstrings;
    for (int i = 0; i < s.length(); ++i) {
        std::string substring;
        for (int j = i; j < s.length(); ++j) {
            substring += s[j];
            distinctSubstrings.insert(substring);
        }
    }
    return distinctSubstrings.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string `s`. This is because we're generating all substrings using a nested loop, but the set operations (insertion and lookup) are averaged $O(1)$.
> - **Space Complexity:** $O(n^2)$, as in the worst case, we might store all substrings in the set.
> - **Optimality proof:** This approach is optimal because we must consider all substrings to count distinct ones, and using a set minimizes the time spent on duplicate detection.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Using sets for efficient duplicate detection, and sliding window techniques for substring generation.
- Problem-solving patterns: Breaking down problems into smaller, manageable parts (like generating substrings), and applying data structures for efficiency.
- Optimization techniques: Minimizing unnecessary computations by using sets for duplicate detection.
- Similar problems to practice: Other string manipulation problems involving sets or maps for efficient processing.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases (like empty strings), and not validating inputs.
- Edge cases to watch for: Handling strings with repeated characters, and strings of varying lengths.
- Performance pitfalls: Using inefficient data structures (like lists) for storing unique substrings, which can lead to high time complexities.
- Testing considerations: Thoroughly testing the function with a variety of inputs, including edge cases and large strings.