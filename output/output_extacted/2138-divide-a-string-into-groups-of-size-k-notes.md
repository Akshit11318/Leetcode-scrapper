## Divide a String into Groups of Size K
**Problem Link:** https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description

**Problem Statement:**
- Input: A non-empty string `s` and an integer `k`.
- Constraints: `1 <= s.length <= 1000`, `1 <= k <= 1000`, `s` consists of lowercase letters, and `k` is a positive integer.
- Expected Output: Divide `s` into groups of size `k`. If the remainder of the division of the length of `s` by `k` is not zero, fill the remaining groups with a filler character `filler`.
- Key Requirements:
  - Divide the string into groups of size `k`.
  - If the length of `s` is not a multiple of `k`, fill the remaining groups with `filler`.
  - Return a list of strings representing the divided groups.
- Example Test Cases:
  - Input: `s = "abcdefghi", k = 3, filler = "x"`, Output: `["abc", "def", "ghi"]`.
  - Input: `s = "abcdefghij", k = 3, filler = "x"`, Output: `["abc", "def", "ghi", "jxx"]`.

---

### Brute Force Approach
**Explanation:**
- Initialize an empty list `result` to store the divided groups.
- Iterate over the string `s` in steps of `k`.
- For each iteration, append the substring of length `k` to `result`.
- If the remaining characters in `s` are less than `k`, append the remaining characters and fill the rest with `filler`.

```cpp
#include <vector>
#include <string>

std::vector<std::string> divideString(std::string s, int k, char filler) {
    std::vector<std::string> result;
    int i = 0;
    while (i < s.length()) {
        if (i + k <= s.length()) {
            result.push_back(s.substr(i, k));
        } else {
            std::string group = s.substr(i);
            while (group.length() < k) {
                group += filler;
            }
            result.push_back(group);
        }
        i += k;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`, since we are iterating over `s` once.
> - **Space Complexity:** $O(n)$, as we are storing the divided groups in the `result` list.
> - **Why these complexities occur:** The time complexity is linear due to the single pass over `s`, and the space complexity is also linear as we are storing all characters of `s` in the `result` list.

---

### Optimal Approach (Required)
**Explanation:**
- The brute force approach is already optimal for this problem, as we need to iterate over the entire string `s` to divide it into groups of size `k`.
- However, we can slightly improve the implementation by using a more efficient way to append the remaining characters and fill them with `filler`.

```cpp
#include <vector>
#include <string>

std::vector<std::string> divideString(std::string s, int k, char filler) {
    std::vector<std::string> result;
    for (int i = 0; i < s.length(); i += k) {
        std::string group = s.substr(i, k);
        if (group.length() < k) {
            group.resize(k, filler);
        }
        result.push_back(group);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`.
> - **Space Complexity:** $O(n)$, as we are storing the divided groups in the `result` list.
> - **Optimality proof:** This is the optimal solution because we must iterate over `s` at least once to divide it into groups of size `k`, and we are doing so in a single pass.

---

### Final Notes

**Learning Points:**
- Dividing a string into groups of a specified size.
- Handling remaining characters when the length of the string is not a multiple of the group size.
- Using `std::string::substr` and `std::string::resize` to manipulate strings.

**Mistakes to Avoid:**
- Not checking if the length of the string is a multiple of the group size.
- Not filling the remaining groups with the filler character.
- Not using efficient string manipulation methods.

**Similar Problems to Practice:**
- Divide a string into groups of varying sizes.
- Divide a string into groups based on a specific delimiter.
- Implement a string tokenizer to divide a string into groups based on a set of delimiters.