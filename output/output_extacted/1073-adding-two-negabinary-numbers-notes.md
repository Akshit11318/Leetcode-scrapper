## Adding Two Negabinary Numbers
**Problem Link:** https://leetcode.com/problems/adding-two-negabinary-numbers/description

**Problem Statement:**
- Input format and constraints: The input consists of two arrays, `arr1` and `arr2`, representing negabinary numbers. Each array contains integers, where each integer is either 0 or 1. The numbers are represented in base -2 (negabinary). The task is to add these two numbers and return the result as an array representing the sum in negabinary.
- Expected output format: The output should be an array of integers, where each integer is either 0 or 1, representing the sum of `arr1` and `arr2` in negabinary.
- Key requirements and edge cases to consider: Handling carry-over from the addition of two digits, dealing with the base -2 system, and ensuring the output is correctly represented in negabinary.
- Example test cases with explanations: For example, adding `[1,1,1,1,1]` and `[1,0,1]` should result in `[1,0,0,0,0]` because in base -2, the calculation is as follows: `11111 (base -2) + 101 (base -2) = 10000 (base -2)`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Convert each negabinary number to decimal, add the two decimal numbers, and then convert the sum back to negabinary.
- Step-by-step breakdown of the solution:
  1. Convert each negabinary number to decimal.
  2. Add the two decimal numbers.
  3. Convert the sum back to negabinary.
- Why this approach comes to mind first: It's a straightforward method that leverages the understanding of base conversion and arithmetic operations.

```cpp
#include <iostream>
#include <vector>

std::vector<int> addNegabinary(std::vector<int>& arr1, std::vector<int>& arr2) {
    int num1 = 0, num2 = 0;
    for (int i = arr1.size() - 1; i >= 0; --i) {
        num1 += arr1[i] * pow(-2, arr1.size() - 1 - i);
    }
    for (int i = arr2.size() - 1; i >= 0; --i) {
        num2 += arr2[i] * pow(-2, arr2.size() - 1 - i);
    }
    int sum = num1 + num2;
    if (sum == 0) return {0};
    std::vector<int> result;
    while (sum != 0) {
        int remainder = sum % -2;
        sum /= -2;
        if (remainder < 0) {
            remainder += 2;
            sum++;
        }
        result.push_back(remainder);
    }
    std::reverse(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m + log|sum|)$, where $n$ and $m$ are the lengths of `arr1` and `arr2`, respectively, and $log|sum|$ accounts for the conversion of the sum back to negabinary.
> - **Space Complexity:** $O(n + m + log|sum|)$, for storing the input arrays and the result.
> - **Why these complexities occur:** The conversion to decimal and back to negabinary involves iterating through the input arrays and performing arithmetic operations that depend on the size of the inputs and the sum.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Perform the addition directly in negabinary without converting to decimal, using a similar approach to adding binary numbers but taking into account the base -2 system.
- Detailed breakdown of the approach:
  1. Initialize pointers at the end of both arrays and a result array.
  2. Iterate through both arrays from right to left, adding corresponding digits and handling carry-over.
  3. If a carry-over occurs, adjust the current sum and the carry for the next iteration, considering the base -2 system.
- Proof of optimality: This approach avoids the overhead of converting between bases and directly computes the sum in negabinary, making it more efficient.

```cpp
std::vector<int> addNegabinary(std::vector<int>& arr1, std::vector<int>& arr2) {
    std::vector<int> result;
    int carry = 0, i = arr1.size() - 1, j = arr2.size() - 1;
    while (i >= 0 || j >= 0 || carry) {
        if (i >= 0) carry += arr1[i--];
        if (j >= 0) carry += arr2[j--];
        result.push_back(carry % 2);
        carry = -(carry / 2);
    }
    // Remove leading zeros
    while (result.size() > 1 && result.back() == 0) result.pop_back();
    std::reverse(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(max(n, m))$, where $n$ and $m$ are the lengths of `arr1` and `arr2`, respectively.
> - **Space Complexity:** $O(max(n, m))$, for storing the result.
> - **Optimality proof:** This approach directly computes the sum in negabinary without the need for base conversion, making it the most efficient method.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Base conversion, arithmetic operations in non-standard bases, and optimization techniques.
- Problem-solving patterns identified: Direct computation in the target base can be more efficient than converting between bases.
- Optimization techniques learned: Avoiding unnecessary conversions and leveraging the properties of the base -2 system.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of carry-over in the base -2 system.
- Edge cases to watch for: Handling arrays of different lengths and ensuring correct output for sums that result in leading zeros.
- Performance pitfalls: Converting between bases unnecessarily, which can lead to inefficiencies.
- Testing considerations: Thoroughly testing with various input lengths and values to ensure correctness.