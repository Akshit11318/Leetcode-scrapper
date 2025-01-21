## Check If Word Is Valid After Substitutions
**Problem Link:** https://leetcode.com/problems/check-if-word-is valid-after-substitutions/description

**Problem Statement:**
- Input: A string `s` containing only the characters `'a'`, `'b'`, and `'c'`.
- Constraints: The string `s` is non-empty and consists only of the characters `'a'`, `'b'`, and `'c'`.
- Expected Output: Return `true` if the string is valid after performing all possible substitutions, and `false` otherwise.
- Key Requirements: A string is valid if all occurrences of `"ab"` can be replaced by `"c"`.
- Example Test Cases:
  - Input: `s = "abcc"`; Output: `true`
  - Input: `s = "abc"`; Output: `false`
  - Input: `s = "aabcbc"`; Output: `true`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Perform all possible substitutions of `"ab"` with `"c"` and check if the resulting string is valid.
- Step-by-step breakdown of the solution:
  1. Initialize a flag to track if any substitution was made.
  2. Loop through the string to find occurrences of `"ab"`.
  3. Replace `"ab"` with `"c"` and update the flag.
  4. Repeat steps 2-3 until no more substitutions can be made.
  5. Check if the resulting string is valid.

```cpp
bool isValid(string s) {
    bool substituted;
    do {
        substituted = false;
        for (int i = 0; i < s.length() - 1; ++i) {
            if (s[i] == 'a' && s[i + 1] == 'b') {
                s.replace(i, 2, "c");
                substituted = true;
            }
        }
    } while (substituted);
    return !s.empty() && s.find("ab") == string::npos;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of the string and $m$ is the number of substitutions made. This occurs because in the worst-case scenario, we might need to iterate over the entire string for each substitution.
> - **Space Complexity:** $O(n)$, as we are modifying the input string in place, but the `replace` function might create temporary strings.
> - **Why these complexities occur:** The brute force approach involves repeated iterations over the string and potential creation of temporary strings during substitution, leading to these complexities.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can use a stack to track the characters and perform substitutions on the fly.
- Detailed breakdown of the approach:
  1. Initialize an empty stack.
  2. Iterate over the input string.
  3. If the current character is `'c'` or the stack is empty, push it onto the stack.
  4. If the current character is `'b'` and the top of the stack is `'a'`, pop the top element ( effectively substituting `"ab"` with `"c"`).
  5. After iterating over the entire string, check if the stack contains any `'ab'` pairs.
- Why further optimization is impossible: This approach minimizes the number of iterations and uses a stack to efficiently perform substitutions, making it optimal.

```cpp
bool isValid(string s) {
    stack<char> stk;
    for (char c : s) {
        if (c == 'c' || stk.empty() || stk.top() != 'a') {
            stk.push(c);
        } else if (c == 'b' && stk.top() == 'a') {
            stk.pop();
        }
    }
    return stk.size() == 0 || (stk.size() == 1 && stk.top() == 'c');
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This occurs because we are iterating over the string once.
> - **Space Complexity:** $O(n)$, as in the worst-case scenario, we might need to push all characters onto the stack.
> - **Optimality proof:** This approach is optimal because it minimizes the number of iterations and uses a stack to efficiently perform substitutions, resulting in the best possible time and space complexities.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Stack operations, string manipulation, and substitution.
- Problem-solving patterns identified: Using a stack to track and substitute characters efficiently.
- Optimization techniques learned: Minimizing iterations and using data structures to reduce complexity.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as empty strings or strings with only one character.
- Edge cases to watch for: Handling strings with repeated substitutions, such as `"abab"`.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexities.
- Testing considerations: Thoroughly testing the solution with various input cases, including edge cases and boundary conditions.