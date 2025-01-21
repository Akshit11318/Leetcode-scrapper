## Count Odd Numbers in an Interval Range

**Problem Link:** https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description

**Problem Statement:**
- Input format and constraints: The problem takes two integers, `low` and `high`, as input, where `1 <= low <= high <= 10^9`.
- Expected output format: The function should return the number of odd integers in the range `[low, high]`.
- Key requirements and edge cases to consider: The range is inclusive, and the input numbers are guaranteed to be positive integers.
- Example test cases with explanations: 
    - For `low = 3` and `high = 7`, the output should be `3` because there are three odd numbers in this range: `3`, `5`, and `7`.
    - For `low = 2` and `high = 2`, the output should be `0` because `2` is an even number.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to solve this problem is to iterate through all numbers in the given range and count the odd numbers.
- Step-by-step breakdown of the solution: 
    1. Start from `low`.
    2. For each number in the range, check if it is odd by using the modulus operator (`%`). If the remainder of the division by `2` is not `0`, then the number is odd.
    3. Increment a counter for each odd number found.
    4. Continue until `high` is reached.
- Why this approach comes to mind first: It directly addresses the problem statement by checking each number in the range.

```cpp
int countOdds(int low, int high) {
    int count = 0;
    for (int i = low; i <= high; i++) {
        if (i % 2 != 0) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of integers in the range `[low, high]`. This is because in the worst case, we have to iterate through every number in the range.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the count and the loop variable.
> - **Why these complexities occur:** The time complexity is linear because of the iteration through the range, and the space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Recognize that the number of odd integers in a range can be calculated directly without needing to iterate through each number. 
- Detailed breakdown of the approach: 
    1. Calculate the total number of integers in the range.
    2. Since every other number is odd, we can find the number of odd numbers by dividing the total count by `2` and then adjusting based on whether the start or end (or both) of the range is odd.
- Proof of optimality: This approach is optimal because it reduces the problem to a simple arithmetic calculation, avoiding the need for iteration.
- Why further optimization is impossible: We cannot avoid calculating the number of odd integers in fewer steps than this because we must at least consider the start and end of the range.

```cpp
int countOdds(int low, int high) {
    return (high + 1) / 2 - low / 2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because the calculation involves a constant number of operations regardless of the input size.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it achieves a constant time complexity, which is the lowest possible time complexity for any algorithm.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Direct calculation, avoidance of unnecessary iteration.
- Problem-solving patterns identified: Looking for patterns or mathematical relationships that allow for direct computation.
- Optimization techniques learned: Reducing iteration by identifying mathematical shortcuts.
- Similar problems to practice: Other problems involving ranges or sequences where direct calculation might be applicable.

**Mistakes to Avoid:**
- Common implementation errors: Not considering the inclusivity of the range, misinterpreting the problem statement.
- Edge cases to watch for: When `low` and `high` are the same, or when one of them is an odd or even number.
- Performance pitfalls: Using iteration when a direct calculation is possible.
- Testing considerations: Ensure to test with various ranges, including those starting or ending with odd or even numbers, and ranges of different sizes.