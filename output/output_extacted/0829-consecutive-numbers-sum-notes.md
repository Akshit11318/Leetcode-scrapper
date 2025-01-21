## Consecutive Numbers Sum
**Problem Link:** https://leetcode.com/problems/consecutive-numbers-sum/description

**Problem Statement:**
- Input format: An integer `n`.
- Constraints: `1 <= n <= 10^9`.
- Expected output format: The number of ways to express `n` as a sum of consecutive numbers.
- Key requirements: Find all sequences of consecutive numbers that sum up to `n`.
- Example test cases:
  - Input: `5`
  - Output: `2`
  - Explanation: `5 = 5` and `5 = 2 + 3`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible sequences of consecutive numbers.
- Step-by-step breakdown:
  1. Start from the first number `1`.
  2. For each starting number, try all possible sequence lengths.
  3. Calculate the sum of the sequence.
  4. If the sum equals `n`, increment the count.
- Why this approach comes to mind first: It is the most straightforward way to generate all possible sequences.

```cpp
class Solution {
public:
    int consecutiveNumbersSum(int n) {
        int count = 0;
        for (int start = 1; start <= n; start++) {
            int sum = 0;
            for (int length = 1; length <= n; length++) {
                sum += start + length - 1;
                if (sum == n) {
                    count++;
                } else if (sum > n) {
                    break;
                }
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the input number.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The sum of a sequence of consecutive numbers can be expressed as `(start + end) * length / 2`, where `start` is the first number, `end` is the last number, and `length` is the number of terms.
- Detailed breakdown:
  1. Express the sum of the sequence using the formula.
  2. Rearrange the formula to get `length = 2 * n / (end + start)`.
  3. Since `length` must be an integer, `end + start` must be a divisor of `2 * n`.
  4. Try all possible divisors of `2 * n` as `end + start`.
- Proof of optimality: This approach tries all possible sequences of consecutive numbers in a more efficient way than the brute force approach.

```cpp
class Solution {
public:
    int consecutiveNumbersSum(int n) {
        int count = 0;
        for (int sum = 2; sum <= 2 * n; sum++) {
            if ((2 * n) % sum == 0) {
                int length = (2 * n) / sum;
                if ((sum - length + 1) % 2 == 0) {
                    count++;
                }
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\sqrt{n})$, where $n$ is the input number.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** This approach tries all possible sequences of consecutive numbers in the most efficient way possible.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using mathematical formulas to simplify problems, trying all possible divisors of a number.
- Problem-solving patterns identified: Expressing the problem in terms of a mathematical formula, using the properties of the formula to simplify the solution.
- Optimization techniques learned: Using a more efficient algorithm to try all possible sequences of consecutive numbers.
- Similar problems to practice: Finding the number of ways to express a number as a sum of squares, finding the number of ways to express a number as a product of prime numbers.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for integer division, not handling edge cases.
- Edge cases to watch for: When `n` is 1, when `n` is a prime number.
- Performance pitfalls: Using a brute force approach, not optimizing the solution.
- Testing considerations: Test the solution with large inputs, test the solution with small inputs.