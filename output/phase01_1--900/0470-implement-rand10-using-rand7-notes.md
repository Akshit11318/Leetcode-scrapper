## Implement Rand10 Using Rand7

**Problem Link:** https://leetcode.com/problems/implement-rand10-using-rand7/description

**Problem Statement:**
- Input: `rand7()` function which returns a random integer from 1 to 7 with uniform probability.
- Output: Implement `rand10()` function which returns a random integer from 1 to 10 with uniform probability.
- Key requirements and edge cases to consider:
  - The `rand7()` function is the only source of randomness.
  - The output of `rand10()` should have uniform probability distribution.
- Example test cases:
  - `rand10()` should return integers from 1 to 10 with equal probability.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves using `rand7()` to generate a large number of random integers and then taking the modulus to reduce it to the range of 1 to 10. However, this approach does not guarantee uniform distribution.
- Step-by-step breakdown:
  1. Generate a large number by concatenating the results of multiple `rand7()` calls.
  2. Take the modulus of the generated number to bring it within the range of 1 to 10.
- Why this approach comes to mind first: It's a straightforward way to try and utilize `rand7()` to generate a number within a different range.

```cpp
int rand10() {
    int result = 0;
    int multiplier = 1;
    for (int i = 0; i < 4; i++) {
        result += rand7() * multiplier;
        multiplier *= 7;
    }
    return (result % 10) + 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of times `rand7()` is called. In this case, $n = 4$.
> - **Space Complexity:** $O(1)$, as only a constant amount of space is used.
> - **Why these complexities occur:** The time complexity is due to the loop that calls `rand7()` multiple times, and the space complexity is constant because only a fixed amount of space is used to store variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: To achieve uniform distribution, we can use the property that if we generate a number in a larger range (e.g., 1 to 49) uniformly, we can then map it to a smaller range (1 to 10) while preserving uniformity.
- Detailed breakdown:
  1. Generate a number between 1 and 49 (7*7) by calling `rand7()` twice.
  2. If the generated number is between 1 and 40 (inclusive), map it to a number between 1 and 10 by taking the modulus and adjusting.
  3. If the generated number is outside the range of 1 to 40, discard it and repeat the process.
- Proof of optimality: This approach ensures that each number from 1 to 10 has an equal chance of being selected, as we're effectively generating numbers in a larger space and then mapping them uniformly to the smaller space.

```cpp
int rand10() {
    int num;
    do {
        num = (rand7() - 1) * 7 + rand7();
    } while (num > 40);
    return (num - 1) / 4 + 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ in terms of the number of operations, but it can vary due to the potential for repeated calls to `rand7()` in the worst case. The expected number of calls to `rand7()` can be calculated as $E[T] = 1 / P(\text{success})$, where $P(\text{success})$ is the probability of generating a number within the desired range on a single try. Here, $P(\text{success}) = 40/49$, so $E[T] = 49/40$.
> - **Space Complexity:** $O(1)$, as only a constant amount of space is used.
> - **Optimality proof:** The approach is optimal because it minimizes the number of calls to `rand7()` while ensuring a uniform distribution of the output.

---

### Final Notes

**Learning Points:**
- The importance of ensuring uniform distribution when generating random numbers.
- Using a larger range to achieve uniformity and then mapping to a smaller range.
- Understanding the trade-offs between different approaches, including the potential for repeated operations.

**Mistakes to Avoid:**
- Directly using the result of `rand7()` without ensuring uniform distribution.
- Not considering the potential for repeated operations and their impact on performance.
- Failing to validate the output distribution of the implemented `rand10()` function.