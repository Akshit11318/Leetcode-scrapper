## Simplified Fractions
**Problem Link:** https://leetcode.com/problems/simplified-fractions/description

**Problem Statement:**
- Input format and constraints: Given an integer `n`, return a list of all non-negative integers `less than or equal to n` that are not `0` or `1` that are not divisible by any integer `less than n and greater than 1`.
- Expected output format: A list of simplified fractions in the format `i/j` where `i` and `j` are non-negative integers.
- Key requirements and edge cases to consider: The input `n` is guaranteed to be in the range `[2, 31]`.
- Example test cases with explanations:
  - For `n = 2`, the output should be `["1/2"]`.
  - For `n = 3`, the output should be `["1/2", "1/3", "2/3"]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To generate all possible fractions, we can use two nested loops to iterate over all possible numerators and denominators.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the simplified fractions.
  2. Iterate over all possible denominators from 2 to `n`.
  3. For each denominator, iterate over all possible numerators from 1 to `denominator - 1`.
  4. Check if the numerator and denominator have a common divisor greater than 1. If they do, skip this fraction.
  5. Add the simplified fraction to the list.
- Why this approach comes to mind first: It's a straightforward way to generate all possible fractions and then filter out the ones that are not simplified.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <numeric>

std::vector<std::string> simplifiedFractions(int n) {
    std::vector<std::string> result;
    for (int denominator = 2; denominator <= n; denominator++) {
        for (int numerator = 1; numerator < denominator; numerator++) {
            if (std::gcd(numerator, denominator) == 1) {
                result.push_back(std::to_string(numerator) + "/" + std::to_string(denominator));
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the input number. This is because we have two nested loops, each of which iterates up to $n$ times.
> - **Space Complexity:** $O(n^2)$, where $n$ is the input number. This is because we store all the simplified fractions in a list, and in the worst case, we might have to store $n^2$ fractions.
> - **Why these complexities occur:** The time complexity occurs because we are using two nested loops to generate all possible fractions. The space complexity occurs because we are storing all the simplified fractions in a list.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use the same approach as the brute force solution, but with a slight optimization. We can use a single loop to iterate over all possible denominators, and for each denominator, we can use a single loop to iterate over all possible numerators.
- Detailed breakdown of the approach:
  1. Initialize an empty list to store the simplified fractions.
  2. Iterate over all possible denominators from 2 to `n`.
  3. For each denominator, iterate over all possible numerators from 1 to `denominator - 1`.
  4. Check if the numerator and denominator have a common divisor greater than 1. If they do, skip this fraction.
  5. Add the simplified fraction to the list.
- Proof of optimality: This approach is optimal because it generates all possible simplified fractions in a single pass, without any redundant calculations.
- Why further optimization is impossible: This approach is already optimal because it has a time complexity of $O(n^2)$, which is the best possible time complexity for this problem.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <numeric>

std::vector<std::string> simplifiedFractions(int n) {
    std::vector<std::string> result;
    for (int denominator = 2; denominator <= n; denominator++) {
        for (int numerator = 1; numerator < denominator; numerator++) {
            if (std::gcd(numerator, denominator) == 1) {
                result.push_back(std::to_string(numerator) + "/" + std::to_string(denominator));
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the input number. This is because we have two nested loops, each of which iterates up to $n$ times.
> - **Space Complexity:** $O(n^2)$, where $n$ is the input number. This is because we store all the simplified fractions in a list, and in the worst case, we might have to store $n^2$ fractions.
> - **Optimality proof:** This approach is optimal because it generates all possible simplified fractions in a single pass, without any redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The use of nested loops to generate all possible fractions, and the use of the `std::gcd` function to check if two numbers have a common divisor.
- Problem-solving patterns identified: The use of a single loop to iterate over all possible denominators, and the use of a single loop to iterate over all possible numerators.
- Optimization techniques learned: The use of a single pass to generate all possible simplified fractions, without any redundant calculations.
- Similar problems to practice: Generating all possible combinations of a set of numbers, or generating all possible permutations of a set of numbers.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the numerator and denominator have a common divisor greater than 1, or not handling the case where the denominator is 1.
- Edge cases to watch for: The case where the input number is 1, or the case where the input number is less than 2.
- Performance pitfalls: Using a brute force approach that has a time complexity of $O(n^3)$ or worse.
- Testing considerations: Testing the function with a variety of input values, including edge cases and large input values.