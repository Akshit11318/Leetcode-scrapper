## Divide Two Integers
**Problem Link:** [https://leetcode.com/problems/divide-two-integers/description](https://leetcode.com/problems/divide-two-integers/description)

**Problem Statement:**
- Input format and constraints: Given two integers `dividend` and `divisor`, find the quotient without using the division operator.
- Expected output format: Return the integer part of the quotient.
- Key requirements and edge cases to consider: 
    - `dividend` and `divisor` are 32-bit signed integers.
    - The quotient should be rounded towards zero.
    - Handle the case where `dividend` is the minimum possible integer value (`-2^31`) and `divisor` is `-1`, which causes an integer overflow.
- Example test cases with explanations:
    - `dividend = 10, divisor = 3` should return `3`.
    - `dividend = 7, divisor = -3` should return `-2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use repeated subtraction to find the quotient.
- Step-by-step breakdown of the solution:
    1. Initialize a variable `quotient` to `0`.
    2. If `dividend` is negative, convert it to positive and set a flag `is_negative` to `true`.
    3. If `divisor` is negative, convert it to positive.
    4. While `dividend` is greater than or equal to `divisor`, subtract `divisor` from `dividend` and increment `quotient`.
    5. If `is_negative` is `true`, make `quotient` negative.
- Why this approach comes to mind first: It is a straightforward and intuitive solution.

```cpp
int divide(int dividend, int divisor) {
    // Handle the case where divisor is 0
    if (divisor == 0) {
        throw runtime_error("Cannot divide by zero");
    }

    // Initialize quotient to 0
    int quotient = 0;

    // Check if dividend is negative
    bool is_negative = (dividend < 0);

    // Convert dividend to positive if necessary
    long long abs_dividend = abs((long long)dividend);

    // Convert divisor to positive
    long long abs_divisor = abs((long long)divisor);

    // Perform repeated subtraction
    while (abs_dividend >= abs_divisor) {
        abs_dividend -= abs_divisor;
        quotient++;
    }

    // If dividend was negative, make quotient negative
    if (is_negative) {
        quotient = -quotient;
    }

    // Check for integer overflow
    if (quotient > INT_MAX || quotient < INT_MIN) {
        throw runtime_error("Integer overflow");
    }

    return quotient;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\frac{dividend}{divisor})$, where `dividend` and `divisor` are the input integers. This occurs because we perform repeated subtraction in the worst case.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the quotient and other variables.
> - **Why these complexities occur:** The time complexity is due to the repeated subtraction operation, while the space complexity is constant because we only use a fixed amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use bit manipulation to find the quotient.
- Detailed breakdown of the approach:
    1. Initialize a variable `quotient` to `0`.
    2. If `dividend` is negative, convert it to positive and set a flag `is_negative` to `true`.
    3. If `divisor` is negative, convert it to positive.
    4. Use bit manipulation to find the largest power of 2 that can be subtracted from `dividend` without making it negative.
    5. Subtract the largest power of 2 from `dividend` and add the corresponding value to `quotient`.
    6. Repeat steps 4-5 until `dividend` is less than `divisor`.
- Proof of optimality: This approach has a time complexity of $O(log\ dividend)$, which is optimal because we are using bit manipulation to find the largest power of 2 that can be subtracted from `dividend`.

```cpp
int divide(int dividend, int divisor) {
    // Handle the case where divisor is 0
    if (divisor == 0) {
        throw runtime_error("Cannot divide by zero");
    }

    // Initialize quotient to 0
    int quotient = 0;

    // Check if dividend is negative
    bool is_negative = (dividend < 0) ^ (divisor < 0);

    // Convert dividend and divisor to positive
    long long abs_dividend = abs((long long)dividend);
    long long abs_divisor = abs((long long)divisor);

    // Perform bit manipulation
    while (abs_dividend >= abs_divisor) {
        long long temp = abs_divisor;
        int i = 1;
        while (abs_dividend >= (temp << 1)) {
            temp <<= 1;
            i <<= 1;
        }
        abs_dividend -= temp;
        quotient += i;
    }

    // If dividend was negative, make quotient negative
    if (is_negative) {
        quotient = -quotient;
    }

    // Check for integer overflow
    if (quotient > INT_MAX || quotient < INT_MIN) {
        throw runtime_error("Integer overflow");
    }

    return quotient;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log\ dividend)$, where `dividend` is the input integer. This occurs because we use bit manipulation to find the largest power of 2 that can be subtracted from `dividend`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the quotient and other variables.
> - **Optimality proof:** This approach is optimal because we are using bit manipulation to find the largest power of 2 that can be subtracted from `dividend`, which reduces the number of operations required to find the quotient.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, repeated subtraction.
- Problem-solving patterns identified: Using bit manipulation to find the largest power of 2 that can be subtracted from a number.
- Optimization techniques learned: Using bit manipulation to reduce the number of operations required to find the quotient.
- Similar problems to practice: Other problems that involve bit manipulation, such as finding the largest power of 2 that divides a number.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where `dividend` is the minimum possible integer value and `divisor` is `-1`.
- Edge cases to watch for: Not checking for integer overflow when calculating the quotient.
- Performance pitfalls: Using repeated subtraction instead of bit manipulation to find the quotient.
- Testing considerations: Testing the function with different input values, including negative numbers and edge cases.