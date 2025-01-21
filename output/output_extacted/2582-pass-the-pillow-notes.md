## Pass the Pillow
**Problem Link:** https://leetcode.com/problems/pass-the-pillow/description

**Problem Statement:**
- Input format and constraints: The problem involves a list of `n` friends and `m` rounds. Each round consists of passing a pillow to the next person in a specific sequence.
- Expected output format: Determine the person who ends up with the pillow after `m` rounds.
- Key requirements and edge cases to consider: The sequence in which the pillow is passed is determined by the `n` friends, and the pillow is passed in a circular manner. If a friend is skipped due to the sequence, they are removed from the circle.
- Example test cases with explanations: For example, if there are 4 friends and 2 rounds, the pillow will be passed to the next person in the sequence for each round.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to simulate the passing of the pillow for each round. We can use a queue to keep track of the friends and the pillow's current position.
- Step-by-step breakdown of the solution:
  1. Initialize a queue with the `n` friends.
  2. For each round, remove the friend at the front of the queue and add them to the back of the queue (since the pillow is passed in a circular manner).
  3. Repeat step 2 for `m` rounds.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be efficient for large inputs.

```cpp
#include <queue>
using namespace std;

int passThePillow(int n, int m) {
    queue<int> q;
    for (int i = 1; i <= n; i++) {
        q.push(i);
    }
    for (int i = 0; i < m; i++) {
        q.push(q.front());
        q.pop();
    }
    return q.front();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$, where $m$ is the number of rounds. This is because we perform a constant amount of work for each round.
> - **Space Complexity:** $O(n)$, where $n$ is the number of friends. This is because we store all the friends in the queue.
> - **Why these complexities occur:** The time complexity is linear because we simulate each round individually, and the space complexity is linear because we store all the friends in the queue.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is that the pillow will always end up with the friend who is `m % n` positions ahead of the initial position.
- Detailed breakdown of the approach:
  1. Calculate `m % n` to determine the number of positions to move the pillow.
  2. Return the friend who is at the resulting position.
- Proof of optimality: This approach is optimal because it eliminates the need to simulate each round individually. Instead, we can calculate the final position directly.
- Why further optimization is impossible: This approach is already optimal because it has a constant time complexity.

```cpp
int passThePillow(int n, int m) {
    return (m % n) + 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, where $n$ is the number of friends and $m$ is the number of rounds. This is because we perform a constant amount of work.
> - **Space Complexity:** $O(1)$, where $n$ is the number of friends and $m$ is the number of rounds. This is because we use a constant amount of space.
> - **Optimality proof:** The time complexity is constant because we calculate the final position directly, and the space complexity is constant because we use a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of modular arithmetic and the importance of finding patterns in problems.
- Problem-solving patterns identified: The problem requires identifying a pattern in the sequence of pillow passing and using it to optimize the solution.
- Optimization techniques learned: The problem teaches the importance of eliminating unnecessary work and using mathematical insights to optimize solutions.
- Similar problems to practice: Other problems that involve finding patterns and using modular arithmetic, such as the "Josephus Problem".

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as when `n` or `m` is zero.
- Edge cases to watch for: The problem has edge cases when `n` or `m` is zero, and the solution should handle these cases correctly.
- Performance pitfalls: The brute force approach can be slow for large inputs, and the optimal approach should be used instead.
- Testing considerations: The solution should be tested with different inputs, including edge cases, to ensure it works correctly.