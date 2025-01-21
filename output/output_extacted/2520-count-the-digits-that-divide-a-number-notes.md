## Count the Digits That Divide a Number

**Problem Link:** https://leetcode.com/problems/count-the-digits-that-divide-a-number/description

**Problem Statement:**
- Input format: An integer `number`.
- Constraints: $1 \leq number \leq 10^9$.
- Expected output format: The count of digits that divide the number without leaving a remainder.
- Key requirements: Each digit of the number should be considered individually, and a digit is considered valid if it is non-zero and divides the number without a remainder.
- Example test cases:
  - Input: `number = 1012`
    - Explanation: The digits 1, 0, 1, and 2 are considered. However, 0 does not divide any number, so it's excluded. Both 1 and 2 divide 1012 without a remainder.
  - Input: `number = 1000`
    - Explanation: Only the digit 1 divides 1000 without a remainder.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking each digit of the number to see if it divides the number without a remainder.
- Step-by-step breakdown:
  1. Convert the number into a string to easily iterate through each digit.
  2. For each digit, convert it back to an integer and check if it is non-zero (since 0 cannot divide any number).
  3. If the digit is non-zero, check if the number is divisible by this digit without a remainder.
  4. Count the digits that satisfy this condition.

```cpp
int countDigits(int number) {
    int count = 0;
    string numStr = to_string(number);
    for (char c : numStr) {
        int digit = c - '0'; // Convert char to int
        if (digit != 0 && number % digit == 0) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of digits in the number. This is because we are iterating through each digit once.
> - **Space Complexity:** $O(n)$, for converting the number to a string. This is necessary for easy iteration through each digit.
> - **Why these complexities occur:** The iteration through each digit and the conversion to a string cause these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is the same as in the brute force approach since checking each digit is necessary.
- However, the optimal approach is essentially the same as the brute force in terms of algorithmic complexity because we must check each digit. The optimization lies in recognizing that the brute force approach is already optimal in terms of time complexity for this specific problem.
- Proof of optimality: Since we must check each digit at least once to determine if it divides the number without a remainder, the minimum time complexity is $O(n)$, where $n$ is the number of digits.

```cpp
int countDigits(int number) {
    int count = 0;
    string numStr = to_string(number);
    for (char c : numStr) {
        int digit = c - '0'; // Convert char to int
        if (digit != 0 && number % digit == 0) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of digits in the number.
> - **Space Complexity:** $O(n)$, for converting the number to a string.
> - **Optimality proof:** The necessity to check each digit ensures that $O(n)$ is the optimal time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept: Iteration through each digit of a number and checking divisibility.
- Problem-solving pattern: Converting numbers to strings for easier digit manipulation.
- Optimization technique: Recognizing when a brute force approach is already optimal due to the inherent requirements of the problem.

**Mistakes to Avoid:**
- Forgetting to check for non-zero digits before divisibility checks.
- Not considering the conversion of numbers to strings for digit iteration.
- Overcomplicating the problem with unnecessary optimizations.