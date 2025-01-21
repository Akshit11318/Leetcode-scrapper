## Armstrong Number
**Problem Link:** https://leetcode.com/problems/armstrong-number/description

**Problem Statement:**
- Input format and constraints: The input is a single integer `N`. The constraints are that `N` is a non-negative integer.
- Expected output format: The output should be a boolean value indicating whether `N` is an Armstrong number or not.
- Key requirements and edge cases to consider: An Armstrong number is a number that is equal to the sum of cubes of its digits. For example, 371 is an Armstrong number since 3^3 + 7^3 + 1^3 = 371.
- Example test cases with explanations:
  - Input: `N = 153`, Output: `true` (1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153)
  - Input: `N = 370`, Output: `true` (3^3 + 7^3 + 0^3 = 27 + 343 + 0 = 370)
  - Input: `N = 123`, Output: `false` (1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36, which is not equal to 123)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To determine if a number is an Armstrong number, we need to calculate the sum of cubes of its digits and compare it with the original number.
- Step-by-step breakdown of the solution:
  1. Convert the number to a string to easily access each digit.
  2. Initialize a variable to store the sum of cubes of the digits.
  3. Iterate over each character (digit) in the string, convert it back to an integer, cube it, and add it to the sum.
  4. Compare the sum with the original number to determine if it's an Armstrong number.
- Why this approach comes to mind first: It's a straightforward method that directly implements the definition of an Armstrong number.

```cpp
class Solution {
public:
    bool isArmstrong(int N) {
        string str = to_string(N);
        int sum = 0;
        for (char c : str) {
            int digit = c - '0'; // Convert character to integer
            sum += pow(digit, str.length()); // Cube the digit and add to sum
        }
        return sum == N; // Check if sum equals the original number
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(N))$, where $N$ is the input number. This is because we are iterating over each digit in the number, and the number of digits in a number $N$ is proportional to $log(N)$.
> - **Space Complexity:** $O(log(N))$, because we are converting the number to a string, and the length of the string is proportional to $log(N)$.
> - **Why these complexities occur:** The time complexity is due to the iteration over the digits, and the space complexity is due to the conversion of the number to a string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, but we can optimize the calculation of the power by using the `pow` function with three arguments for integer exponentiation, which is more efficient than the `pow` function with two arguments.
- Detailed breakdown of the approach: We still convert the number to a string, iterate over each character (digit), cube it, and add it to the sum. However, we use a more efficient method for calculating the power.
- Proof of optimality: This approach is optimal because it directly calculates the sum of cubes of the digits without any unnecessary steps or operations.
- Why further optimization is impossible: This approach has a time complexity of $O(log(N))$, which is the minimum required to iterate over each digit in the number.

```cpp
class Solution {
public:
    bool isArmstrong(int N) {
        string str = to_string(N);
        int sum = 0;
        for (char c : str) {
            int digit = c - '0'; // Convert character to integer
            sum += pow(digit, str.length()); // Cube the digit and add to sum
        }
        return sum == N; // Check if sum equals the original number
    }
};
```

However, to avoid using the `pow` function which involves floating point calculations and can be less efficient for integer exponentiation, we can calculate the power manually for the specific case of cubing:

```cpp
class Solution {
public:
    bool isArmstrong(int N) {
        string str = to_string(N);
        int sum = 0;
        for (char c : str) {
            int digit = c - '0'; // Convert character to integer
            sum += digit * digit * digit; // Cube the digit and add to sum
        }
        return sum == N; // Check if sum equals the original number
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(N))$, where $N$ is the input number.
> - **Space Complexity:** $O(log(N))$, because we are converting the number to a string.
> - **Optimality proof:** This approach is optimal because it directly calculates the sum of cubes of the digits without any unnecessary steps or operations, using integer arithmetic for efficiency.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over digits of a number, calculation of powers.
- Problem-solving patterns identified: Direct implementation of the definition of an Armstrong number.
- Optimization techniques learned: Using integer arithmetic for efficiency, avoiding unnecessary function calls.
- Similar problems to practice: Other problems involving properties of numbers, such as checking if a number is a palindrome or a perfect square.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect calculation of the power, incorrect iteration over the digits.
- Edge cases to watch for: Numbers with leading zeros, negative numbers.
- Performance pitfalls: Using inefficient methods for calculating powers, using floating-point arithmetic for integer calculations.
- Testing considerations: Test with a variety of inputs, including edge cases and large numbers.