## Remove 9
**Problem Link:** https://leetcode.com/problems/remove-9/description

**Problem Statement:**
- Input format and constraints: The input is an integer `x`.
- Expected output format: The output should be an integer after removing all occurrences of digit 9 from the number.
- Key requirements and edge cases to consider: The number can be negative or positive, and it can contain multiple occurrences of the digit 9.
- Example test cases with explanations: For example, if the input is 199, the output should be 19 because we remove the 9 from the number.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to convert the integer into a string, iterate over each character, and remove all occurrences of the character '9'. Then, we convert the resulting string back into an integer.
- Step-by-step breakdown of the solution:
  1. Convert the integer into a string.
  2. Initialize an empty string to store the result.
  3. Iterate over each character in the string. If the character is not '9', append it to the result string.
  4. Convert the result string back into an integer.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. It involves basic string manipulation and conversion between data types.

```cpp
class Solution {
public:
    int newInteger(int x) {
        string str = to_string(x);
        string result = "";
        for (char c : str) {
            if (c != '9') {
                result += c;
            }
        }
        if (result.empty()) {
            return 0;
        }
        return stoi(result);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of digits in the input integer. This is because we iterate over each character in the string representation of the integer.
> - **Space Complexity:** $O(n)$, where $n$ is the number of digits in the input integer. This is because we create a new string to store the result.
> - **Why these complexities occur:** The time complexity is $O(n)$ because we iterate over each character in the string. The space complexity is $O(n)$ because we create a new string to store the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating over each character in the string, we can use a mathematical approach to remove all occurrences of the digit 9 from the number. We can do this by using the fact that the number 10 is equivalent to the number 1 followed by a 0, and the number 100 is equivalent to the number 1 followed by two 0s, and so on.
- Detailed breakdown of the approach:
  1. Initialize a variable `result` to 0.
  2. Initialize a variable `base` to 1.
  3. Iterate over each digit in the input integer from right to left. If the digit is not 9, add the digit multiplied by the base to the result and multiply the base by 10.
- Proof of optimality: This approach is optimal because it avoids the overhead of string conversion and iteration.
- Why further optimization is impossible: This approach is already optimal because it uses a mathematical approach to remove all occurrences of the digit 9 from the number, which is more efficient than iterating over each character in the string.

```cpp
class Solution {
public:
    int newInteger(int x) {
        int result = 0;
        int base = 1;
        while (x) {
            int digit = x % 10;
            if (digit != 9) {
                result += digit * base;
            }
            x /= 10;
            if (digit != 9) {
                base *= 10;
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log x)$, where $x$ is the input integer. This is because we iterate over each digit in the input integer.
> - **Space Complexity:** $O(1)$, where $x$ is the input integer. This is because we use a constant amount of space to store the result and the base.
> - **Optimality proof:** The time complexity is $O(\log x)$ because we iterate over each digit in the input integer. The space complexity is $O(1)$ because we use a constant amount of space to store the result and the base.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Mathematical approach to remove all occurrences of the digit 9 from the number.
- Problem-solving patterns identified: Using a mathematical approach to solve a problem instead of iterating over each character in the string.
- Optimization techniques learned: Avoiding the overhead of string conversion and iteration.
- Similar problems to practice: Problems that involve removing all occurrences of a certain digit or character from a number or string.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the case where the input integer is 0.
- Edge cases to watch for: The case where the input integer is negative or positive.
- Performance pitfalls: Using a string-based approach instead of a mathematical approach.
- Testing considerations: Testing the function with different input integers, including negative and positive numbers, and numbers with multiple occurrences of the digit 9.