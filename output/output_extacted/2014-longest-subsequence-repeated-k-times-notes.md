## Longest Subsequence Repeated K Times

**Problem Link:** https://leetcode.com/problems/longest-subsequence-repeated-k-times/description

**Problem Statement:**
- Input format and constraints: Given a string `s` and an integer `k`, find the length of the longest subsequence that repeats `k` times.
- Expected output format: Return the length of the longest subsequence as an integer.
- Key requirements and edge cases to consider:
  - `1 <= k <= s.length <= 1000`
  - `s` consists of lowercase English letters
  - The subsequence must appear exactly `k` times
- Example test cases with explanations:
  - For `s = "aabbcaabc"`, `k = 2`, the longest repeated subsequence is `"aab"` which appears twice, so the answer is `3`.
  - For `s = "aabbcaabc"`, `k = 3`, there is no subsequence that appears exactly three times, so the answer is `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the longest repeated subsequence, we can generate all possible subsequences of `s` and check which ones appear exactly `k` times.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of `s`.
  2. For each subsequence, count how many times it appears in `s`.
  3. If a subsequence appears exactly `k` times, update the maximum length if necessary.
- Why this approach comes to mind first: It's a straightforward approach that checks all possibilities, ensuring we don't miss the longest repeated subsequence.

```cpp
#include <iostream>
#include <vector>
#include <string>

int longestSubsequenceRepeatedKTimes(std::string s, int k) {
    int n = s.length();
    int maxLength = 0;

    // Generate all possible subsequences
    for (int mask = 1; mask < (1 << n); ++mask) {
        std::string subsequence;
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i))) {
                subsequence += s[i];
            }
        }

        // Count occurrences of the subsequence
        int count = 0;
        for (int i = 0; i <= n - subsequence.length(); ++i) {
            bool match = true;
            for (int j = 0; j < subsequence.length(); ++j) {
                if (s[i + j] != subsequence[j]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                ++count;
            }
        }

        // Update maxLength if subsequence appears exactly k times
        if (count == k && subsequence.length() > maxLength) {
            maxLength = subsequence.length();
        }
    }

    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m)$, where $n$ is the length of `s` and $m$ is the average length of subsequences. This is because we generate $2^n$ subsequences, and for each, we potentially scan `s` to count occurrences.
> - **Space Complexity:** $O(n)$, for storing the current subsequence.
> - **Why these complexities occur:** The exponential time complexity comes from generating all possible subsequences, and the linear space complexity is due to storing the current subsequence being checked.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all possible subsequences, we can use a recursive approach with memoization to efficiently explore the search space. This problem is closely related to the Longest Common Subsequence (LCS) problem but with the additional constraint of `k` repetitions.
- Detailed breakdown of the approach:
  1. Define a recursive function that explores all possible subsequences but uses memoization to avoid redundant computations.
  2. Within the recursive function, check if the current subsequence appears exactly `k` times in `s`.
  3. If it does, update the maximum length found so far.
- Proof of optimality: This approach ensures that we explore all possible subsequences without redundant work, thanks to memoization, making it optimal in terms of reducing unnecessary computations.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

int countOccurrences(const string& s, const string& sub) {
    int count = 0;
    for (int i = 0; i <= s.length() - sub.length(); ++i) {
        bool match = true;
        for (int j = 0; j < sub.length(); ++j) {
            if (s[i + j] != sub[j]) {
                match = false;
                break;
            }
        }
        if (match) {
            ++count;
        }
    }
    return count;
}

int longestSubsequenceRepeatedKTimes(string s, int k) {
    unordered_map<string, int> memo;
    int maxLength = 0;

    function<void(string)> recurse = [&](string current) {
        if (memo.find(current) != memo.end()) {
            return;
        }
        memo[current] = 1;

        int count = countOccurrences(s, current);
        if (count == k && current.length() > maxLength) {
            maxLength = current.length();
        }

        for (char c = 'a'; c <= 'z'; ++c) {
            recurse(current + c);
        }
    };

    recurse("");
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(26^n)$ in the worst case without memoization, but significantly reduced with memoization. However, the actual complexity is difficult to express precisely due to the effects of memoization and the problem's constraints.
> - **Space Complexity:** $O(n)$ for the recursion stack and memoization.
> - **Optimality proof:** The use of memoization ensures that each subsequence is processed exactly once, avoiding redundant computations and making the approach optimal in terms of computational efficiency.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive exploration with memoization, counting occurrences of subsequences.
- Problem-solving patterns identified: Using memoization to avoid redundant computations in recursive problems.
- Optimization techniques learned: Memoization to reduce computational complexity.
- Similar problems to practice: Longest Common Subsequence, Shortest Common Supersequence.

**Mistakes to Avoid:**
- Common implementation errors: Not using memoization correctly, missing edge cases (e.g., empty string, `k=0`).
- Edge cases to watch for: Handling the base case of recursion correctly, ensuring memoization is properly implemented.
- Performance pitfalls: Not using memoization, leading to exponential time complexity without bounds.
- Testing considerations: Thoroughly test with various inputs, including edge cases and large inputs to ensure the solution scales well.