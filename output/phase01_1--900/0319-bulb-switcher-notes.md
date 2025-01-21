## Bulb Switcher
**Problem Link:** https://leetcode.com/problems/bulb-switcher/description

**Problem Statement:**
- Input format and constraints: The problem asks to find the number of bulbs that are on after `n` rounds of flipping, where `n` is the number of bulbs.
- Expected output format: The number of bulbs that are on after `n` rounds.
- Key requirements and edge cases to consider: The key requirement is to understand the pattern of bulb switching. Each bulb is switched on or off based on the number of factors it has. A bulb is switched on if it has an odd number of factors, and it is switched off if it has an even number of factors.
- Example test cases with explanations:
  - For `n = 3`, the bulbs are switched as follows:
    1. Round 1: Bulb 1, 2, 3 are switched on.
    2. Round 2: Bulb 2 is switched off.
    3. Round 3: Bulb 3 is switched off.
    The final state is: Bulb 1 is on.
  - For `n = 4`, the bulbs are switched as follows:
    1. Round 1: Bulb 1, 2, 3, 4 are switched on.
    2. Round 2: Bulb 2, 4 are switched off.
    3. Round 3: Bulb 3 is switched off.
    4. Round 4: Bulb 4 is switched on.
    The final state is: Bulb 1, 4 are on.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought process is to simulate the switching of bulbs for each round.
- Step-by-step breakdown of the solution:
  1. Initialize an array of size `n` to represent the state of the bulbs.
  2. For each round `i`, iterate over the bulbs and switch the bulb at index `j` if `j` is a multiple of `i`.
  3. After `n` rounds, count the number of bulbs that are on.
- Why this approach comes to mind first: This approach comes to mind first because it directly simulates the problem statement.

```cpp
class Solution {
public:
    int bulbSwitch(int n) {
        vector<bool> bulbs(n, false);
        for (int i = 1; i <= n; i++) {
            for (int j = i - 1; j < n; j += i) {
                bulbs[j] = !bulbs[j];
            }
        }
        int count = 0;
        for (bool bulb : bulbs) {
            if (bulb) count++;
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because we have two nested loops, each of which runs up to `n` times.
> - **Space Complexity:** $O(n)$ because we need to store the state of `n` bulbs.
> - **Why these complexities occur:** These complexities occur because we are simulating the switching of bulbs for each round, which requires iterating over the bulbs for each round.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to realize that a bulb is switched on if it has an odd number of factors, and it is switched off if it has an even number of factors. A number has an odd number of factors if and only if it is a perfect square.
- Detailed breakdown of the approach:
  1. Initialize a counter for the number of bulbs that are on.
  2. Iterate from 1 to `n` and check if the number is a perfect square.
  3. If the number is a perfect square, increment the counter.
- Proof of optimality: This approach is optimal because it directly counts the number of perfect squares up to `n`, which is the number of bulbs that are on after `n` rounds.
- Why further optimization is impossible: Further optimization is impossible because we need to check each number up to `n` to determine if it is a perfect square.

```cpp
class Solution {
public:
    int bulbSwitch(int n) {
        int count = 0;
        for (int i = 1; i * i <= n; i++) {
            count++;
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\sqrt{n})$ because we only need to iterate up to the square root of `n` to check for perfect squares.
> - **Space Complexity:** $O(1)$ because we only need a constant amount of space to store the counter.
> - **Optimality proof:** This approach is optimal because it directly counts the number of perfect squares up to `n`, which is the number of bulbs that are on after `n` rounds.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of perfect squares and the insight that a number has an odd number of factors if and only if it is a perfect square.
- Problem-solving patterns identified: The problem identifies the pattern of switching bulbs based on the number of factors.
- Optimization techniques learned: The problem teaches the technique of optimizing the solution by directly counting the number of perfect squares up to `n`.
- Similar problems to practice: Similar problems to practice include finding the number of perfect squares up to a given number, finding the number of factors of a given number, and optimizing solutions by identifying key insights.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to iterate over all numbers up to `n` to check for perfect squares, which has a time complexity of $O(n)$.
- Edge cases to watch for: An edge case to watch for is when `n` is 0, in which case the function should return 0.
- Performance pitfalls: A performance pitfall is to use a brute force approach, which has a time complexity of $O(n^2)$.
- Testing considerations: Testing considerations include testing the function with different values of `n`, including edge cases such as 0 and 1.