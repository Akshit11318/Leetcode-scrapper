## Harshad Number
**Problem Link:** https://leetcode.com/problems/harshad-number/description

**Problem Statement:**
- Input: An integer `n`
- Constraints: $1 \leq n \leq 100$
- Expected output: Determine if `n` is a **Harshad number**, which is an integer that is divisible by the sum of its digits.
- Key requirements and edge cases to consider:
  - A number is divisible by its digit sum if the remainder when the number is divided by its digit sum is 0.
  - All numbers in the given range are positive integers.
- Example test cases with explanations:
  - Input: `n = 19`, Output: `true` because 1 + 9 = 10 and 19 is not divisible by 10, but since 19 is not divisible by 10 it is not a Harshad number. 
  - Input: `n = 13`, Output: `false` because 1 + 3 = 4 and 13 is not divisible by 4.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the sum of the digits of `n`, then check if `n` is divisible by this sum.
- Step-by-step breakdown of the solution:
  1. Convert the integer `n` to a string to easily iterate over its digits.
  2. Calculate the sum of the digits by converting each character back to an integer and summing them up.
  3. Check if `n` is divisible by the sum of its digits by using the modulus operator (`%`). If the remainder is 0, then `n` is a Harshad number.
- Why this approach comes to mind first: It directly implements the definition of a Harshad number without requiring any additional mathematical insights or optimizations.

```cpp
bool isHarshad(int n) {
    int digitSum = 0;
    int original = n;
    while (n > 0) {
        digitSum += n % 10;
        n /= 10;
    }
    return original % digitSum == 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$ because we are essentially iterating over the digits of `n`, and the number of digits in `n` is proportional to $\log n$.
> - **Space Complexity:** $O(1)$ because we are using a constant amount of space to store the sum of the digits and the original number.
> - **Why these complexities occur:** The time complexity is due to the while loop that iterates over each digit of `n`, and the space complexity is constant because we only use a fixed amount of space regardless of the size of `n`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach. The definition of a Harshad number directly leads to a straightforward algorithm.
- Detailed breakdown of the approach: Same as the brute force approach because the initial solution is already optimal for this problem.
- Proof of optimality: This approach is optimal because it must check each digit of `n` at least once to calculate the sum of the digits and then check divisibility, which matches the lower bound of $\Omega(\log n)$ due to the need to examine each digit.
- Why further optimization is impossible: Further optimization is not possible because we must examine each digit at least once, and our current approach does so in a single pass.

```cpp
bool isHarshad(int n) {
    int digitSum = 0;
    int original = n;
    while (n > 0) {
        digitSum += n % 10;
        n /= 10;
    }
    return original % digitSum == 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$
> - **Space Complexity:** $O(1)$
> - **Optimality proof:** The algorithm is optimal because it checks each digit exactly once, which is necessary to compute the sum of the digits and then check for divisibility, matching the problem's inherent time complexity lower bound.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over digits of a number, basic arithmetic operations.
- Problem-solving patterns identified: Direct implementation of a problem's definition can often lead to an efficient solution.
- Optimization techniques learned: Recognizing when a straightforward approach is already optimal.
- Similar problems to practice: Other problems involving properties of numbers and basic arithmetic operations.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases (e.g., single-digit numbers), incorrect calculation of digit sum.
- Edge cases to watch for: Numbers with leading zeros (though not applicable here since we're dealing with integers), single-digit numbers.
- Performance pitfalls: Unnecessary iterations or operations.
- Testing considerations: Ensure to test with numbers of varying lengths and properties (e.g., prime numbers, numbers with repeated digits).