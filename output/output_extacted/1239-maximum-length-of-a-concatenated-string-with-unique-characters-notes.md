## Maximum Length of a Concatenated String with Unique Characters

**Problem Link:** https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description

**Problem Statement:**
- Input: An array of strings `arr`.
- Constraints: `1 <= arr.length <= 16`, `1 <= arr[i].length <= 100`, `arr[i]` consists of lowercase English letters.
- Expected output: The maximum length of a concatenated string with unique characters.
- Key requirements and edge cases to consider:
  - Handling empty input arrays.
  - Ensuring uniqueness of characters in the concatenated string.
- Example test cases with explanations:
  - Input: `["un","iq","ue"]`, Output: `4` (Explanation: `"un"` and `"iq"` have unique characters, and their length is `4`).
  - Input: `["cha","r","act","ers"]`, Output: `6` (Explanation: `"cha"` and `"r"` and `"act"` and `"ers"` have unique characters, and their length is `6`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible combinations of strings from the input array and check each combination for uniqueness of characters.
- Step-by-step breakdown of the solution:
  1. Initialize an empty set to store unique characters.
  2. Generate all possible combinations of strings using bit manipulation (for each string, either include it in the combination or not).
  3. For each combination, concatenate the strings and check if all characters are unique by iterating through the concatenated string and adding each character to the set. If the size of the set equals the length of the concatenated string, all characters are unique.
  4. Keep track of the maximum length of concatenated strings with unique characters.
- Why this approach comes to mind first: It's a straightforward method to ensure all possible combinations are considered.

```cpp
#include <vector>
#include <string>
#include <unordered_set>

class Solution {
public:
    int maxLength(std::vector<std::string>& arr) {
        int n = arr.size();
        int maxLen = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            std::string concat;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    concat += arr[i];
                }
            }
            if (isUnique(concat)) {
                maxLen = std::max(maxLen, (int)concat.size());
            }
        }
        return maxLen;
    }

    bool isUnique(const std::string& str) {
        std::unordered_set<char> uniqueChars;
        for (char c : str) {
            if (uniqueChars.find(c) != uniqueChars.end()) {
                return false;
            }
            uniqueChars.insert(c);
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string. This is because we generate $2^n$ combinations and for each combination, we check for uniqueness in $O(m)$ time.
> - **Space Complexity:** $O(m)$, as we store the concatenated string and the set of unique characters, which in the worst case can be of size $m$.
> - **Why these complexities occur:** The exponential time complexity is due to generating all possible combinations of strings, and the linear space complexity is due to storing the concatenated string and the set of unique characters.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use backtracking to efficiently explore all combinations of strings while ensuring uniqueness of characters at each step.
- Detailed breakdown of the approach:
  1. Define a recursive function that takes the current index in the array and the current concatenated string.
  2. In each recursive call, check if adding the current string to the concatenated string would result in a string with unique characters. If so, update the maximum length and recursively call the function with the next index.
  3. If adding the current string does not result in a string with unique characters, skip it and recursively call the function with the next index.
- Proof of optimality: This approach ensures that we explore all possible combinations of strings while avoiding unnecessary checks for uniqueness, thus achieving the optimal time complexity.

```cpp
class Solution {
public:
    int maxLength(std::vector<std::string>& arr) {
        int maxLen = 0;
        std::string concat;
        backtrack(arr, 0, concat, maxLen);
        return maxLen;
    }

    void backtrack(const std::vector<std::string>& arr, int idx, std::string& concat, int& maxLen) {
        if (idx == arr.size()) {
            if (isUnique(concat)) {
                maxLen = std::max(maxLen, (int)concat.size());
            }
            return;
        }
        backtrack(arr, idx + 1, concat, maxLen); // Skip current string
        if (isUnique(concat + arr[idx])) {
            concat += arr[idx];
            backtrack(arr, idx + 1, concat, maxLen); // Include current string
            concat.erase(concat.size() - arr[idx].size()); // Backtrack
        }
    }

    bool isUnique(const std::string& str) {
        std::unordered_set<char> uniqueChars;
        for (char c : str) {
            if (uniqueChars.find(c) != uniqueChars.end()) {
                return false;
            }
            uniqueChars.insert(c);
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string. This is because in the worst case, we still generate $2^n$ combinations, but we prune branches that would lead to non-unique strings.
> - **Space Complexity:** $O(m)$, as we store the concatenated string and the set of unique characters, which in the worst case can be of size $m$.
> - **Optimality proof:** This approach is optimal because it explores all possible combinations of strings while efficiently pruning branches that would not lead to a string with unique characters, thus minimizing the number of checks for uniqueness.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, bit manipulation, and pruning.
- Problem-solving patterns identified: Using backtracking to efficiently explore combinatorial spaces.
- Optimization techniques learned: Pruning branches that would not lead to a solution.
- Similar problems to practice: Other problems involving combinatorial optimization and pruning.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling the base case of the recursion or failing to properly backtrack.
- Edge cases to watch for: Handling empty input arrays or strings with duplicate characters.
- Performance pitfalls: Failing to prune branches that would not lead to a solution, resulting in exponential time complexity.
- Testing considerations: Thoroughly testing the solution with various input cases, including edge cases.