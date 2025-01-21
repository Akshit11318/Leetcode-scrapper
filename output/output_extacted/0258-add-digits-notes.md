## Add Digits

**Problem Link:** https://leetcode.com/problems/add-digits/description

**Problem Statement:**
- Input format: An integer `num`.
- Constraints: `0 <= num <= 2^31 - 1`.
- Expected output format: A single integer representing the result of adding digits of `num` until a single digit is obtained.
- Key requirements and edge cases to consider: The input can be any integer within the given range, and the output should be a single digit. For example, if `num = 38`, the output should be `2` because `3 + 8 = 11`, and `1 + 1 = 2`.
- Example test cases with explanations:
  - `num = 38` returns `2` because `3 + 8 = 11`, and `1 + 1 = 2`.
  - `num = 0` returns `0` because there are no digits to add.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can repeatedly add the digits of the number until a single digit is obtained.
- Step-by-step breakdown of the solution:
  1. Convert the number into a string to easily access each digit.
  2. Initialize a variable to store the sum of the digits.
  3. Iterate over the string, convert each character back to an integer, and add it to the sum.
  4. If the sum is greater than 9, repeat the process with the new sum until a single digit is obtained.
- Why this approach comes to mind first: It's a straightforward, intuitive way to solve the problem by directly following the problem statement's instructions.

```cpp
class Solution {
public:
    int addDigits(int num) {
        while (num > 9) {
            int sum = 0;
            while (num > 0) {
                sum += num % 10;
                num /= 10;
            }
            num = sum;
        }
        return num;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the input number. This is because in the worst case, we are reducing the number of digits by one in each iteration. The number of digits in a number $n$ is $\log_{10}n$, hence the time complexity.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the sum and the number.
> - **Why these complexities occur:** The time complexity occurs because we are iteratively reducing the size of the input (the number of digits), and the space complexity is constant because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using the concept of digital root, where the digital root of a number is the recursive sum of all its digits until we get a single-digit number. However, there's a mathematical shortcut to find the digital root of a number without iteration: if the number is 0, its digital root is 0; otherwise, the digital root is the remainder when the number is divided by 9, unless the remainder is 0, in which case the digital root is 9.
- Detailed breakdown of the approach:
  1. If the number is 0, return 0.
  2. Otherwise, calculate the remainder of the number divided by 9.
  3. If the remainder is 0, return 9; otherwise, return the remainder.
- Proof of optimality: This approach is optimal because it directly calculates the digital root without any iteration, resulting in a constant time complexity.

```cpp
class Solution {
public:
    int addDigits(int num) {
        if (num == 0) return 0;
        return (num % 9 == 0) ? 9 : num % 9;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we are performing a constant number of operations regardless of the input size.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space.
> - **Optimality proof:** This approach is optimal because it achieves the digital root in constant time, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Digital root, iterative sum of digits, and mathematical optimization.
- Problem-solving patterns identified: Looking for mathematical shortcuts to avoid iteration.
- Optimization techniques learned: Using mathematical properties to simplify calculations.
- Similar problems to practice: Other problems involving digital roots or iterative calculations.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where the input number is 0, or not correctly calculating the remainder.
- Edge cases to watch for: The number 0, and numbers that are multiples of 9.
- Performance pitfalls: Using iteration when a mathematical shortcut is available.
- Testing considerations: Ensure to test with a variety of inputs, including 0, single-digit numbers, and large numbers.