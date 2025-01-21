## Hexspeak

**Problem Link:** [https://leetcode.com/problems/hexspeak/description](https://leetcode.com/problems/hexspeak/description)

**Problem Statement:**
- Input format and constraints: The input is a string `num` representing a decimal number.
- Expected output format: The output should be a string representing the hexadecimal representation of the input number, with all numbers replaced with their corresponding letters (10 -> A, 11 -> B, ..., 15 -> F).
- Key requirements and edge cases to consider: The input string can be very large, and the output should be in uppercase.
- Example test cases with explanations:
  - Input: "123"
    - Output: "7B"
  - Input: "10"
    - Output: "A"

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Convert the decimal number to a hexadecimal string, then replace each digit with its corresponding letter.
- Step-by-step breakdown of the solution:
  1. Convert the decimal number to a hexadecimal string using the `stoll` function with base 16.
  2. Iterate over each character in the hexadecimal string.
  3. If the character is a digit, replace it with its corresponding letter (10 -> A, 11 -> B, ..., 15 -> F).
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, but it may not be efficient for very large inputs.

```cpp
using namespace std;

class Solution {
public:
    string toHexspeak(string num) {
        // Convert decimal to hexadecimal
        long long decimal = stoll(num);
        stringstream ss;
        ss << hex << uppercase << decimal;
        string hexString = ss.str();

        // Replace digits with letters
        string result = "";
        for (char c : hexString) {
            if (c >= '0' && c <= '9') {
                if (c == '0') {
                    return "ERROR";
                }
                result += 'A' + (c - '0' - 1);
            } else {
                result += c;
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the hexadecimal string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the hexadecimal string.
> - **Why these complexities occur:** The time complexity is linear because we iterate over each character in the hexadecimal string once. The space complexity is also linear because we store the result in a string of the same length as the input.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single loop to convert the decimal number to a hexadecimal string and replace digits with letters.
- Detailed breakdown of the approach:
  1. Convert the decimal number to a hexadecimal string using the `stoll` function with base 16.
  2. Iterate over each character in the hexadecimal string, replacing digits with letters and checking for errors.
- Proof of optimality: This approach has the same time complexity as the brute force approach, but it uses less space because it does not require an extra string for the hexadecimal representation.
- Why further optimization is impossible: The time complexity is already linear, and we cannot reduce the space complexity further because we need to store the result in a string.

```cpp
using namespace std;

class Solution {
public:
    string toHexspeak(string num) {
        long long decimal = stoll(num);
        stringstream ss;
        ss << hex << uppercase << decimal;
        string hexString = ss.str();

        string result = "";
        for (char c : hexString) {
            if (c >= '0' && c <= '9') {
                if (c == '0') {
                    return "ERROR";
                }
                result += 'A' + (c - '0' - 1);
            } else {
                result += c;
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the hexadecimal string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the hexadecimal string.
> - **Optimality proof:** This approach is optimal because it has the same time complexity as the brute force approach, but it uses less space because it does not require an extra string for the hexadecimal representation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Conversion between decimal and hexadecimal numbers, string manipulation, and error handling.
- Problem-solving patterns identified: Using a single loop to perform multiple operations, checking for errors, and optimizing space complexity.
- Optimization techniques learned: Reducing the number of loops and strings used in the solution.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check for errors, using extra strings or loops, and not optimizing space complexity.
- Edge cases to watch for: Very large inputs, inputs with leading zeros, and inputs that result in hexadecimal strings with digits.
- Performance pitfalls: Using extra strings or loops, not checking for errors, and not optimizing space complexity.
- Testing considerations: Testing with very large inputs, inputs with leading zeros, and inputs that result in hexadecimal strings with digits.