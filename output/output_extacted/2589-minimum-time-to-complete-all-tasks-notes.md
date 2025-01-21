## Minimum Time to Complete All Tasks

**Problem Link:** https://leetcode.com/problems/minimum-time-to-complete-all-tasks/description

**Problem Statement:**
- Input format: An array of integers `tasks` representing the time required to complete each task, and an integer `sessionTime` representing the maximum time allowed per session.
- Constraints: $1 \leq \text{tasks.length} \leq 14$, $1 \leq \text{tasks[i]} \leq 10$, $1 \leq \text{sessionTime} \leq 15$.
- Expected output format: The minimum number of sessions required to complete all tasks.
- Key requirements and edge cases to consider:
  - Tasks can be completed in any order.
  - Each session must be fully utilized before starting the next session.
- Example test cases with explanations:
  - Input: `tasks = [2,3,3], sessionTime = 4`, Output: `4`.
  - Input: `tasks = [10], sessionTime = 10`, Output: `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of tasks in each session and calculate the total number of sessions required.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of tasks.
  2. For each combination, calculate the total time required.
  3. If the total time is less than or equal to the session time, add the tasks to the current session.
  4. Otherwise, start a new session.
- Why this approach comes to mind first: It is a straightforward approach that considers all possible scenarios.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int minSessions(std::vector<int>& tasks, int sessionTime) {
    std::sort(tasks.rbegin(), tasks.rend());
    int n = tasks.size();
    int ans = n;
    for (int mask = 0; mask < (1 << n); mask++) {
        int sessions = 0;
        int time = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                time += tasks[i];
                if (time > sessionTime) {
                    sessions++;
                    time = tasks[i];
                }
            }
        }
        if (time > 0) sessions++;
        ans = std::min(ans, sessions);
    }
    return ans;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of tasks.
> - **Space Complexity:** $O(1)$, excluding the space required for the input and output.
> - **Why these complexities occur:** The time complexity occurs because we are generating all possible combinations of tasks and calculating the total time for each combination. The space complexity is constant because we are only using a fixed amount of space to store the input and output.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a bitmask to represent the tasks that are completed in each session.
- Detailed breakdown of the approach:
  1. Initialize the minimum number of sessions to the number of tasks.
  2. Iterate over all possible bitmasks.
  3. For each bitmask, calculate the total time required for the tasks represented by the bitmask.
  4. If the total time is less than or equal to the session time, update the minimum number of sessions.
- Proof of optimality: This approach is optimal because it considers all possible combinations of tasks and sessions.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int minSessions(std::vector<int>& tasks, int sessionTime) {
    std::sort(tasks.rbegin(), tasks.rend());
    int n = tasks.size();
    int ans = n;
    for (int mask = 1; mask < (1 << n); mask++) {
        int time = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                time += tasks[i];
            }
        }
        if (time <= sessionTime) {
            ans = std::min(ans, __builtin_popcount(mask));
        }
    }
    return ans;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of tasks.
> - **Space Complexity:** $O(1)$, excluding the space required for the input and output.
> - **Optimality proof:** This approach is optimal because it considers all possible combinations of tasks and sessions.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bitmasking, iteration over all possible combinations.
- Problem-solving patterns identified: Using a bitmask to represent tasks and sessions.
- Optimization techniques learned: Using a bitmask to reduce the number of iterations.

**Mistakes to Avoid:**
- Common implementation errors: Not considering all possible combinations of tasks and sessions.
- Edge cases to watch for: When the total time required for a task is greater than the session time.
- Performance pitfalls: Not using a bitmask to reduce the number of iterations.
- Testing considerations: Test the code with different inputs and edge cases to ensure correctness.