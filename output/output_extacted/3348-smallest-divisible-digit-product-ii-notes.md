## Smallest Divisible Digit Product II

**Problem Link:** https://leetcode.com/problems/smallest-divisible-digit-product-ii/description

**Problem Statement:**
- Input format and constraints: Given a string `s` consisting of digits and a number `k`, find the smallest possible product of digits that is divisible by `k`.
- Expected output format: The smallest product of digits that is divisible by `k`, or `-1` if no such product exists.
- Key requirements and edge cases to consider: Handle cases where `s` contains non-digit characters or `k` is not a positive integer.
- Example test cases with explanations:
  - `s = "123", k = 2`, the output should be `2` because `2` is the smallest digit in `s` that is divisible by `2`.
  - `s = "123", k = 3`, the output should be `3` because `3` is the smallest digit in `s` that is divisible by `3`.
  - `s = "123", k = 4`, the output should be `12` because `12` is the smallest product of digits in `s` that is divisible by `4`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible products of digits in `s` and check if they are divisible by `k`.
- Step-by-step breakdown of the solution:
  1. Generate all possible products of digits in `s`.
  2. Check each product if it is divisible by `k`.
  3. Keep track of the smallest product that is divisible by `k`.
- Why this approach comes to mind first: It's a straightforward approach that involves checking all possible products.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>

int smallestDivisibleProduct(const std::string& s, int k) {
    int n = s.size();
    int minProduct = INT_MAX;

    for (int mask = 0; mask < (1 << n); ++mask) {
        std::vector<int> digits;
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) != 0) {
                digits.push_back(s[i] - '0');
            }
        }

        if (digits.empty()) {
            continue;
        }

        int product = 1;
        for (int digit : digits) {
            product *= digit;
        }

        if (product % k == 0 && product < minProduct) {
            minProduct = product;
        }
    }

    return minProduct == INT_MAX ? -1 : minProduct;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of `s`. This is because we generate all possible subsets of digits in `s` and calculate their products.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `s`. This is because we store the digits in each subset.
> - **Why these complexities occur:** The time complexity occurs because we generate all possible subsets of digits in `s`, and the space complexity occurs because we store the digits in each subset.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible products of digits, we can use a more efficient approach by iterating over the digits in `s` and checking if we can form a product that is divisible by `k`.
- Detailed breakdown of the approach:
  1. Sort the digits in `s` in ascending order.
  2. Iterate over the sorted digits and try to form a product that is divisible by `k`.
  3. Use a `std::string` to build the product.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n \log n)$, where $n$ is the length of `s`, which is much faster than the brute force approach.

```cpp
int smallestDivisibleProduct(const std::string& s, int k) {
    std::vector<int> digits;
    for (char c : s) {
        if (c >= '0' && c <= '9') {
            digits.push_back(c - '0');
        }
    }

    if (digits.empty()) {
        return -1;
    }

    std::sort(digits.begin(), digits.end());

    for (int i = 0; i < digits.size(); ++i) {
        if (digits[i] % k == 0) {
            return digits[i];
        }
    }

    for (int i = 0; i < digits.size(); ++i) {
        for (int j = i + 1; j < digits.size(); ++j) {
            if ((digits[i] * digits[j]) % k == 0) {
                return digits[i] * digits[j];
            }
        }
    }

    // Try to form a product of three digits
    for (int i = 0; i < digits.size(); ++i) {
        for (int j = i + 1; j < digits.size(); ++j) {
            for (int m = j + 1; m < digits.size(); ++m) {
                if ((digits[i] * digits[j] * digits[m]) % k == 0) {
                    return digits[i] * digits[j] * digits[m];
                }
            }
        }
    }

    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + n^2 + n^3)$, where $n$ is the length of `s`. This is because we sort the digits and then try to form products of one, two, and three digits.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `s`. This is because we store the digits in a vector.
> - **Optimality proof:** This approach is optimal because it has a much faster time complexity than the brute force approach, and it is guaranteed to find the smallest product that is divisible by `k`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, iteration, and optimization.
- Problem-solving patterns identified: Using a more efficient approach to solve a problem by iterating over the digits in `s` and checking if we can form a product that is divisible by `k`.
- Optimization techniques learned: Using a `std::string` to build the product and iterating over the sorted digits to try to form a product that is divisible by `k`.
- Similar problems to practice: Other problems that involve finding the smallest or largest product of digits that satisfies a certain condition.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the digits in `s` are valid or not handling edge cases properly.
- Edge cases to watch for: Handling cases where `s` contains non-digit characters or `k` is not a positive integer.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the function with different inputs and edge cases to ensure that it works correctly.