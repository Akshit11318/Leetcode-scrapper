## Optimal Partition of String

**Problem Link:** https://leetcode.com/problems/optimal-partition-of-string/description

**Problem Statement:**
- Input: a string `s`
- Output: the minimum number of unique characters in the optimal partition of `s`
- Key requirements: the optimal partition is the partition that minimizes the maximum number of unique characters in any substring
- Edge cases: empty string, single character string, string with all unique characters

Example test cases:
- Input: `s = "abacccd"` Output: `2` Explanation: The optimal partition is `"ab|ac|cc|d"`, and the maximum number of unique characters in any substring is 2.
- Input: `s = "abc"` Output: `3` Explanation: The optimal partition is `"a|b|c"`, and the maximum number of unique characters in any substring is 3.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: try all possible partitions of the string and calculate the maximum number of unique characters in each partition
- Step-by-step breakdown:
  1. Generate all possible partitions of the string
  2. For each partition, calculate the number of unique characters in each substring
  3. Calculate the maximum number of unique characters in any substring
  4. Return the minimum maximum number of unique characters across all partitions

```cpp
class Solution {
public:
    int partitionString(string s) {
        int n = s.size();
        int res = INT_MAX;
        for (int mask = 1; mask < (1 << n); mask++) {
            vector<int> partitions;
            int start = 0;
            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    partitions.push_back(i - start + 1);
                    start = i + 1;
                }
            }
            partitions.push_back(n - start);
            int maxUnique = 0;
            for (int i = 0; i < partitions.size(); i++) {
                int end = start + partitions[i] - 1;
                unordered_set<char> uniqueChars;
                for (int j = start; j <= end; j++) {
                    uniqueChars.insert(s[j]);
                }
                maxUnique = max(maxUnique, (int)uniqueChars.size());
                start = end + 1;
            }
            res = min(res, maxUnique);
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string. This is because we generate all possible partitions of the string, which takes $O(2^n)$ time, and for each partition, we calculate the number of unique characters in each substring, which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because we store the partitions and the unique characters in each substring.
> - **Why these complexities occur:** The brute force approach generates all possible partitions of the string, which results in an exponential time complexity. The space complexity is linear because we only store the partitions and the unique characters in each substring.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: we can use a greedy approach to partition the string. We start with an empty partition and add characters to it until we encounter a character that is already in the partition. At this point, we start a new partition.
- Detailed breakdown:
  1. Initialize an empty partition and a set to store the unique characters in the partition
  2. Iterate through the string, adding each character to the current partition and updating the set of unique characters
  3. If we encounter a character that is already in the set of unique characters, start a new partition and reset the set of unique characters
  4. Return the number of partitions

```cpp
class Solution {
public:
    int partitionString(string s) {
        int res = 0;
        unordered_set<char> uniqueChars;
        for (char c : s) {
            if (uniqueChars.find(c) != uniqueChars.end()) {
                res++;
                uniqueChars.clear();
            }
            uniqueChars.insert(c);
        }
        return res + 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we iterate through the string once, and for each character, we perform a constant-time operation (insertion into the set).
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because in the worst case, we may need to store all characters in the set of unique characters.
> - **Optimality proof:** This approach is optimal because it minimizes the number of partitions by starting a new partition only when necessary (i.e., when we encounter a character that is already in the current partition). This ensures that each partition has the minimum possible number of unique characters.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: greedy approach, set data structure
- Problem-solving patterns: partitioning problems, minimizing maximum values
- Optimization techniques: reducing the number of partitions by starting a new partition only when necessary

**Mistakes to Avoid:**
- Common implementation errors: forgetting to reset the set of unique characters when starting a new partition
- Edge cases: handling empty strings, single character strings, and strings with all unique characters
- Performance pitfalls: using a brute force approach, which can result in exponential time complexity.