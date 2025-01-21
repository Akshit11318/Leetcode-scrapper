## Long Pressed Name
**Problem Link:** https://leetcode.com/problems/long-pressed-name/description

**Problem Statement:**
- Input format and constraints: Given two strings `name` and `typed`, determine if `typed` is a long pressed version of `name`.
- Expected output format: Return `true` if `typed` is a long pressed version of `name`, otherwise return `false`.
- Key requirements and edge cases to consider:
  - A character in `name` can be long pressed if it is followed by the same character in `typed`.
  - A character in `name` can be long pressed if the same character appears in `typed` but is not followed by another instance of the same character in `typed`.
  - If the current character in `typed` does not match the current character in `name`, the function should return `false`.
- Example test cases with explanations:
  - `name = "alex", typed = "aaleex"`: Returns `true` because all 'a' characters in `name` can be long pressed to form `typed`.
  - `name = "saeed", typed = "ssaaedd"`: Returns `false` because the first 's' in `name` cannot be long pressed to form two 's' characters in `typed`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use two nested loops to compare each character in `name` with each character in `typed`.
- Step-by-step breakdown of the solution:
  1. Initialize two pointers, `i` and `j`, to the start of `name` and `typed`, respectively.
  2. Compare the characters at `name[i]` and `typed[j]`.
  3. If the characters match, increment `i` and `j`.
  4. If the characters do not match, check if the character at `typed[j]` is the same as the character at `typed[j-1]`.
  5. If they are the same, increment `j`.
  6. If they are not the same, return `false`.
- Why this approach comes to mind first: It is a straightforward approach that checks each character in `name` against each character in `typed`.

```cpp
bool isLongPressedName(string name, string typed) {
    int i = 0, j = 0;
    while (j < typed.size()) {
        if (i < name.size() && name[i] == typed[j]) {
            i++;
            j++;
        } else if (j > 0 && typed[j] == typed[j-1]) {
            j++;
        } else {
            return false;
        }
    }
    return i == name.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of `name` and `typed`, respectively. This is because we are using a single pass through both strings.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the pointers.
> - **Why these complexities occur:** The time complexity is linear because we are only iterating through each string once, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use two pointers to compare the characters in `name` and `typed`, and we only need to increment the pointer in `name` when the characters match.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `i` and `j`, to the start of `name` and `typed`, respectively.
  2. Compare the characters at `name[i]` and `typed[j]`.
  3. If the characters match, increment `i` and `j`.
  4. If the characters do not match, check if the character at `typed[j]` is the same as the character at `typed[j-1]`.
  5. If they are the same, increment `j`.
  6. If they are not the same, return `false`.
- Proof of optimality: This approach is optimal because it only requires a single pass through both strings, and it uses a constant amount of space.
- Why further optimization is impossible: We must check each character in `name` and `typed` at least once, so we cannot improve the time complexity beyond $O(n + m)$.

```cpp
bool isLongPressedName(string name, string typed) {
    int i = 0, j = 0;
    while (j < typed.size()) {
        if (i < name.size() && name[i] == typed[j]) {
            i++;
            j++;
        } else if (j > 0 && typed[j] == typed[j-1]) {
            j++;
        } else {
            return false;
        }
    }
    return i == name.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of `name` and `typed`, respectively. This is because we are using a single pass through both strings.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the pointers.
> - **Optimality proof:** The time complexity is optimal because we must check each character in `name` and `typed` at least once, and the space complexity is optimal because we are not using any data structures that scale with the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, string comparison.
- Problem-solving patterns identified: Using two pointers to compare characters in two strings.
- Optimization techniques learned: Using a single pass through both strings, using a constant amount of space.
- Similar problems to practice: Other string comparison problems, such as checking if a string is a substring of another string.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as when `name` or `typed` is empty.
- Edge cases to watch for: When `name` or `typed` is empty, when `name` and `typed` have different lengths.
- Performance pitfalls: Using nested loops to compare characters in `name` and `typed`.
- Testing considerations: Testing with different inputs, such as when `name` and `typed` are the same, when `name` and `typed` have different lengths.