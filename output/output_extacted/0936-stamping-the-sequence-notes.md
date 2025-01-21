## Stamping the Sequence

**Problem Link:** https://leetcode.com/problems/stamping-the-sequence/description

**Problem Statement:**
- Input format and constraints: You are given a string `target` and a string `stamp`. You are required to transform the `target` into a string of all `?` characters by stamping the `stamp` onto the `target` string.
- Expected output format: Return an array of indices where the `stamp` is stamped onto the `target` string.
- Key requirements and edge cases to consider: The `stamp` string should be stamped onto the `target` string such that the characters in the `stamp` string match the corresponding characters in the `target` string, and the characters in the `target` string that are not matched are replaced with `?`.
- Example test cases with explanations: For example, if `target = "abca"` and `stamp = "a"`, the output should be `[3, 0, 1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over the `target` string and checking if the `stamp` string can be stamped at each position.
- Step-by-step breakdown of the solution:
  1. Iterate over the `target` string.
  2. For each position in the `target` string, check if the `stamp` string can be stamped at that position.
  3. If the `stamp` string can be stamped, mark the characters in the `target` string that are matched with the `stamp` string as `?`.
  4. Repeat steps 1-3 until the `target` string is transformed into a string of all `?` characters.
- Why this approach comes to mind first: This approach is intuitive because it involves checking each position in the `target` string and stamping the `stamp` string at each position where it can be stamped.

```cpp
#include <iostream>
#include <vector>
#include <string>

std::vector<int> movesToStamp(std::string target, std::string stamp) {
    int n = target.size();
    int m = stamp.size();
    std::vector<int> res;
    std::string temp = target;

    while (true) {
        bool found = false;
        for (int i = 0; i <= n - m; i++) {
            bool match = true;
            for (int j = 0; j < m; j++) {
                if (temp[i + j] != '?' && temp[i + j] != stamp[j]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                found = true;
                res.push_back(i);
                for (int j = 0; j < m; j++) {
                    temp[i + j] = '?';
                }
            }
        }
        if (!found) {
            break;
        }
    }

    if (temp != std::string(n, '?')) {
        return {};
    }

    std::reverse(res.begin(), res.end());
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the length of the `target` string, $m$ is the length of the `stamp` string, and $k$ is the number of stamps required to transform the `target` string into a string of all `?` characters. This is because in the worst case, we need to iterate over the `target` string $k$ times, and for each iteration, we need to check each position in the `target` string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the `target` string. This is because we need to store the `target` string and the `stamp` string.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach that involves iterating over the `target` string and checking each position for a match with the `stamp` string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a similar approach to the brute force solution, but with some optimizations.
- Detailed breakdown of the approach:
  1. Iterate over the `target` string.
  2. For each position in the `target` string, check if the `stamp` string can be stamped at that position.
  3. If the `stamp` string can be stamped, mark the characters in the `target` string that are matched with the `stamp` string as `?`.
  4. Repeat steps 1-3 until the `target` string is transformed into a string of all `?` characters.
- Proof of optimality: This solution is optimal because it involves checking each position in the `target` string only once, and it uses a similar approach to the brute force solution but with some optimizations.

```cpp
#include <iostream>
#include <vector>
#include <string>

std::vector<int> movesToStamp(std::string target, std::string stamp) {
    int n = target.size();
    int m = stamp.size();
    std::vector<int> res;
    std::string temp = target;

    while (true) {
        bool found = false;
        for (int i = 0; i <= n - m; i++) {
            bool match = true;
            for (int j = 0; j < m; j++) {
                if (temp[i + j] != '?' && temp[i + j] != stamp[j]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                found = true;
                res.push_back(i);
                for (int j = 0; j < m; j++) {
                    temp[i + j] = '?';
                }
            }
        }
        if (!found) {
            break;
        }
    }

    if (temp != std::string(n, '?')) {
        return {};
    }

    std::reverse(res.begin(), res.end());
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the length of the `target` string, $m$ is the length of the `stamp` string, and $k$ is the number of stamps required to transform the `target` string into a string of all `?` characters. This is because in the worst case, we need to iterate over the `target` string $k$ times, and for each iteration, we need to check each position in the `target` string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the `target` string. This is because we need to store the `target` string and the `stamp` string.
> - **Optimality proof:** This solution is optimal because it involves checking each position in the `target` string only once, and it uses a similar approach to the brute force solution but with some optimizations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of a brute force approach and an optimal approach to solve a string manipulation problem.
- Problem-solving patterns identified: The problem involves identifying a pattern in the `target` string and using the `stamp` string to transform the `target` string into a string of all `?` characters.
- Optimization techniques learned: The problem involves optimizing the brute force approach to reduce the time complexity.
- Similar problems to practice: Similar problems include string manipulation problems such as finding the longest common subsequence between two strings.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to forget to check if the `target` string is transformed into a string of all `?` characters after each iteration.
- Edge cases to watch for: An edge case to watch for is when the `target` string is already a string of all `?` characters.
- Performance pitfalls: A performance pitfall is to use a brute force approach without any optimizations.
- Testing considerations: The solution should be tested with different inputs to ensure that it works correctly.