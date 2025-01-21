## Palindrome Number

**Problem Link:** https://leetcode.com/problems/palindrome-number/description

**Problem Statement:**
- Input format and constraints: The input is an integer `x` which can be any 32-bit signed integer.
- Expected output format: The output is a boolean value indicating whether the input integer is a palindrome or not.
- Key requirements and edge cases to consider: The function should handle negative numbers, single-digit numbers, and multi-digit numbers.
- Example test cases with explanations:
  - Input: `121`, Output: `true`
  - Input: `-121`, Output: `false`
  - Input: `10`, Output: `false`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach to solving this problem involves converting the integer into a string and then checking if the string is a palindrome.
- Step-by-step breakdown of the solution:
  1. Convert the integer into a string.
  2. Initialize two pointers at the start and end of the string.
  3. Compare the characters at the two pointers. If they are different, return `false`.
  4. Move the pointers towards the center of the string.
  5. If all pairs of characters match, return `true`.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, making it a natural first choice.

```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        // Convert integer to string
        string str = to_string(x);
        
        // Initialize two pointers
        int left = 0;
        int right = str.length() - 1;
        
        // Compare characters from both ends
        while (left < right) {
            if (str[left] != str[right]) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of digits in the integer. This is because we are converting the integer into a string and then iterating over the string.
> - **Space Complexity:** $O(n)$, as we are storing the string representation of the integer.
> - **Why these complexities occur:** The time complexity is linear because we are iterating over the string once. The space complexity is also linear because we are storing the entire string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of converting the integer into a string, we can directly reverse the integer and compare it with the original number.
- Detailed breakdown of the approach:
  1. If the number is negative, return `false` because negative numbers cannot be palindromes.
  2. Initialize a variable `reversed` to 0.
  3. While the input number `x` is greater than 0, extract the last digit of `x` by taking `x % 10`, and append it to `reversed` by multiplying `reversed` by 10 and adding the extracted digit.
  4. Remove the last digit from `x` by performing integer division `x / 10`.
  5. Once all digits have been processed, compare the original number with the reversed number.
- Proof of optimality: This approach is optimal because it only requires a constant amount of space and has a linear time complexity.

```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        // Negative numbers cannot be palindromes
        if (x < 0) return false;
        
        // Initialize variables
        int original = x;
        int reversed = 0;
        
        // Reverse the number
        while (x > 0) {
            reversed = reversed * 10 + x % 10;
            x /= 10;
        }
        
        // Compare original and reversed numbers
        return original == reversed;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the input number. This is because we are processing each digit of the number once.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity with respect to the number of digits in the input number and uses a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Reversing a number, comparing numbers, and handling edge cases.
- Problem-solving patterns identified: Directly manipulating numbers instead of converting them to strings.
- Optimization techniques learned: Avoiding unnecessary conversions and using mathematical operations to reverse numbers.
- Similar problems to practice: Other problems involving number manipulation and comparison.

**Mistakes to Avoid:**
- Common implementation errors: Not handling negative numbers correctly, not checking for integer overflow.
- Edge cases to watch for: Negative numbers, single-digit numbers, and numbers with leading zeros.
- Performance pitfalls: Using inefficient algorithms or data structures.
- Testing considerations: Thoroughly testing the function with different inputs, including edge cases.