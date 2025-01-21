## String to Integer (atoi)
**Problem Link:** https://leetcode.com/problems/string-to-integer-atoi/description

**Problem Statement:**
- Input format: a string `s` containing a potential integer.
- Constraints: `0 <= s.length <= 200`.
- Expected output format: the integer value of `s`, or `0` if `s` cannot be converted.
- Key requirements: handle whitespace, signs, and non-numeric characters.
- Edge cases: empty string, leading whitespace, overflow.

Example test cases:
- `"42"` returns `42`
- `"   -42"` returns `-42`
- `"4193 with words"` returns `4193`
- `"words and 987"` returns `0`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: iterate over the string, checking each character to determine if it's part of a valid integer.
- Step-by-step breakdown:
  1. Remove leading whitespace.
  2. Determine the sign of the integer (if any).
  3. Iterate over the remaining characters, appending digits to a result string.
  4. Convert the result string to an integer and apply the sign.
- Why this approach comes to mind first: it directly addresses the problem statement and handles edge cases in a straightforward manner.

```cpp
int myAtoi(string s) {
    int sign = 1; // default to positive
    long long result = 0; // use long long to handle overflow
    int index = 0;

    // Remove leading whitespace
    while (index < s.length() && s[index] == ' ') {
        index++;
    }

    // Determine sign
    if (index < s.length() && (s[index] == '-' || s[index] == '+')) {
        if (s[index] == '-') {
            sign = -1;
        }
        index++;
    }

    // Iterate over remaining characters
    while (index < s.length() && isdigit(s[index])) {
        result = result * 10 + (s[index++] - '0');
        // Check for overflow
        if (result > INT_MAX && sign == 1) {
            return INT_MAX;
        } else if (result > INT_MAX && sign == -1) {
            return INT_MIN;
        }
    }

    return sign * result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we potentially iterate over the entire string.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store our variables.
> - **Why these complexities occur:** the iteration over the string to process each character leads to the linear time complexity, while the constant space usage is due to not creating any data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: the same approach as the brute force is optimal because we must examine each character at least once to determine if it contributes to a valid integer.
- Detailed breakdown: identical to the brute force approach, as it already achieves the minimum necessary complexity.
- Proof of optimality: any algorithm must read the input at least once, leading to a minimum time complexity of $O(n)$.
- Why further optimization is impossible: without additional information about the input, we cannot avoid examining each character.

```cpp
int myAtoi(string s) {
    int sign = 1;
    long long result = 0;
    int index = 0;

    while (index < s.length() && s[index] == ' ') {
        index++;
    }

    if (index < s.length() && (s[index] == '-' || s[index] == '+')) {
        if (s[index] == '-') {
            sign = -1;
        }
        index++;
    }

    while (index < s.length() && isdigit(s[index])) {
        result = result * 10 + (s[index++] - '0');
        if (result > INT_MAX && sign == 1) {
            return INT_MAX;
        } else if (result > INT_MAX && sign == -1) {
            return INT_MIN;
        }
    }

    return sign * result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space.
> - **Optimality proof:** the algorithm must examine each character at least once, making $O(n)$ the best possible time complexity.

---

### Final Notes

**Learning Points:**
- Handling edge cases such as whitespace, signs, and non-numeric characters is crucial.
- Using `long long` to detect overflow before converting to `int` is a good practice.
- Understanding the minimum necessary complexity for a problem helps in recognizing when an algorithm is optimal.

**Mistakes to Avoid:**
- Not checking for overflow before converting a `long long` to an `int`.
- Not handling leading whitespace correctly.
- Not considering the impact of signs on the final result.

By following these steps and considering the key insights and learning points, you can effectively solve the String to Integer (atoi) problem and similar problems involving string processing and integer conversion.