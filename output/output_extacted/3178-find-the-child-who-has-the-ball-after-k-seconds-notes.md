## Find the Child Who Has the Ball After K Seconds

**Problem Link:** https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/description

**Problem Statement:**
- Input format and constraints: The problem involves a circular queue of `n` children and a ball that moves `k` steps after each child touches the ball. The task is to find which child will have the ball after `k` seconds.
- Expected output format: The index of the child who has the ball after `k` seconds.
- Key requirements and edge cases to consider: The input `n` and `k` will be positive integers, and we need to consider the circular nature of the queue.
- Example test cases with explanations:
  - If `n = 4` and `k = 2`, the ball will move to the child at index 2 after the first second and to the child at index 0 after the second second.
  - If `n = 3` and `k = 3`, the ball will move to the child at index 0 after the first second, to the child at index 1 after the second second, and to the child at index 2 after the third second.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can simulate the movement of the ball by iterating `k` times and updating the index of the child who has the ball at each step.
- Step-by-step breakdown of the solution:
  1. Initialize the index of the child who has the ball to 0.
  2. Iterate `k` times.
  3. At each iteration, update the index of the child who has the ball by adding 1 to the current index and taking the modulus of the result with `n` to ensure the index wraps around to the beginning of the queue when it exceeds `n-1`.
- Why this approach comes to mind first: It is a straightforward way to simulate the movement of the ball and does not require any advanced mathematical concepts.

```cpp
class Solution {
public:
    int findTheChild(int n, int k) {
        int index = 0;
        for (int i = 0; i < k; i++) {
            index = (index + 1) % n;
        }
        return index;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(k)$, where $k$ is the number of seconds. This is because we iterate `k` times to simulate the movement of the ball.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the index of the child who has the ball.
> - **Why these complexities occur:** The time complexity is linear with respect to $k$ because we iterate `k` times, and the space complexity is constant because we only use a fixed amount of space to store the index of the child who has the ball.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the final index of the child who has the ball directly using the formula `(k % n)`.
- Detailed breakdown of the approach:
  1. Calculate the final index of the child who has the ball using the formula `(k % n)`.
- Proof of optimality: This approach is optimal because it eliminates the need for iteration and directly calculates the final index of the child who has the ball.
- Why further optimization is impossible: This approach has a constant time complexity and uses a constant amount of space, making it impossible to further optimize.

```cpp
class Solution {
public:
    int findTheChild(int n, int k) {
        return (k % n);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we directly calculate the final index of the child who has the ball using a constant-time operation.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the result.
> - **Optimality proof:** This approach is optimal because it has a constant time complexity and uses a constant amount of space, making it the most efficient possible solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of circular queues and the use of the modulus operator to wrap around to the beginning of the queue.
- Problem-solving patterns identified: The problem illustrates the importance of identifying patterns and using mathematical insights to optimize solutions.
- Optimization techniques learned: The problem demonstrates the use of mathematical formulas to eliminate iteration and optimize solutions.
- Similar problems to practice: Other problems that involve circular queues and modulus operations, such as the "Josephus Problem".

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as when `n` or `k` is 0.
- Edge cases to watch for: The problem requires handling the case where `n` or `k` is 0, as well as the case where `k` is greater than `n`.
- Performance pitfalls: Using iteration to simulate the movement of the ball can lead to poor performance for large values of `k`.
- Testing considerations: The problem requires testing with different values of `n` and `k` to ensure that the solution works correctly in all cases.