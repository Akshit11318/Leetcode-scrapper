## Minimum Sum of Four Digit Number After Splitting Digits

**Problem Link:** https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description

**Problem Statement:**
- Given a 4-digit integer, split it into two 2-digit integers.
- The minimum sum of these two integers should be found.
- Input format: a single integer `num` between 1000 and 9999 (inclusive).
- Expected output format: the minimum possible sum of the two 2-digit integers.
- Key requirements: the input number must be split into two 2-digit numbers, and the sum of these two numbers should be minimized.
- Example test cases:
  - Input: `num = 2932`, Output: `52`, Explanation: The minimum sum is obtained by splitting the number into 29 and 32, resulting in a sum of 29 + 32 = 61. However, the optimal split is into 29 and 23, yielding a sum of 29 + 23 = 52.
  - Input: `num = 4009`, Output: `49`, Explanation: The optimal split is into 40 and 09, resulting in a sum of 40 + 9 = 49.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of splitting the 4-digit number into two 2-digit numbers.
- Step-by-step breakdown:
  1. Extract the digits of the input number `num`.
  2. Generate all possible pairs of 2-digit numbers that can be formed by rearranging these digits.
  3. Calculate the sum of each pair.
  4. Find the minimum sum among all pairs.
- This approach comes to mind first because it systematically explores all possibilities, ensuring that the minimum sum is found.

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int minimumSum(int num) {
    int digits[4];
    // Extract digits
    digits[0] = num / 1000;
    digits[1] = (num % 1000) / 100;
    digits[2] = (num % 100) / 10;
    digits[3] = num % 10;
    
    // Generate all permutations of digits
    int minSum = INT_MAX;
    do {
        // Calculate sum for current permutation
        int sum = (digits[0]*10 + digits[1]) + (digits[2]*10 + digits[3]);
        minSum = min(minSum, sum);
    } while (next_permutation(digits, digits + 4));
    
    return minSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because there are only 24 permutations of 4 digits, and each permutation takes constant time to process.
> - **Space Complexity:** $O(1)$, as we only use a fixed amount of space to store the digits and the current sum.
> - **Why these complexities occur:** The brute force approach has a constant time complexity because, despite the permutation generation, the number of operations is bounded by a constant (the number of permutations of 4 items).

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that to minimize the sum, the largest digits should be paired with the smallest digits, and the next largest with the next smallest, to minimize the value of each 2-digit number.
- Detailed breakdown:
  1. Sort the digits in ascending order.
  2. Form the first 2-digit number by combining the smallest and the next smallest digits.
  3. Form the second 2-digit number by combining the largest and the next largest digits.
- This approach is optimal because it ensures the smallest possible values for each 2-digit number, thus minimizing their sum.

```cpp
int minimumSum(int num) {
    int digits[4];
    // Extract digits
    digits[0] = num / 1000;
    digits[1] = (num % 1000) / 100;
    digits[2] = (num % 100) / 10;
    digits[3] = num % 10;
    
    // Sort digits
    sort(digits, digits + 4);
    
    // Form and return the minimum sum
    return (digits[0]*10 + digits[2]) + (digits[1]*10 + digits[3]);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because sorting 4 elements and forming the sum takes constant time.
> - **Space Complexity:** $O(1)$, as we only use a fixed amount of space to store the digits.
> - **Optimality proof:** This approach is optimal because it minimizes the sum by pairing the smallest digits with the next smallest and the largest with the next largest, ensuring the smallest possible values for each 2-digit number.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: permutation generation, sorting, and optimization through digit rearrangement.
- Problem-solving patterns identified: minimizing sums through strategic pairing.
- Optimization techniques learned: using sorting to minimize the sum of paired digits.

**Mistakes to Avoid:**
- Not considering all possible permutations of the digits.
- Not optimizing the pairing of digits to minimize the sum.
- Overlooking the simplicity of sorting as a method to find the optimal pairing.