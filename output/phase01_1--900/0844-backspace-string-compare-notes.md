## Backspace String Compare
**Problem Link:** https://leetcode.com/problems/backspace-string-compare/description

**Problem Statement:**
- Input format: Two strings `s` and `t`, both consisting of lowercase letters and `#` characters.
- Constraints: $1 \leq s.length, t.length \leq 200$ and $s, t$ only contain lowercase letters and `#` characters.
- Expected output format: A boolean indicating whether the strings are equal after applying backspace operations.
- Key requirements and edge cases to consider: Backspace operations (`#`) delete the character preceding them, unless there is no preceding character.
- Example test cases with explanations:
  - `s = "ab#c", t = "ad#c"`: Both strings become `"ac"` after applying backspace operations, so they are equal.
  - `s = "ab##", t = "c#d#"`: Both strings become `""` after applying backspace operations, so they are equal.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Apply backspace operations to both strings and compare the resulting strings.
- Step-by-step breakdown of the solution:
  1. Create a stack for each string to keep track of characters that are not deleted by backspace operations.
  2. Iterate through each string. When a character is encountered, push it onto the stack. When a `#` is encountered, pop the top character from the stack if it is not empty.
  3. After processing both strings, compare the stacks. If they are equal, the strings are equal after applying backspace operations.
- Why this approach comes to mind first: It directly simulates the backspace operations and then compares the results.

```cpp
#include <iostream>
#include <stack>
#include <string>

bool backspaceCompare(std::string s, std::string t) {
    std::stack<char> stackS, stackT;
    for (char c : s) {
        if (c == '#') {
            if (!stackS.empty()) stackS.pop();
        } else {
            stackS.push(c);
        }
    }
    for (char c : t) {
        if (c == '#') {
            if (!stackT.empty()) stackT.pop();
        } else {
            stackT.push(c);
        }
    }
    while (!stackS.empty() && !stackT.empty()) {
        if (stackS.top() != stackT.top()) return false;
        stackS.pop();
        stackT.pop();
    }
    return stackS.empty() && stackT.empty();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of strings $s$ and $t$ respectively. This is because we process each character in both strings once.
> - **Space Complexity:** $O(n + m)$, as in the worst case, we might end up storing all characters from both strings in the stacks.
> - **Why these complexities occur:** The time complexity is linear because we make a single pass through each string. The space complexity is also linear because in the worst case, we store all characters from both strings.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using stacks, we can use two pointers starting from the end of each string and move backwards. When a `#` is encountered, we skip the next character.
- Detailed breakdown of the approach:
  1. Initialize two pointers at the end of each string.
  2. Move the pointers backwards. When a `#` is encountered, skip the next character and the `#` itself.
  3. Compare characters at the current positions of the pointers. If they are different, return false.
  4. If one pointer reaches the beginning of its string and the other does not, return false.
  5. If both pointers reach the beginning of their strings without finding any differences, return true.
- Proof of optimality: This approach has the same time complexity as the brute force approach but avoids the extra space needed for stacks.

```cpp
bool backspaceCompare(std::string s, std::string t) {
    int i = s.size() - 1, j = t.size() - 1;
    int skipS = 0, skipT = 0;
    while (i >= 0 || j >= 0) {
        while (i >= 0) {
            if (s[i] == '#') {
                skipS++;
                i--;
            } else if (skipS > 0) {
                skipS--;
                i--;
            } else {
                break;
            }
        }
        while (j >= 0) {
            if (t[j] == '#') {
                skipT++;
                j--;
            } else if (skipT > 0) {
                skipT--;
                j--;
            } else {
                break;
            }
        }
        if (i >= 0 && j >= 0 && s[i] != t[j]) return false;
        if ((i >= 0) != (j >= 0)) return false;
        i--;
        j--;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of strings $s$ and $t$ respectively.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the pointers and skip counters.
> - **Optimality proof:** This is the optimal solution because it achieves the same result as the brute force approach but with constant space complexity, making it more efficient in terms of memory usage.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using two pointers to compare strings from the end, handling backspace operations by skipping characters.
- Problem-solving patterns identified: Starting from the end of strings to handle backspace operations efficiently.
- Optimization techniques learned: Avoiding unnecessary data structures like stacks to reduce space complexity.
- Similar problems to practice: Other string comparison problems with special operations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling the `#` character, not checking for edge cases like empty strings.
- Edge cases to watch for: Strings of different lengths, strings with only `#` characters.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexity.
- Testing considerations: Thoroughly testing with various input cases, including edge cases and boundary conditions.