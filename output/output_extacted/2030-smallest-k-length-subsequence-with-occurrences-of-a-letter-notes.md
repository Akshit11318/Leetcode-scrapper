## Smallest K-Length Subsequence with Occurrences of a Letter
**Problem Link:** https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/description

**Problem Statement:**
- Input: A string `s`, an integer `k`, and a character `letter`.
- Output: The lexicographically smallest subsequence of length `k` that contains the specified `letter` at least once.
- Constraints: `1 <= k <= s.length <= 1000`, `s` contains only lowercase English letters, and `letter` is a lowercase English letter.
- Key Requirements:
  - The subsequence must be of length `k`.
  - It must contain at least one occurrence of `letter`.
  - Among all possible subsequences satisfying the above conditions, the lexicographically smallest one is required.
- Edge Cases:
  - When `k` is equal to the length of `s`, the problem simplifies to finding the lexicographically smallest subsequence that includes `letter` at least once, which could be the string itself if it meets the condition.
  - If `s` does not contain `letter`, there is no valid subsequence.

**Example Test Cases:**
- Input: `s = "leet", k = 3, letter = "e"`; Output: `"eet"`
- Input: `s = "leetcode", k = 4, letter = "e"`; Output: `"ecde"`
- Input: `s = "xyz", k = 3, letter = "x"`; Output: `"xyz"`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible subsequences of `s` of length `k`, then filtering out those that do not contain `letter`, and finally selecting the lexicographically smallest one from the remaining subsequences.
- Step-by-step breakdown:
  1. Generate all subsequences of length `k` from `s`.
  2. Check each subsequence for the presence of `letter`.
  3. Compare the qualifying subsequences lexicographically to find the smallest one.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

void generateSubsequences(std::string s, int k, char letter, std::vector<std::string>& subsequences) {
    std::vector<bool> current(k);
    std::vector<std::string> result;
    generateSubsequenceHelper(s, k, letter, 0, current, result);
    subsequences = result;
}

void generateSubsequenceHelper(std::string s, int k, char letter, int index, std::vector<bool>& current, std::vector<std::string>& result) {
    if (index == k) {
        std::string subsequence;
        for (int i = 0; i < k; ++i) {
            subsequence += s[current[i]];
        }
        if (subsequence.find(letter) != std::string::npos) {
            result.push_back(subsequence);
        }
        return;
    }

    for (int i = 0; i < s.length(); ++i) {
        current[index] = i;
        generateSubsequenceHelper(s, k, letter, index + 1, current, result);
    }
}

std::string smallestSubsequence(std::string s, int k, char letter) {
    std::vector<std::string> subsequences;
    generateSubsequences(s, k, letter, subsequences);
    if (subsequences.empty()) return "";
    return *std::min_element(subsequences.begin(), subsequences.end());
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of `s`. This is because we generate all possible subsequences (which can be $2^n$ for a string of length $n$) and then check each of length $k$ for `letter`.
> - **Space Complexity:** $O(2^n \cdot n)$, for storing all subsequences.
> - **Why these complexities occur:** The brute force approach involves generating all possible subsequences and then filtering them, leading to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a monotonic stack to build the subsequence, ensuring it's lexicographically smallest and contains `letter`.
- Step-by-step breakdown:
  1. Initialize an empty stack and counters for the remaining characters and `letter`.
  2. Iterate through `s`, maintaining the stack such that it's always lexicographically smallest and ensuring `letter` is included.
  3. Use a counter to track how many times `letter` appears in the remaining part of `s` to ensure we include it in the subsequence.

```cpp
std::string smallestSubsequence(std::string s, int k, char letter) {
    int n = s.length();
    int letterCount = 0;
    for (char c : s) {
        if (c == letter) letterCount++;
    }
    
    std::string res;
    for (int i = 0; i < n; i++) {
        while (!res.empty() && res.back() > s[i] && res.length() + n - i > k && (res.back() != letter || letterCount > 0)) {
            if (res.back() == letter) letterCount++;
            res.pop_back();
        }
        
        if (res.length() < k) {
            res += s[i];
            if (s[i] == letter) letterCount--;
        }
        
        if (s[i] == letter) letterCount--;
    }
    
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `s`, since we make a single pass through `s`.
> - **Space Complexity:** $O(k)$, for storing the result subsequence.
> - **Optimality proof:** This approach ensures the subsequence is lexicographically smallest by maintaining a monotonic stack and includes `letter` by tracking its occurrences in the remaining part of `s`.

---

### Final Notes

**Learning Points:**
- The importance of monotonic stacks in solving string subsequence problems.
- How to optimize string manipulation problems by avoiding unnecessary operations.
- The use of counters to track specific characters in strings.

**Mistakes to Avoid:**
- Not considering the lexicographical order when building the subsequence.
- Failing to track the occurrences of `letter` in the remaining part of `s`.
- Not optimizing the solution to reduce time and space complexity.