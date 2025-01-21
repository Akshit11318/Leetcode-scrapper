## Reverse Integer
**Problem Link:** https://leetcode.com/problems/reverse-integer/description

**Problem Statement:**
- Input format and constraints: The input is a 32-bit signed integer.
- Expected output format: The output should be the reversed integer.
- Key requirements and edge cases to consider: The reversed integer should be within the range of a 32-bit signed integer. If the reversed integer is outside this range, return 0.
- Example test cases with explanations:
  - Example 1: Input: `123`, Output: `321`
  - Example 2: Input: `-123`, Output: `-321`
  - Example 3: Input: `120`, Output: `21`
  - Example 4: Input: `1534236469`, Output: `0` (because the reversed integer is outside the range of a 32-bit signed integer)

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The first approach that comes to mind is to convert the integer into a string, reverse the string, and then convert it back to an integer.
- Step-by-step breakdown of the solution:
  1. Convert the integer to a string.
  2. Reverse the string.
  3. Convert the reversed string back to an integer.
  4. Check if the reversed integer is within the range of a 32-bit signed integer.
- Why this approach comes to mind first: This approach is straightforward and easy to implement.

```cpp
class Solution {
public:
    int reverse(int x) {
        // Convert integer to string
        string str = to_string(x);
        
        // Check if the number is negative
        bool isNegative = false;
        if (str[0] == '-') {
            isNegative = true;
            str = str.substr(1);
        }
        
        // Reverse the string
        reverse(str.begin(), str.end());
        
        // Convert string back to integer
        long long result = stoll(str);
        
        // Apply negative sign if necessary
        if (isNegative) {
            result = -result;
        }
        
        // Check if the result is within the range of a 32-bit signed integer
        if (result < INT_MIN || result > INT_MAX) {
            return 0;
        }
        
        return (int)result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log|x|)$, where $|x|$ is the absolute value of the input integer. This is because the number of digits in the integer is proportional to the logarithm of its absolute value.
> - **Space Complexity:** $O(log|x|)$, where $|x|$ is the absolute value of the input integer. This is because we are converting the integer to a string, and the length of the string is proportional to the number of digits in the integer.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over each digit in the integer to reverse it. The space complexity occurs because we are storing the reversed integer as a string.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can reverse the integer without converting it to a string by using arithmetic operations to extract and append digits.
- Detailed breakdown of the approach:
  1. Initialize a variable to store the reversed integer.
  2. While the input integer is non-zero, extract the last digit by taking the remainder when divided by 10.
  3. Append the extracted digit to the reversed integer by shifting its digits to the left (multiplying by 10) and adding the extracted digit.
  4. Remove the last digit from the input integer by performing integer division by 10.
  5. Check if the reversed integer is within the range of a 32-bit signed integer.
- Proof of optimality: This approach is optimal because it only requires a constant amount of space and has a time complexity proportional to the number of digits in the input integer.

```cpp
class Solution {
public:
    int reverse(int x) {
        long long result = 0;
        while (x != 0) {
            int digit = x % 10;
            x /= 10;
            result = result * 10 + digit;
            if (result > INT_MAX || result < INT_MIN) {
                return 0;
            }
        }
        return (int)result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log|x|)$, where $|x|$ is the absolute value of the input integer.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the reversed integer and the input integer.
> - **Optimality proof:** This approach is optimal because it has a time complexity proportional to the number of digits in the input integer and uses a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Arithmetic operations, digit extraction, and integer reversal.
- Problem-solving patterns identified: Using arithmetic operations to manipulate integers and checking for overflow.
- Optimization techniques learned: Avoiding unnecessary conversions to strings and using constant space.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for overflow when reversing the integer.
- Edge cases to watch for: Negative integers and integers with a large number of digits.
- Performance pitfalls: Converting integers to strings unnecessarily.
- Testing considerations: Test with a variety of input integers, including negative integers and integers with a large number of digits.