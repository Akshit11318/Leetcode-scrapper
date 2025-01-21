## Sum of Square Numbers

**Problem Link:** https://leetcode.com/problems/sum-of-square-numbers/description

**Problem Statement:**
- Input format: An integer `n`.
- Constraints: `1 <= n <= 10^4`.
- Expected output format: A boolean indicating whether `n` can be expressed as the sum of two square numbers.
- Key requirements and edge cases to consider: Handling cases where `n` is a perfect square, and cases where `n` is an odd number.
- Example test cases with explanations:
  - `n = 5`, return `True` because `5 = 1^2 + 2^2`.
  - `n = 3`, return `False` because there are no integer solutions for `a` and `b` such that `3 = a^2 + b^2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check all possible combinations of squares that sum up to `n`.
- Step-by-step breakdown of the solution:
  1. Iterate over all numbers from `0` to `sqrt(n)`.
  2. For each number `a`, calculate `b = sqrt(n - a^2)`.
  3. If `b` is an integer, return `True`.
  4. If no such pair is found after checking all numbers, return `False`.
- Why this approach comes to mind first: It's a straightforward solution that checks all possible combinations.

```cpp
class Solution {
public:
    bool judgeSquareSum(int n) {
        for (int a = 0; a * a <= n; a++) {
            double b = sqrt(n - a * a);
            if (b == (int)b) return true;
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\sqrt{n})$ because we iterate up to the square root of `n`.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity is due to the loop that iterates up to the square root of `n`, and the space complexity is constant because we don't use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a similar approach to the brute force solution, but with a slight optimization.
- Detailed breakdown of the approach:
  1. Iterate over all numbers from `0` to `sqrt(n)`.
  2. For each number `a`, calculate `b = sqrt(n - a^2)`.
  3. If `b` is an integer, return `True`.
  4. If no such pair is found after checking all numbers, return `False`.
- Proof of optimality: This solution is optimal because it checks all possible combinations of squares that sum up to `n` in the most efficient way possible.
- Why further optimization is impossible: We must check all possible combinations of squares, and this solution does so in the most efficient way possible.

```cpp
class Solution {
public:
    bool judgeSquareSum(int n) {
        for (int a = 0; a * a <= n; a++) {
            double b = sqrt(n - a * a);
            if (b == (int)b) return true;
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\sqrt{n})$ because we iterate up to the square root of `n`.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space.
> - **Optimality proof:** This solution is optimal because it checks all possible combinations of squares in the most efficient way possible.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Checking all possible combinations of squares that sum up to `n`.
- Problem-solving patterns identified: Using a brute force approach and optimizing it to find the most efficient solution.
- Optimization techniques learned: Iterating up to the square root of `n` to reduce the number of iterations.
- Similar problems to practice: Finding the sum of two cubes, finding the sum of two fourth powers, etc.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for integer values of `b`, not iterating up to the square root of `n`.
- Edge cases to watch for: Handling cases where `n` is a perfect square, handling cases where `n` is an odd number.
- Performance pitfalls: Iterating up to `n` instead of the square root of `n`.
- Testing considerations: Testing with large values of `n`, testing with perfect squares, testing with odd numbers.