## Thousand Separator
**Problem Link:** https://leetcode.com/problems/thousand-separator/description

**Problem Statement:**
- Input: An integer `n`.
- Constraints: `0 <= n < 2^31`.
- Expected output: A string representing the input integer with commas as thousand separators.
- Key requirements: Handle edge cases such as `n = 0` and large integers.
- Example test cases:
  - Input: `n = 123456789`
  - Output: `"123,456,789"`
  - Explanation: Insert commas as thousand separators.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Convert the integer to a string, then iterate over the string from right to left, inserting commas every three characters.
- Step-by-step breakdown:
  1. Convert the integer to a string.
  2. Initialize an empty string `result`.
  3. Iterate over the string from right to left.
  4. For every three characters, insert a comma before them in the `result` string.
- Why this approach comes to mind first: It directly addresses the problem statement and is straightforward to implement.

```cpp
class Solution {
public:
    string thousandSeparator(int n) {
        string str = to_string(n);
        string result = "";
        int count = 0;
        for (int i = str.size() - 1; i >= 0; i--) {
            result = str[i] + result;
            count++;
            if (count == 3 && i != 0) {
                result = "," + result;
                count = 0;
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the input integer, because we iterate over the string representation of the integer.
> - **Space Complexity:** $O(\log n)$, because we create a new string to store the result.
> - **Why these complexities occur:** The number of digits in the integer $n$ is proportional to $\log n$, so both the time and space complexities depend on the number of digits.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The brute force approach is already quite efficient and straightforward. However, we can slightly optimize the code by using a more efficient way to build the string.
- Detailed breakdown:
  1. Convert the integer to a string.
  2. Use a `StringBuilder` or equivalent to efficiently build the result string.
  3. Iterate over the string from right to left, inserting commas as needed.
- Proof of optimality: This approach has the same time complexity as the brute force approach but is slightly more efficient in practice due to the use of a `StringBuilder`.

```cpp
class Solution {
public:
    string thousandSeparator(int n) {
        string str = to_string(n);
        string result = "";
        for (int i = 0; i < str.size(); i++) {
            result += str[i];
            if ((str.size() - i) % 3 == 1 && i != str.size() - 1) {
                result += ",";
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the input integer.
> - **Space Complexity:** $O(\log n)$, because we create a new string to store the result.
> - **Optimality proof:** This approach has the same time complexity as the brute force approach but is slightly more efficient in practice due to the simplified code.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: String manipulation, iteration, and conditional statements.
- Problem-solving patterns: Converting integers to strings and iterating over the characters.
- Optimization techniques: Using a `StringBuilder` or equivalent to efficiently build strings.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as `n = 0`.
- Edge cases to watch for: Large integers and negative integers (although the problem statement specifies non-negative integers).
- Performance pitfalls: Using inefficient string concatenation methods.
- Testing considerations: Test with various input values, including edge cases.