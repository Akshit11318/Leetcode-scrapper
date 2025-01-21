## Subtract the Product and Sum of Digits of an Integer

**Problem Link:** https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description

**Problem Statement:**
- Input: An integer `n`.
- Constraints: `1 <= n <= 10^5`.
- Expected output: The difference between the product of its digits and the sum of its digits.
- Key requirements and edge cases: Handle cases where `n` has leading zeros, negative numbers, and very large integers.

**Example Test Cases:**
- For `n = 234`, the product of digits is `2 * 3 * 4 = 24` and the sum of digits is `2 + 3 + 4 = 9`. Therefore, the output should be `24 - 9 = 15`.
- For `n = 4421`, the product of digits is `4 * 4 * 2 * 1 = 32` and the sum of digits is `4 + 4 + 2 + 1 = 11`. Therefore, the output should be `32 - 11 = 21`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves directly calculating the product and sum of the digits of the input integer `n`.
- We start by initializing two variables, `product` and `sum`, to 1 and 0, respectively.
- Then, we iterate through each digit of `n` from right to left (i.e., from the least significant digit to the most significant digit).
- For each digit, we multiply the current `product` by the digit and add the digit to the `sum`.
- Finally, we return the difference between the `product` and the `sum`.

```cpp
int subtractProductAndSum(int n) {
    int product = 1;
    int sum = 0;
    while (n > 0) {
        int digit = n % 10;
        product *= digit;
        sum += digit;
        n /= 10;
    }
    return product - sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the input integer. This is because we are iterating through each digit of `n`, and the number of digits in `n` is proportional to $\log n$.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the `product` and `sum` variables.
> - **Why these complexities occur:** The time complexity occurs because we are iterating through each digit of `n`, and the space complexity occurs because we are using a constant amount of space to store the intermediate results.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is the same as the brute force approach, as we must iterate through each digit of `n` to calculate the product and sum.
- However, we can make some minor optimizations to the code, such as using more descriptive variable names and adding comments to explain the logic.
- The key insight is that we can calculate the product and sum in a single pass through the digits of `n`, without needing to store the digits in an array or list.

```cpp
int subtractProductAndSum(int n) {
    int digitProduct = 1;
    int digitSum = 0;
    while (n > 0) {
        // Extract the least significant digit of n
        int digit = n % 10;
        // Update the product and sum
        digitProduct *= digit;
        digitSum += digit;
        // Remove the least significant digit from n
        n /= 10;
    }
    // Return the difference between the product and sum
    return digitProduct - digitSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the input integer. This is because we are iterating through each digit of `n`, and the number of digits in `n` is proportional to $\log n$.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the `digitProduct` and `digitSum` variables.
> - **Optimality proof:** This approach is optimal because we must iterate through each digit of `n` to calculate the product and sum, and we are doing so in a single pass.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the ability to iterate through each digit of an integer using the modulo operator (`%`) and integer division (`/`).
- The problem-solving pattern identified is the use of a single pass through the digits of an integer to calculate multiple values (in this case, the product and sum).
- The optimization technique learned is the use of descriptive variable names and comments to improve code readability.

**Mistakes to Avoid:**
- A common implementation error is to forget to initialize the `product` variable to 1, rather than 0. This would cause the product to be 0, regardless of the input.
- An edge case to watch for is when the input `n` is 0. In this case, the product and sum are both 0, so the function should return 0.
- A performance pitfall to avoid is using a recursive approach to iterate through the digits of `n`, as this would cause a stack overflow for large inputs.