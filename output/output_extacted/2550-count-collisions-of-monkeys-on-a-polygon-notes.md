## Count Collisions of Monkeys on a Polygon

**Problem Link:** https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/description

**Problem Statement:**
- Input format: An integer `n` representing the number of monkeys and an integer `t` representing the time after which the collision count is required.
- Constraints: `3 <= n <= 1000` and `1 <= t <= 10^6`.
- Expected output format: The number of collisions after `t` time units.
- Key requirements: Calculate the number of collisions between monkeys moving in a circular fashion.
- Edge cases: Consider the cases where `t` is less than `n`, equal to `n`, or greater than `n`.

### Brute Force Approach

**Explanation:**
- The initial thought process involves simulating the movement of each monkey over time `t`.
- For each time unit, check if any two monkeys collide.
- This approach comes to mind first because it directly simulates the scenario described in the problem.

```cpp
int countCollisions(int n, int t) {
    // Initialize an array to represent the positions of the monkeys
    int positions[n];
    for (int i = 0; i < n; i++) {
        positions[i] = i;
    }

    int collisions = 0;
    for (int time = 0; time < t; time++) {
        // Simulate the movement of each monkey
        for (int i = 0; i < n; i++) {
            // Move the monkey to the next position
            positions[i] = (positions[i] + 1) % n;
        }

        // Check for collisions
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (positions[i] == positions[j]) {
                    collisions++;
                }
            }
        }
    }

    return collisions;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(t \cdot n^2)$ because for each time unit, we check all pairs of monkeys for collisions.
> - **Space Complexity:** $O(n)$ because we need to store the positions of all monkeys.
> - **Why these complexities occur:** The brute force approach involves nested loops over time and pairs of monkeys, leading to high time complexity. The space complexity is linear because we only store the positions of the monkeys.

### Optimal Approach (Required)

**Explanation:**
- The key insight is recognizing that the pattern of collisions repeats after a certain period.
- For `n` monkeys, the pattern repeats every `n` time units because each monkey returns to its original position after `n` moves.
- We can calculate the total number of collisions in one period and then scale it according to the given time `t`.

```cpp
int countCollisions(int n, int t) {
    if (t < n) {
        // Calculate collisions for the given time
        int collisions = 0;
        for (int time = 0; time < t; time++) {
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    if ((i + time + 1) % n == (j + time + 1) % n) {
                        collisions++;
                    }
                }
            }
        }
        return collisions;
    } else {
        // Calculate collisions for one period and scale
        int collisionsInPeriod = 0;
        for (int time = 0; time < n; time++) {
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    if ((i + time + 1) % n == (j + time + 1) % n) {
                        collisionsInPeriod++;
                    }
                }
            }
        }
        int fullPeriods = t / n;
        int remainingTime = t % n;
        return fullPeriods * collisionsInPeriod + countCollisions(n, remainingTime);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ because in the worst case, we calculate collisions for one period.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it takes advantage of the periodic nature of the problem, reducing the time complexity significantly compared to the brute force approach.

### Final Notes

**Learning Points:**
- Recognizing periodic patterns in problems can significantly reduce computational complexity.
- Understanding the problem's constraints and edge cases is crucial for developing an efficient solution.
- Recursive or divide-and-conquer approaches can be effective for problems with periodic or repetitive structures.

**Mistakes to Avoid:**
- Not considering the periodic nature of the problem, leading to unnecessary complexity.
- Failing to handle edge cases properly, such as when `t` is less than `n`.
- Not optimizing the solution for the given constraints, leading to inefficient use of resources.