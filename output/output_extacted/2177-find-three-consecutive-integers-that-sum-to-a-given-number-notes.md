## Find Three Consecutive Integers That Sum to a Given Number
**Problem Link:** https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/description

**Problem Statement:**
- Input format and constraints: Given an integer `num`, return three consecutive integers (as a sorted array) that sum up to `num`. If there are many such answers, return any of them.
- Expected output format: A sorted array of three consecutive integers.
- Key requirements and edge cases to consider: The input `num` can be any integer, and we need to find three consecutive integers that sum up to `num`. If no such integers exist, we should return an empty array.
- Example test cases with explanations:
  - Input: `num = 33`
    - Output: `[10, 11, 12]`
    - Explanation: `10 + 11 + 12 = 33`
  - Input: `num = 5`
    - Output: `[]`
    - Explanation: No three consecutive integers sum up to 5.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by checking all possible combinations of three consecutive integers.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible starting numbers for the sequence of three consecutive integers.
  2. For each starting number, calculate the sum of the three consecutive integers.
  3. If the sum matches the given number, return the three consecutive integers.
- Why this approach comes to mind first: It's a straightforward and intuitive approach, but it's not efficient for large inputs.

```cpp
vector<int> sumOfThree(int num) {
    for (int i = -1000; i <= 1000; i++) {
        if (i + (i + 1) + (i + 2) == num) {
            return {i, i + 1, i + 2};
        }
    }
    return {};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the range of possible starting numbers. In this case, $n = 2001$.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the result.
> - **Why these complexities occur:** The time complexity is linear because we iterate over all possible starting numbers, and the space complexity is constant because we only use a fixed amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the formula for the sum of an arithmetic series to find the middle number of the sequence.
- Detailed breakdown of the approach:
  1. Let $x$ be the middle number of the sequence. Then, the three consecutive integers are $x - 1$, $x$, and $x + 1$.
  2. The sum of these three consecutive integers is $3x$, which must be equal to the given number.
  3. Therefore, we can calculate $x$ by dividing the given number by 3.
  4. If $x$ is an integer, we can return the three consecutive integers. Otherwise, we return an empty array.
- Proof of optimality: This approach is optimal because it only requires a constant amount of time and space, regardless of the input size.

```cpp
vector<int> sumOfThree(int num) {
    if (num % 3 != 0) {
        return {};
    }
    int x = num / 3;
    return {x - 1, x, x + 1};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we only perform a constant number of operations.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the result.
> - **Optimality proof:** This approach is optimal because it only requires a constant amount of time and space, regardless of the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Arithmetic series, division, and modulo operations.
- Problem-solving patterns identified: Using mathematical formulas to simplify the problem and reduce the time complexity.
- Optimization techniques learned: Avoiding unnecessary iterations and using constant-time operations.
- Similar problems to practice: Other problems that involve arithmetic series, such as finding the sum of a sequence or determining if a number is a perfect square.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check for integer division or using the wrong data type.
- Edge cases to watch for: Handling cases where the input number is not divisible by 3 or is outside the range of possible starting numbers.
- Performance pitfalls: Using inefficient algorithms or data structures that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the code with different input values, including edge cases and boundary values.