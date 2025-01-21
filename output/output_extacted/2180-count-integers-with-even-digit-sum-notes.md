## Count Integers with Even Digit Sum

**Problem Link:** https://leetcode.com/problems/count-integers-with-even-digit-sum/description

**Problem Statement:**
- Input: An integer `limit`.
- Constraints: $1 \leq limit \leq 10^4$.
- Expected output: The number of integers between 1 and `limit` (inclusive) whose digit sum is even.
- Key requirements and edge cases to consider:
  - Handling numbers with varying numbers of digits.
  - Calculating the sum of digits for each number.
  - Determining if the digit sum is even.
- Example test cases with explanations:
  - For `limit = 4`, the integers with even digit sums are 2 and 4, so the output is 2.
  - For `limit = 30`, we need to calculate the digit sum for each integer from 1 to 30 and count those with even sums.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all integers from 1 to `limit`, calculate the digit sum for each, and count those with even sums.
- Step-by-step breakdown of the solution:
  1. Loop through each integer `i` from 1 to `limit`.
  2. For each `i`, calculate its digit sum by converting `i` to a string, iterating through each character (digit), converting it back to an integer, and summing them up.
  3. Check if the digit sum is even by using the modulo operator (`%`). If the remainder when divided by 2 is 0, the sum is even.
  4. Increment a counter for each integer with an even digit sum.
- Why this approach comes to mind first: It directly addresses the problem by checking every possible integer within the given range.

```cpp
int countEven(int limit) {
    int count = 0;
    for (int i = 1; i <= limit; i++) {
        int digitSum = 0;
        int num = i;
        while (num > 0) {
            digitSum += num % 10;
            num /= 10;
        }
        if (digitSum % 2 == 0) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the limit and $m$ is the average number of digits in the numbers up to the limit. This is because for each number, we are potentially iterating through its digits.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store our variables.
> - **Why these complexities occur:** The time complexity is linear with respect to the limit because we are checking each number once. The space complexity is constant because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Recognize that the digit sum's parity (even or odd) only depends on the parity of the number of odd digits. This insight allows for a more direct calculation without needing to explicitly sum digits for each number.
- Detailed breakdown of the approach:
  1. Initialize a counter for integers with even digit sums.
  2. Iterate through all integers from 1 to `limit`.
  3. For each integer, calculate its digit sum's parity by counting the number of odd digits.
  4. If the count of odd digits is even, the digit sum is even, so increment the counter.
- Proof of optimality: This approach is optimal because it minimizes the number of operations required to determine the parity of the digit sum for each integer, thus achieving the best possible time complexity for this problem.

```cpp
int countEven(int limit) {
    int count = 0;
    for (int i = 1; i <= limit; i++) {
        int oddDigitCount = 0;
        int num = i;
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 != 0) {
                oddDigitCount++;
            }
            num /= 10;
        }
        if (oddDigitCount % 2 == 0) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, similar to the brute force approach, where $n$ is the limit and $m$ is the average number of digits. However, this approach might be slightly more efficient in practice due to its simpler calculation.
> - **Space Complexity:** $O(1)$, as we are still using a constant amount of space.
> - **Optimality proof:** The time complexity is optimal for this problem because we must at least look at each number once to determine its digit sum's parity. The space complexity is also optimal as we only need a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checking, and basic arithmetic operations.
- Problem-solving patterns identified: The importance of understanding the problem's constraints and the properties of numbers (e.g., parity).
- Optimization techniques learned: Simplifying calculations and minimizing the number of operations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect loop conditions, forgetting to reset variables, and off-by-one errors.
- Edge cases to watch for: Numbers with leading zeros (though not applicable in this integer context), and the special case of the number 0 itself.
- Performance pitfalls: Using overly complex data structures or algorithms for a simple problem.
- Testing considerations: Ensure to test with a variety of inputs, including edge cases like 1, a small number, and the maximum limit.