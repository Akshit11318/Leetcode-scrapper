## Partition Labels
**Problem Link:** https://leetcode.com/problems/partition-labels/description

**Problem Statement:**
- Input format: A string `S` of length `n`.
- Constraints: `1 <= S.length <= 500`.
- Expected output format: A list of integers representing the partition lengths.
- Key requirements: Partition the string into the fewest number of disjoint, non-empty substrings such that each substring contains all occurrences of every character it contains.
- Example test cases:
  - Input: `"ababcbacadefegdehijhklij"`
  - Output: `[9,7,8]`
  - Explanation: The partition is `"ababcbaca", "defegde", "hijhklij"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible partitions of the string and check if each substring contains all occurrences of every character it contains.
- Step-by-step breakdown of the solution:
  1. Generate all possible partitions of the string.
  2. For each partition, check if each substring contains all occurrences of every character it contains.
  3. If a partition satisfies the condition, calculate the partition lengths.
- Why this approach comes to mind first: It's a straightforward approach that tries all possibilities.

```cpp
#include <iostream>
#include <vector>
#include <string>

vector<int> partitionLabels(string S) {
    vector<int> result;
    for (int i = 0; i < S.length(); i++) {
        for (int j = i + 1; j <= S.length(); j++) {
            string substr = S.substr(i, j - i);
            bool valid = true;
            for (char c : substr) {
                int first = substr.find(c);
                int last = substr.rfind(c);
                if (substr.find(c, first + 1) != last) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                result.push_back(j - i);
                i = j - 1;
                break;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string. This is because we're generating all possible partitions and checking each substring.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string. This is because we're storing the partition lengths.
> - **Why these complexities occur:** The brute force approach tries all possible partitions and checks each substring, resulting in high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a `last` array to store the last index of each character in the string.
- Detailed breakdown of the approach:
  1. Create a `last` array to store the last index of each character in the string.
  2. Initialize the result vector and the current partition length.
  3. Iterate through the string, updating the current partition length and the result vector as needed.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is the best possible time complexity because we need to iterate through the string at least once.

```cpp
#include <iostream>
#include <vector>
#include <string>

vector<int> partitionLabels(string S) {
    vector<int> last(26, 0);
    for (int i = 0; i < S.length(); i++) {
        last[S[i] - 'a'] = i;
    }
    vector<int> result;
    int anchor = 0, j = 0;
    for (int i = 0; i < S.length(); i++) {
        j = max(j, last[S[i] - 'a']);
        if (i == j) {
            result.push_back(i - anchor + 1);
            anchor = i + 1;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we're iterating through the string twice.
> - **Space Complexity:** $O(1)$, because we're using a fixed-size array to store the last index of each character.
> - **Optimality proof:** This approach has the best possible time complexity because we need to iterate through the string at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Using a `last` array to store the last index of each character.
- Problem-solving patterns: Iterating through the string and updating the result vector as needed.
- Optimization techniques: Using a `last` array to avoid unnecessary iterations.
- Similar problems to practice: Other string partitioning problems.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the `last` array correctly.
- Edge cases to watch for: Empty strings or strings with a single character.
- Performance pitfalls: Using a brute force approach with high time complexity.
- Testing considerations: Test the function with different input strings and edge cases.