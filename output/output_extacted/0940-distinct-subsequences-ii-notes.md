## Distinct Subsequences II
**Problem Link:** https://leetcode.com/problems/distinct-subsequences-ii/description

**Problem Statement:**
- Input format: A string `s` containing only lowercase letters.
- Constraints: The length of `s` is between 1 and 2 * 10^5.
- Expected output format: The number of distinct subsequences of `s`.
- Key requirements and edge cases to consider: Handling sequences with repeated characters, ensuring distinctness of subsequences.
- Example test cases with explanations: 
  - Input: `s = "abc"`
    - Output: `7` 
    - Explanation: The distinct subsequences are `"a"`, `"b"`, `"c"`, `"ab"`, `"ac"`, `"bc"`, and `"abc"`.
  - Input: `s = "aaa"`
    - Output: `3` 
    - Explanation: The distinct subsequences are `"a"`, `"aa"`, and `"aaa"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of the input string and count the distinct ones.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences using bit manipulation or recursion.
  2. Store each subsequence in a set to ensure distinctness.
  3. Count the number of elements in the set as the result.
- Why this approach comes to mind first: It directly addresses the requirement of finding distinct subsequences but lacks efficiency due to the exponential number of subsequences.

```cpp
#include <iostream>
#include <set>
#include <string>

int distinctSubseqII(const std::string& s) {
    std::set<std::string> subsequences;
    int n = s.size();
    for (int mask = 0; mask < (1 << n); ++mask) {
        std::string sub;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                sub += s[i];
            }
        }
        subsequences.insert(sub);
    }
    return subsequences.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input string. The $2^n$ term comes from generating all possible subsequences, and the $n$ term comes from the string concatenation operation inside the loop.
> - **Space Complexity:** $O(2^n \cdot n)$, as in the worst case, we might store all possible subsequences in the set.
> - **Why these complexities occur:** The brute force approach involves generating all possible subsequences, which leads to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to keep track of the count of distinct subsequences ending at each position.
- Detailed breakdown of the approach:
  1. Initialize an array `dp` where `dp[i]` represents the count of distinct subsequences ending at index `i`.
  2. For each character in the string, update `dp[i]` by considering two cases: including the current character in the subsequence and excluding it.
  3. To handle repeated characters and ensure distinctness, use a `lastOccurrence` map to track the last index where each character occurred.
- Proof of optimality: This approach ensures that each distinct subsequence is counted exactly once and avoids the exponential complexity of the brute force approach.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int distinctSubseqII(const std::string& s) {
    int n = s.size();
    std::unordered_map<char, int> lastOccurrence;
    long long dp[n + 1] = {0};
    dp[0] = 1; // Empty string is one distinct subsequence
    
    for (int i = 1; i <= n; ++i) {
        dp[i] = dp[i - 1] * 2; // Include or exclude the current character
        if (lastOccurrence.find(s[i - 1]) != lastOccurrence.end()) {
            // If the character has occurred before, subtract the count of subsequences that end with this character
            dp[i] -= dp[lastOccurrence[s[i - 1]]];
        }
        lastOccurrence[s[i - 1]] = i - 1; // Update last occurrence
    }
    return dp[n] - 1; // Subtract 1 because we don't count the empty string as a subsequence
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, as we make a single pass through the string.
> - **Space Complexity:** $O(n)$, for storing the dynamic programming array and the last occurrence map.
> - **Optimality proof:** This approach has linear time complexity, which is optimal for this problem since we must at least read the input string once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, handling repeated elements, and ensuring distinctness of subsequences.
- Problem-solving patterns identified: Breaking down the problem into smaller subproblems and using memoization (dynamic programming) to avoid redundant computation.
- Optimization techniques learned: Using a `lastOccurrence` map to efficiently track and update the counts of distinct subsequences.
- Similar problems to practice: Other dynamic programming problems involving strings and subsequences.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect indexing, forgetting to initialize variables, and not handling edge cases properly.
- Edge cases to watch for: Empty string, single-character string, and strings with all identical characters.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases and large inputs to ensure correctness and efficiency.