## Count the Number of Good Partitions
**Problem Link:** https://leetcode.com/problems/count-the-number-of-good-partitions/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Constraints: `1 <= s.length <= 1000`, `1 <= k <= s.length`, and `s` consists only of lowercase English letters.
- Expected Output: The number of good partitions of `s` with `k` groups.
- Key Requirements: A partition of `s` is considered good if each of its `k` groups has a distinct character set.
- Edge Cases: When `k` is 1, there is only one partition, which includes the entire string. When `k` equals the length of `s`, each character forms its own group.
- Example Test Cases:
  - Input: `s = "abc", k = 2`, Output: `1`
  - Input: `s = "abac", k = 2`, Output: `1`
  - Input: `s = "aabb", k = 2`, Output: `0`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible partitions of `s` into `k` groups and then check each partition to see if it is good.
- Step-by-step breakdown:
  1. Generate all possible partitions of `s` into `k` groups.
  2. For each partition, check if each group has a distinct character set.
  3. Count the number of good partitions found.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <string>

using namespace std;

int countGoodPartitions(string s, int k) {
    int n = s.length();
    vector<vector<int>> partitions;
    vector<int> currentPartition;
    
    // Generate all possible partitions
    function<void(int, int)> generatePartitions = [&](int start, int groupsLeft) {
        if (start == n && groupsLeft == 0) {
            partitions.push_back(currentPartition);
            return;
        }
        
        for (int end = start + 1; end <= n && end - start <= n / (groupsLeft + 1); ++end) {
            currentPartition.push_back(end - start);
            generatePartitions(end, groupsLeft - 1);
            currentPartition.pop_back();
        }
    };
    
    generatePartitions(0, k);
    
    int goodCount = 0;
    for (const auto& partition : partitions) {
        unordered_set<unordered_set<char>> charSets;
        int start = 0;
        
        // Check if each group has a distinct character set
        bool isGood = true;
        for (int groupSize : partition) {
            unordered_set<char> charSet;
            for (int i = start; i < start + groupSize; ++i) {
                charSet.insert(s[i]);
            }
            if (charSets.find(charSet) != charSets.end()) {
                isGood = false;
                break;
            }
            charSets.insert(charSet);
            start += groupSize;
        }
        
        if (isGood) {
            goodCount++;
        }
    }
    
    return goodCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot k \cdot n)$, where $n$ is the length of the string `s`, due to generating all possible partitions and checking each one.
> - **Space Complexity:** $O(n \cdot k)$, for storing the current partition and the set of character sets.
> - **Why these complexities occur:** Generating all possible partitions leads to exponential time complexity. Checking each partition and storing the character sets contribute to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use dynamic programming to efficiently count the number of good partitions without generating all possible partitions explicitly.
- Detailed breakdown:
  1. Initialize a 2D table `dp` where `dp[i][j]` represents the number of ways to partition the first `i` characters into `j` groups with distinct character sets.
  2. Iterate over the string and update the `dp` table based on whether the current character can be added to an existing group or must start a new group.
  3. The final answer is stored in `dp[n][k]`, where `n` is the length of the string.

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int countGoodPartitions(string s, int k) {
    int n = s.length();
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
    dp[0][0] = 1;
    
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= min(i, k); ++j) {
            // If the current character is new, start a new group
            dp[i][j] += dp[i - 1][j - 1];
            // If the current character can be added to an existing group
            for (int prev = i - 1; prev >= 0; --prev) {
                if (s[prev] == s[i - 1]) {
                    dp[i][j] += dp[prev][j];
                    break;
                }
            }
        }
    }
    
    return dp[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the length of the string `s`.
> - **Space Complexity:** $O(n \cdot k)$, for the dynamic programming table.
> - **Optimality proof:** This approach efficiently counts the number of good partitions by avoiding the explicit generation of all possible partitions and using dynamic programming to store and reuse intermediate results.

---

### Final Notes

**Learning Points:**
- The importance of dynamic programming in solving combinatorial problems efficiently.
- How to approach partitioning problems with constraints on group properties.
- The value of identifying key insights that simplify the problem solution.

**Mistakes to Avoid:**
- Generating all possible partitions explicitly, leading to exponential time complexity.
- Not considering the distinct character set constraint when counting partitions.
- Failing to utilize dynamic programming to store and reuse intermediate results.