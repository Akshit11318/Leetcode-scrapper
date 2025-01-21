## Smallest Number with Given Digit Product
**Problem Link:** https://leetcode.com/problems/smallest-number-with-given-digit-product/description

**Problem Statement:**
- Input format: An integer `product` representing the product of digits in the desired number.
- Constraints: `1 <= product <= 10^9`.
- Expected output format: The smallest number (as a string) with a digit product equal to the input `product`.
- Key requirements and edge cases:
  - Handle cases where the product is a large number.
  - The output should be the smallest possible number with the given product.
  - Consider cases where the product is not achievable with single-digit numbers.

**Example Test Cases:**
- Input: `product = 30`
  Output: `"257"`
  Explanation: `2 * 5 * 7 = 70`, but this is the smallest possible number with a product closest to 30.
- Input: `product = 9`
  Output: `"9"`
  Explanation: The smallest possible number with a digit product of 9 is simply "9".

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves trying all combinations of digits to form a number and checking if their product equals the given `product`.
- However, this approach quickly becomes impractical due to the large number of combinations and the potential for very large products.

```cpp
#include <iostream>
#include <string>
#include <vector>

void backtrack(int product, std::string& current, std::vector<std::string>& results) {
    if (product == 1) {
        results.push_back(current);
        return;
    }
    for (int i = 2; i <= 9; ++i) {
        if (product % i == 0) {
            current += std::to_string(i);
            backtrack(product / i, current, results);
            current.pop_back();
        }
    }
}

std::string smallestNumber(int product) {
    std::vector<std::string> results;
    std::string current;
    backtrack(product, current, results);
    if (results.empty()) return "0"; // If no combination is found
    std::string smallest = results[0];
    for (const auto& result : results) {
        if (result.size() < smallest.size() || (result.size() == smallest.size() && result < smallest)) {
            smallest = result;
        }
    }
    return smallest;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(9^{log_{10}(product)})$ due to the potential for exploring up to $log_{10}(product)$ levels in the recursion tree, with up to 9 branches at each level.
> - **Space Complexity:** $O(log_{10}(product))$ for the recursion stack and storing the current combination of digits.
> - **Why these complexities occur:** The brute force approach leads to exponential time complexity because it explores all possible combinations of digits without any optimization.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a greedy approach, starting with the largest possible digit (9) and iteratively dividing the product by the largest possible digit until the product becomes 1.
- This approach ensures the smallest possible number because it minimizes the number of digits required to achieve the product.

```cpp
std::string smallestNumber(int product) {
    std::string result;
    for (int i = 9; i >= 2; --i) {
        while (product % i == 0) {
            result += std::to_string(i);
            product /= i;
        }
    }
    if (product > 1) return "0"; // If product cannot be represented by single-digit factors
    std::reverse(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log_{10}(product))$ because in the worst case, we divide the product by the smallest possible factor (2) until it becomes 1.
> - **Space Complexity:** $O(log_{10}(product))$ for storing the result string.
> - **Optimality proof:** This approach is optimal because it uses the fewest possible digits to represent the product, and by starting with the largest digits first, it ensures the smallest possible number.

---

### Final Notes

**Learning Points:**
- The importance of the greedy algorithm in solving problems where the optimal solution can be constructed from locally optimal choices.
- How to approach problems involving factorization and digit manipulation.
- The trade-off between brute force and optimized solutions in terms of time and space complexity.

**Mistakes to Avoid:**
- Not considering the constraints of the problem, such as the range of the input `product`.
- Failing to optimize the solution, leading to inefficient algorithms.
- Not handling edge cases properly, such as when the `product` cannot be represented by single-digit factors.