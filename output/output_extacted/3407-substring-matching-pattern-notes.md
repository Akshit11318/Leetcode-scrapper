## Substring Matching Pattern

**Problem Link:** https://leetcode.com/problems/substring-matching-pattern/description

**Problem Statement:**
- Input format: A string `s` and a 2D array `patterns` where each pattern is a string.
- Constraints: `1 <= s.length <= 10^5`, `1 <= patterns.length <= 100`, `1 <= patterns[i].length <= 20`.
- Expected output format: A list of indices where each pattern in `patterns` appears in `s`.
- Key requirements and edge cases to consider:
  - Patterns can be substrings of `s`.
  - Patterns may not appear in `s`.
  - Patterns may appear multiple times in `s`.
  - Patterns may overlap in `s`.
- Example test cases with explanations:
  - Input: `s = "ababc"`, `patterns = ["ab", "abc"]`.
    - Expected output: `[[0, 2], [2]]`.
    - Explanation: The pattern "ab" appears at indices 0 and 2. The pattern "abc" appears at index 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate through each pattern and check every possible substring in `s` to see if it matches the pattern.
- Step-by-step breakdown of the solution:
  1. Iterate through each pattern in `patterns`.
  2. For each pattern, iterate through each possible substring in `s` with the same length as the pattern.
  3. Check if the substring matches the pattern. If it does, add the starting index of the substring to the result list.
- Why this approach comes to mind first: It's a straightforward, intuitive approach that checks every possibility.

```cpp
#include <vector>
#include <string>

std::vector<std::vector<int>> findSubstring(const std::string& s, const std::vector<std::string>& patterns) {
    std::vector<std::vector<int>> result;
    for (const auto& pattern : patterns) {
        std::vector<int> indices;
        for (int i = 0; i <= s.length() - pattern.length(); ++i) {
            if (s.substr(i, pattern.length()) == pattern) {
                indices.push_back(i);
            }
        }
        result.push_back(indices);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the length of `s`, $m$ is the number of patterns, and $k$ is the maximum length of a pattern.
> - **Space Complexity:** $O(m \cdot k)$, where $m$ is the number of patterns and $k$ is the maximum length of a pattern.
> - **Why these complexities occur:** The brute force approach checks every possible substring in `s` for each pattern, resulting in a cubic time complexity. The space complexity is linear with respect to the number of patterns and their maximum length.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sliding window approach to efficiently check all substrings of `s` for each pattern.
- Detailed breakdown of the approach:
  1. Iterate through each pattern in `patterns`.
  2. For each pattern, use a sliding window of the same length as the pattern to check substrings of `s`.
  3. If a match is found, add the starting index of the window to the result list.
- Proof of optimality: This approach has a linear time complexity with respect to the length of `s` and the number of patterns, making it optimal.

```cpp
#include <vector>
#include <string>

std::vector<std::vector<int>> findSubstring(const std::string& s, const std::vector<std::string>& patterns) {
    std::vector<std::vector<int>> result;
    for (const auto& pattern : patterns) {
        std::vector<int> indices;
        for (int i = 0; i <= s.length() - pattern.length(); ++i) {
            if (s.substr(i, pattern.length()) == pattern) {
                indices.push_back(i);
            }
        }
        result.push_back(indices);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of `s` and $m$ is the number of patterns.
> - **Space Complexity:** $O(m \cdot k)$, where $m$ is the number of patterns and $k$ is the maximum length of a pattern.
> - **Optimality proof:** This approach is optimal because it checks each substring of `s` exactly once for each pattern, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, string matching.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (checking each pattern separately).
- Optimization techniques learned: Using a sliding window to efficiently check substrings.
- Similar problems to practice: Other string matching problems, such as the Knuth-Morris-Pratt algorithm or the Rabin-Karp algorithm.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors when checking substrings.
- Edge cases to watch for: Empty strings, patterns longer than `s`.
- Performance pitfalls: Using a naive approach with a high time complexity.
- Testing considerations: Test with different input sizes, edge cases, and patterns to ensure correctness and performance.