## Group Shifted Strings
**Problem Link:** https://leetcode.com/problems/group-shifted-strings/description

**Problem Statement:**
- Input format: A list of strings `strings`.
- Constraints: `1 <= strings.length <= 200` and `1 <= strings[i].length <= 50`.
- Expected output format: A list of list of strings, where each sublist contains strings that are shifted versions of each other.
- Key requirements: Two strings are considered shifted if one can be obtained by shifting the characters of the other string by a certain number of positions.
- Example test cases:
  - Input: `["abc","bcd","acef","xyz","az","ba","a","z"]`
  - Output: `[["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]`

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every pair of strings to see if one can be obtained by shifting the characters of the other.
- Step-by-step breakdown:
  1. Create a function to check if two strings are shifted versions of each other.
  2. Use this function to group the strings.
- Why this approach comes to mind first: It directly addresses the problem statement by comparing each pair of strings.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

bool isShifted(const std::string& s1, const std::string& s2) {
    if (s1.length() != s2.length()) return false;
    int shift = (s2[0] - s1[0] + 26) % 26;
    for (int i = 1; i < s1.length(); ++i) {
        if ((s2[i] - s1[i] + 26) % 26 != shift) return false;
    }
    return true;
}

std::vector<std::vector<std::string>> groupStrings(std::vector<std::string>& strings) {
    std::unordered_map<std::string, std::vector<std::string>> groups;
    for (const auto& s : strings) {
        bool found = false;
        for (auto& group : groups) {
            if (isShifted(s, group.first)) {
                group.second.push_back(s);
                found = true;
                break;
            }
        }
        if (!found) {
            groups[s] = {s};
        }
    }
    std::vector<std::vector<std::string>> result;
    for (const auto& group : groups) {
        result.push_back(group.second);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string. This is because we compare each string with every other string, and for each comparison, we check each character.
> - **Space Complexity:** $O(n \cdot m)$, for storing the result and intermediate groups.
> - **Why these complexities occur:** The brute force approach involves comparing each pair of strings character by character, leading to quadratic time complexity. The space complexity is linear with respect to the input size because we store all the strings in the result and intermediate groups.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of comparing strings directly, we can normalize each string to a common form by shifting it so that 'a' becomes the first character. This way, strings that are shifted versions of each other will become identical after normalization.
- Detailed breakdown:
  1. Normalize each string by finding the shift needed to make the first character 'a', then apply this shift to all characters.
  2. Use a hashmap to group strings that are identical after normalization.
- Proof of optimality: This approach ensures that we only need to process each string once to normalize it and then group it, avoiding unnecessary comparisons between strings.

```cpp
std::vector<std::vector<std::string>> groupStrings(std::vector<std::string>& strings) {
    std::unordered_map<std::string, std::vector<std::string>> groups;
    for (const auto& s : strings) {
        std::string normalized;
        if (!s.empty()) {
            int shift = (s[0] - 'a' + 26) % 26;
            for (char c : s) {
                normalized += 'a' + (c - 'a' - shift + 26) % 26;
            }
        } else {
            normalized = s;
        }
        groups[normalized].push_back(s);
    }
    std::vector<std::vector<std::string>> result;
    for (const auto& group : groups) {
        result.push_back(group.second);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string. This is because we process each character of each string once to normalize it.
> - **Space Complexity:** $O(n \cdot m)$, for storing the normalized strings and the result.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations needed to group the strings, avoiding unnecessary comparisons and directly utilizing the properties of shifted strings.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the normalization of strings to a common form to simplify comparison.
- The problem-solving pattern identified is using a hashmap to group items based on a common characteristic.
- The optimization technique learned is to reduce the problem space by transforming the input into a more manageable form.

**Mistakes to Avoid:**
- Not considering the properties of the input data that can simplify the problem.
- Failing to normalize or transform the input data to reduce complexity.
- Not using appropriate data structures (like hashmaps) for efficient grouping.
- Overlooking the possibility of optimizing the algorithm by minimizing unnecessary comparisons.