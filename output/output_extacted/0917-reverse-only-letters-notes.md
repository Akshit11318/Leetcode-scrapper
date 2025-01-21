## Reverse Only Letters

**Problem Link:** https://leetcode.com/problems/reverse-only-letters/description

**Problem Statement:**
- Input: A string `s` containing letters and non-letter characters.
- Constraints: The input string consists of ASCII characters and has a length of at most $10^5$.
- Expected Output: The input string with only the letters reversed.
- Key Requirements:
  - Only letters should be reversed.
  - Non-letter characters should remain in their original positions.
- Edge Cases:
  - Empty string
  - Single character string
  - String with no letters
  - String with only letters
- Example Test Cases:
  - Input: `"ab-cd"` - Output: `"dc-ba"`
  - Input: `"a-bC-ba"` - Output: `"a-bC-ba"`
  - Input: `"a"` - Output: `"a"`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through the string and identifying letters.
- We can use two pointers, one starting from the beginning of the string and one from the end, to reverse the letters.
- This approach comes to mind first because it directly addresses the requirement to reverse letters.

```cpp
string reverseOnlyLetters(string s) {
    int left = 0, right = s.length() - 1;
    while (left < right) {
        if (!isalpha(s[left])) {
            left++;
        } else if (!isalpha(s[right])) {
            right--;
        } else {
            // Swap the characters at the left and right pointers
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }
    return s;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string. This is because in the worst case, we might end up iterating through the entire string.
> - **Space Complexity:** $O(n)$ for the string in the worst case, as strings in C++ can be modified in place, but here we consider the general case where the string might be copied.
> - **Why these complexities occur:** The time complexity is linear because we potentially visit each character once. The space complexity is linear due to the string itself.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is the same as the brute force: using two pointers to traverse the string from both ends towards the center, swapping letters as we go.
- This approach is optimal because it directly addresses the requirement with minimal operations.
- Further optimization is impossible because we must at least read the input string once to identify the letters to be reversed.

```cpp
string reverseOnlyLetters(string s) {
    int left = 0, right = s.length() - 1;
    while (left < right) {
        if (!isalpha(s[left])) {
            left++;
        } else if (!isalpha(s[right])) {
            right--;
        } else {
            swap(s[left], s[right]);
            left++;
            right--;
        }
    }
    return s;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string. This is because we potentially iterate through the entire string once.
> - **Space Complexity:** $O(1)$ if we consider the input string as part of the space complexity, since we are modifying it in place. However, if we count the space required for the pointers and other variables, it's still $O(1)$ because the space does not grow with the size of the input.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input string once. The space complexity is optimal because we only use a constant amount of space to store the pointers and do not allocate any additional space that scales with the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique.
- Problem-solving patterns identified: Reversing parts of a string while leaving other parts unchanged.
- Optimization techniques learned: Minimizing operations by directly addressing the problem's requirements.
- Similar problems to practice: Reversing linked lists, rotating arrays.

**Mistakes to Avoid:**
- Not checking for non-letter characters correctly.
- Not handling edge cases such as empty strings or strings with a single character.
- Not optimizing the solution to minimize unnecessary swaps or iterations.
- Not considering the input validation and error handling.