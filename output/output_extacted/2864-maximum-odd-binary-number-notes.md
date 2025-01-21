## Maximum Odd Binary Number
**Problem Link:** https://leetcode.com/problems/maximum-odd-binary-number/description

**Problem Statement:**
- Input: A binary string `s`.
- Output: The maximum odd binary number that can be obtained by changing at most one digit in `s`.
- Key requirements: The resulting binary number must be odd, and at most one digit can be changed.
- Edge cases: If the input string is empty or contains non-binary digits, the function should handle these cases accordingly.

**Example Test Cases:**
- Input: `s = "1101"`
  Output: `"1111"`
  Explanation: Changing the first digit from `1` to `1` (no change) results in the maximum odd binary number `"1111"`.
- Input: `s = "10"`
  Output: `"11"`
  Explanation: Changing the second digit from `0` to `1` results in the maximum odd binary number `"11"`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves generating all possible binary numbers by changing at most one digit in the input string `s`.
- Then, we check each generated number to see if it is odd and keep track of the maximum odd number found.

```cpp
class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int n = s.size();
        string maxOdd = "";
        for (int i = 0; i < n; i++) {
            string temp = s;
            // Try changing the current digit to '1'
            temp[i] = '1';
            if (isValidOddBinary(temp)) {
                if (maxOdd.empty() || compareBinary(temp, maxOdd)) {
                    maxOdd = temp;
                }
            }
            // Try changing the current digit to '0'
            temp[i] = '0';
            if (isValidOddBinary(temp)) {
                if (maxOdd.empty() || compareBinary(temp, maxOdd)) {
                    maxOdd = temp;
                }
            }
        }
        return maxOdd;
    }

    bool isValidOddBinary(string s) {
        // Check if the binary number is odd (i.e., the last digit is '1')
        return s.back() == '1';
    }

    bool compareBinary(string s1, string s2) {
        // Compare two binary numbers
        return s1 > s2;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot n)$, where $n$ is the length of the input string `s`. This is because we iterate over the string and generate a new string for each digit.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string `s`. This is because we create a temporary string for each digit.
> - **Why these complexities occur:** The brute force approach generates all possible binary numbers by changing at most one digit, resulting in a time complexity of $O(n \cdot n)$. The space complexity is $O(n)$ due to the creation of temporary strings.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is that we only need to change the last digit to '1' if it is not already '1', and then try changing each digit to '1' or '0' to see if it results in a larger odd binary number.
- We can start from the most significant digit and work our way down, keeping track of the maximum odd binary number found.

```cpp
class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int n = s.size();
        if (s.back() == '1') {
            // If the last digit is already '1', try changing each digit to '1' or '0'
            for (int i = 0; i < n - 1; i++) {
                if (s[i] == '0') {
                    return s.substr(0, i) + "1" + s.substr(i + 1);
                }
            }
            return s;
        } else {
            // If the last digit is '0', change it to '1' and return the result
            return s.substr(0, n - 1) + "1";
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string `s`. This is because we only need to iterate over the string once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string `s`. This is because we create a new string by changing one digit.
> - **Optimality proof:** This approach is optimal because we only need to change at most one digit to obtain the maximum odd binary number, and we do this in a single pass over the input string.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: iteration, string manipulation, and comparison.
- Problem-solving patterns identified: starting with a brute force approach and optimizing it.
- Optimization techniques learned: reducing the number of iterations and avoiding unnecessary string creations.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, such as an empty input string or a string with non-binary digits.
- Performance pitfalls: using inefficient algorithms or data structures, such as generating all possible binary numbers.
- Testing considerations: testing the function with different input strings, including edge cases.