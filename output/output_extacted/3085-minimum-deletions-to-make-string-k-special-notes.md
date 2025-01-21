## Minimum Deletions to Make String K-Special
**Problem Link:** https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Constraints: `1 <= k <= 26`, `1 <= s.length <= 10^5`.
- Output: The minimum number of deletions required to make the string `k`-special.
- Key requirements: A string is `k`-special if it contains exactly `k` distinct characters.
- Edge cases: Handle cases where the string already has `k` or fewer distinct characters.

**Example Test Cases:**
- Input: `s = "xy", k = 1`, Output: `1`
- Input: `s = "aab", k = 2`, Output: `0`
- Input: `s = "abc", k = 1`, Output: `2`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all possible subsets of the string and count the number of deletions required to make each subset `k`-special.
- However, this approach is inefficient due to the large number of possible subsets.

```cpp
#include <iostream>
#include <string>
#include <unordered_set>

int minDeletionsBruteForce(const std::string& s, int k) {
    int minDeletions = INT_MAX;
    for (int mask = 0; mask < (1 << s.length()); ++mask) {
        std::string subset;
        for (int i = 0; i < s.length(); ++i) {
            if ((mask & (1 << i)) != 0) {
                subset += s[i];
            }
        }
        std::unordered_set<char> distinctChars(subset.begin(), subset.end());
        if (distinctChars.size() == k) {
            minDeletions = std::min(minDeletions, s.length() - subset.length());
        }
    }
    return minDeletions;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string. This is because we generate all possible subsets of the string and count the number of distinct characters in each subset.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because we store the subset of characters in a string.
> - **Why these complexities occur:** The brute force approach generates all possible subsets of the string, resulting in an exponential time complexity. The space complexity is linear because we store the subset of characters in a string.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a frequency count of characters in the string and sort them in descending order.
- We then iterate over the sorted frequency counts and delete characters until we have `k` distinct characters.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>

int minDeletionsOptimal(const std::string& s, int k) {
    std::unordered_map<char, int> freqCount;
    for (char c : s) {
        ++freqCount[c];
    }
    std::vector<int> freqCounts;
    for (const auto& pair : freqCount) {
        freqCounts.push_back(pair.second);
    }
    std::sort(freqCounts.rbegin(), freqCounts.rend());
    int deletions = 0;
    while (freqCounts.size() > k) {
        deletions += freqCounts.back();
        freqCounts.pop_back();
    }
    return deletions;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the string. This is because we sort the frequency counts of characters in the string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because we store the frequency counts of characters in a vector.
> - **Optimality proof:** This approach is optimal because it uses a greedy strategy to delete characters until we have `k` distinct characters. The sorting step ensures that we delete the characters with the smallest frequency counts first, resulting in the minimum number of deletions.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: frequency counting, sorting, and greedy algorithms.
- Problem-solving patterns identified: using frequency counts to solve problems involving distinct characters.
- Optimization techniques learned: using sorting to optimize the greedy algorithm.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases where the string already has `k` or fewer distinct characters.
- Edge cases to watch for: handling cases where the string is empty or has only one distinct character.
- Performance pitfalls: using inefficient algorithms such as the brute force approach.
- Testing considerations: testing the algorithm with different inputs and edge cases to ensure correctness.