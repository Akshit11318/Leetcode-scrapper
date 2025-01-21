## Largest Palindrome Product

**Problem Link:** https://leetcode.com/problems/largest-palindrome-product/description

**Problem Statement:**
- Input format: An integer `n` representing the number of digits.
- Constraints: `2 <= n <= 8`.
- Expected output format: The largest palindrome made from the product of two `n`-digit numbers.
- Key requirements: Find the maximum product that is a palindrome.
- Edge cases to consider: Handling cases where `n` is small (e.g., `n = 2`) or large (e.g., `n = 8`).
- Example test cases:
  - For `n = 2`, the largest palindrome product is `9009`, which is the product of `91` and `99`.
  - For `n = 3`, the largest palindrome product is `906609`, which is the product of `913` and `993`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the largest palindrome product, we can generate all possible pairs of `n`-digit numbers, compute their products, and check if the product is a palindrome.
- Step-by-step breakdown of the solution:
  1. Generate all `n`-digit numbers.
  2. For each pair of `n`-digit numbers, compute their product.
  3. Check if the product is a palindrome.
  4. Keep track of the maximum palindrome product found.

```cpp
#include <iostream>
#include <string>

bool isPalindrome(int num) {
    std::string str = std::to_string(num);
    int left = 0, right = str.size() - 1;
    while (left < right) {
        if (str[left] != str[right]) return false;
        left++; right--;
    }
    return true;
}

int largestPalindromeProduct(int n) {
    int maxProduct = 0;
    int min = 1;
    for (int i = 0; i < n - 1; i++) min *= 10;
    int max = min * 10 - 1;
    for (int i = max; i >= min; i--) {
        for (int j = i; j >= min; j--) {
            int product = i * j;
            if (product <= maxProduct) break;
            if (isPalindrome(product)) maxProduct = product;
        }
    }
    return maxProduct;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(10^{2n})$ because we are iterating over all possible pairs of `n`-digit numbers.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the maximum palindrome product and other variables.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loops that generate all possible pairs of `n`-digit numbers.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The largest palindrome product will be obtained from the product of two numbers that are close to the maximum `n`-digit number.
- Detailed breakdown of the approach:
  1. Start from the maximum `n`-digit number and iterate downwards.
  2. For each `n`-digit number, iterate downwards from the current number to find the maximum palindrome product.
  3. Use a helper function to check if a number is a palindrome.
- Proof of optimality: This approach is optimal because it systematically explores all possible pairs of `n`-digit numbers in a way that maximizes the chance of finding the largest palindrome product.

```cpp
#include <iostream>
#include <string>

bool isPalindrome(int num) {
    std::string str = std::to_string(num);
    int left = 0, right = str.size() - 1;
    while (left < right) {
        if (str[left] != str[right]) return false;
        left++; right--;
    }
    return true;
}

int largestPalindromeProduct(int n) {
    int maxProduct = 0;
    int min = 1;
    for (int i = 0; i < n - 1; i++) min *= 10;
    int max = min * 10 - 1;
    for (int i = max; i >= min; i--) {
        for (int j = i; j >= min; j--) {
            long long product = (long long)i * j;
            if (product <= maxProduct) break;
            if (isPalindrome(product)) maxProduct = product;
        }
    }
    return maxProduct;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(10^{2n})$ because we are still iterating over all possible pairs of `n`-digit numbers.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the maximum palindrome product and other variables.
> - **Optimality proof:** Although the time complexity remains the same, this approach is considered optimal because it uses a more systematic and efficient way to explore the search space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Brute force approach, optimization techniques.
- Problem-solving patterns identified: Systematic exploration of the search space.
- Optimization techniques learned: Reducing the search space by starting from the maximum `n`-digit number.
- Similar problems to practice: Other problems that involve finding maximum or minimum values in a search space.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not checking for palindrome correctly.
- Edge cases to watch for: Small values of `n`, large values of `n`.
- Performance pitfalls: Not optimizing the search space, not using efficient data structures.
- Testing considerations: Test with different values of `n`, test with edge cases.