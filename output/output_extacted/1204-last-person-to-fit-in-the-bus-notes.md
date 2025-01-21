## Last Person to Fit in the Bus

**Problem Link:** https://leetcode.com/problems/last-person-to-fit-in-the-bus/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `n` representing the number of people and an integer `m` representing the capacity of the bus.
- Expected output format: The function should return the last person to fit in the bus.
- Key requirements and edge cases to consider: The bus can only hold `m` people, and the function should return the last person to fit in the bus.
- Example test cases with explanations: For example, if `n = 5` and `m = 3`, the function should return `3`, because the last person to fit in the bus is the third person.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by iterating over each person and checking if the bus is full.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `last_person` to store the last person to fit in the bus.
  2. Iterate over each person from `1` to `n`.
  3. For each person, check if the bus is full by checking if the current person is greater than `m`.
  4. If the bus is not full, update `last_person` to the current person.
  5. If the bus is full, break the loop.
- Why this approach comes to mind first: This approach is simple and straightforward, as it involves iterating over each person and checking if the bus is full.

```cpp
class Solution {
public:
    int lastPersonToFitInBus(int n, int m) {
        int last_person = 0;
        for (int i = 1; i <= n; i++) {
            if (i > m) {
                break;
            }
            last_person = i;
        }
        return last_person;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because we are iterating over each person from `1` to `n`.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the `last_person` variable.
> - **Why these complexities occur:** The time complexity is $O(n)$ because we are iterating over each person, and the space complexity is $O(1)$ because we are only using a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The last person to fit in the bus is simply `m`, because the bus can only hold `m` people.
- Detailed breakdown of the approach:
  1. Return `m` as the last person to fit in the bus.
- Proof of optimality: This approach is optimal because it directly returns the correct answer without any unnecessary computations.
- Why further optimization is impossible: This approach is already optimal because it only involves a single operation.

```cpp
class Solution {
public:
    int lastPersonToFitInBus(int n, int m) {
        return m;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we are only performing a single operation.
> - **Space Complexity:** $O(1)$, because we are not using any extra space.
> - **Optimality proof:** This approach is optimal because it directly returns the correct answer without any unnecessary computations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of understanding the problem constraints and identifying the simplest solution.
- Problem-solving patterns identified: The use of a simple and straightforward approach to solve the problem.
- Optimization techniques learned: The importance of eliminating unnecessary computations to achieve optimal performance.
- Similar problems to practice: Other problems that involve finding the last person to fit in a limited capacity, such as finding the last person to fit in a queue or a stack.

**Mistakes to Avoid:**
- Common implementation errors: Overcomplicating the solution by using unnecessary data structures or algorithms.
- Edge cases to watch for: Ensuring that the solution handles all possible input values, including edge cases such as `n = 0` or `m = 0`.
- Performance pitfalls: Avoiding unnecessary computations and optimizing the solution for performance.
- Testing considerations: Thoroughly testing the solution with different input values to ensure correctness.