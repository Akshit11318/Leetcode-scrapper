## Confusing Number
**Problem Link:** https://leetcode.com/problems/confusing-number/description

**Problem Statement:**
- Input: An integer `N`.
- Constraints: $1 \leq N \leq 10^9$.
- Expected Output: `true` if `N` is a confusing number, `false` otherwise.
- Key Requirements:
  - A confusing number is a number where when its digits are rotated by 180 degrees, it becomes a different number.
- Edge Cases:
  - Numbers with 6 and 9 are the only pairs of digits that can be confused with each other when rotated by 180 degrees.
  - Numbers with any other digit (0-5, 7, 8) cannot be confused with another digit when rotated.

**Example Test Cases:**
- Input: `6`, Output: `true` (because `6` becomes `9` when rotated).
- Input: `89`, Output: `true` (because `89` becomes `68` when rotated).
- Input: `11`, Output: `false` (because `11` remains `11` when rotated).

---

### Brute Force Approach
**Explanation:**
- Convert the integer into a string to easily access each digit.
- Check each digit to see if it can be confused with another digit when rotated.
- If any digit cannot be confused with another digit, return `false`.
- If all digits can be confused with another digit and the resulting number is different, return `true`.

```cpp
class Solution {
public:
    bool confusingNumber(int N) {
        string str = to_string(N);
        string rotated = "";
        for (char c : str) {
            if (c == '6') rotated += '9';
            else if (c == '9') rotated += '6';
            else if (c == '0' || c == '1' || c == '8') rotated += c;
            else return false; // If digit cannot be confused, return false
        }
        // Check if rotated number is different from original
        return rotated != str;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of digits in `N`, because we iterate over each digit once.
> - **Space Complexity:** $O(n)$, because we create a new string of the same length as the input string.
> - **Why these complexities occur:** The iteration over each digit and the creation of a new string for the rotated number cause these complexities.

---

### Optimal Approach (Required)
The provided brute force approach is already optimal because it checks each digit exactly once and uses a constant amount of extra space per digit (for the rotated string). However, we can slightly optimize the code for clarity and efficiency by directly returning as soon as we find a digit that cannot be confused or as soon as we determine the number is confusing.

```cpp
class Solution {
public:
    bool confusingNumber(int N) {
        string str = to_string(N);
        string rotated = "";
        for (char c : str) {
            if (c == '6') rotated += '9';
            else if (c == '9') rotated += '6';
            else if (c == '0' || c == '1' || c == '8') rotated += c;
            else return false; // Digit cannot be confused
        }
        return rotated != str; // Check if rotated is different
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of digits in `N`.
> - **Space Complexity:** $O(n)$, for the rotated string.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input number's digits and uses space proportional to the input size.

---

### Final Notes

**Learning Points:**
- The importance of understanding the properties of digits when rotated (e.g., 6 and 9 are the only digits that can be confused with another digit).
- How to convert an integer to a string in C++ for easier manipulation of digits.
- The concept of iterating over each character in a string and performing operations based on its value.

**Mistakes to Avoid:**
- Not checking for all possible confusing digits (6, 9, 0, 1, 8).
- Not correctly implementing the rotation logic for each digit.
- Not comparing the rotated number with the original to determine if it's confusing.