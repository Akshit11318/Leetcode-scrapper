## Check If All As Appears Before All Bs

**Problem Link:** https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` consisting of characters `a` and `b`.
- Expected output format: The output should be a boolean indicating whether all `a`s appear before all `b`s in the string.
- Key requirements and edge cases to consider: 
  - The string can be empty.
  - The string may contain only `a`s or only `b`s.
  - The string may contain a mix of `a`s and `b`s.

Example test cases with explanations:
- `s = "aaabbb"`: Returns `True` because all `a`s appear before all `b`s.
- `s = "ab"`: Returns `True` because all `a`s appear before all `b`s.
- `s = "ba"`: Returns `False` because not all `a`s appear before all `b`s.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To check if all `a`s appear before all `b`s, we can iterate through the string and keep track of when we encounter the first `b`. If we encounter an `a` after the first `b`, we return `False`.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `hasSeenB` to `False`.
  2. Iterate through the string.
  3. If we encounter a `b`, set `hasSeenB` to `True`.
  4. If we encounter an `a` and `hasSeenB` is `True`, return `False`.
  5. If we finish iterating through the string without returning `False`, return `True`.

```cpp
bool checkString(string s) {
    bool hasSeenB = false;
    for (char c : s) {
        if (c == 'b') {
            hasSeenB = true;
        } else if (c == 'a' && hasSeenB) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we make a single pass through the string.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the `hasSeenB` variable.
> - **Why these complexities occur:** The time complexity is linear because we iterate through the string once. The space complexity is constant because we only use a single variable.

---

### Optimal Approach (Required)

The brute force approach is already optimal for this problem because we must examine each character in the string at least once to determine if all `a`s appear before all `b`s.

**Explanation:**
- Key insight that leads to optimal solution: We must iterate through the string to check the order of `a`s and `b`s.
- Detailed breakdown of the approach: The same as the brute force approach.
- Proof of optimality: Any algorithm must examine each character in the string at least once to determine the correct order, so the optimal time complexity is $O(n)$.

```cpp
bool checkString(string s) {
    bool hasSeenB = false;
    for (char c : s) {
        if (c == 'b') {
            hasSeenB = true;
        } else if (c == 'a' && hasSeenB) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space.
> - **Optimality proof:** The time complexity is optimal because we must examine each character in the string at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checking.
- Problem-solving patterns identified: Checking for a specific condition in a sequence.
- Optimization techniques learned: The importance of examining each element in a sequence when necessary.
- Similar problems to practice: Other problems involving sequence checking or validation.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty string.
- Edge cases to watch for: Empty string, string with only `a`s or only `b`s.
- Performance pitfalls: Using more complex data structures or algorithms than necessary.
- Testing considerations: Test with various input cases, including edge cases.