## Alternating Digit Sum
**Problem Link:** https://leetcode.com/problems/alternating-digit-sum/description

**Problem Statement:**
- Input: An integer `n`.
- Output: The alternating sum of its digits.
- Key requirements: Calculate the sum by alternating between addition and subtraction of digits from left to right.
- Example test cases: 
  - Input: `n = 521`, Output: `5 - 2 + 1 = 4`
  - Input: `n = 111`, Output: `1 - 1 + 1 = 1`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Convert the integer into a string to easily access each digit, then iterate through the string, adding or subtracting each digit based on its position.
- Step-by-step breakdown: 
  1. Convert the integer to a string.
  2. Initialize a variable to keep track of the sum.
  3. Iterate through each character (digit) in the string.
  4. For each digit, check if its position is even or odd. If even, add the digit to the sum; if odd, subtract the digit from the sum.
  5. After iterating through all digits, return the final sum.

```cpp
int alternateDigitSum(int n) {
    string str = to_string(n);
    int sum = 0;
    for (int i = 0; i < str.length(); i++) {
        int digit = str[i] - '0'; // Convert char to int
        if (i % 2 == 0) { // Even position
            sum += digit;
        } else { // Odd position
            sum -= digit;
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$, where $n$ is the input integer. The reason is that the number of digits in an integer $n$ is proportional to $log(n)$.
> - **Space Complexity:** $O(log(n))$ due to the conversion of the integer to a string.
> - **Why these complexities occur:** The iteration through the digits of the number is the primary operation, and since the number of digits is $log(n)$, this dictates the time complexity. The space complexity is due to the storage of the string representation of the number.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The process can be optimized by directly calculating the sum without converting the integer to a string. This can be achieved by using the modulo operator to extract the last digit of the number and then removing this digit from the number.
- Detailed breakdown: 
  1. Initialize a variable to store the sum.
  2. Initialize a flag to track whether the next operation should be addition or subtraction.
  3. While the number is greater than 0, extract the last digit by taking the number modulo 10.
  4. If the flag is set for addition, add the digit to the sum; otherwise, subtract it.
  5. Remove the last digit from the number by performing integer division by 10.
  6. Toggle the flag for the next operation.
  7. Repeat until all digits have been processed.

```cpp
int alternateDigitSum(int n) {
    int sum = 0;
    bool add = true; // Flag to determine whether to add or subtract
    while (n > 0) {
        int digit = n % 10; // Extract the last digit
        if (add) {
            sum += digit;
        } else {
            sum -= digit;
        }
        n /= 10; // Remove the last digit
        add = !add; // Toggle the flag for the next operation
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$, as the number of operations is proportional to the number of digits in $n$.
> - **Space Complexity:** $O(1)$, since only a constant amount of space is used, regardless of the input size.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to compute the alternating sum, directly manipulating the integer without the need for string conversion, thus reducing space complexity to a constant.

---

### Final Notes

**Learning Points:**
- The importance of considering different data types (e.g., string vs. integer) for solving problems.
- How to optimize algorithms by minimizing unnecessary operations and data conversions.
- Understanding the relationship between the number of digits in an integer and its logarithm.

**Mistakes to Avoid:**
- Not considering the implications of data type conversions on performance.
- Overlooking the potential for direct calculation methods that avoid unnecessary steps.
- Failing to analyze the space complexity of solutions, especially when dealing with large inputs.