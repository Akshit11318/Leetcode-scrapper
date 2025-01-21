## Employee Task Duration and Concurrent Tasks

**Problem Link:** https://leetcode.com/problems/employee-task-duration-and-concurrent-tasks/description

**Problem Statement:**
- Input: A list of tasks with their durations and a limit on the number of concurrent tasks.
- Constraints: Each task is represented as a pair of integers, where the first integer is the task ID and the second integer is the task duration.
- Expected Output: The maximum number of tasks that can be completed within the given time limit.
- Key Requirements: Find the maximum number of tasks that can be completed by multiple employees working concurrently, given the task durations and the limit on the number of concurrent tasks.
- Example Test Cases:
  - Input: `tasks = [[1, 2], [2, 3], [3, 1]]`, `limit = 3`, `time = 4`
  - Output: `3`
  - Explanation: The tasks can be completed in the following order: Task 3 (duration 1) can be completed by one employee, while Task 1 (duration 2) and Task 2 (duration 3) can be completed by two other employees, within the given time limit of 4.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of tasks and checking if they can be completed within the given time limit.
- Step-by-step breakdown:
  1. Generate all possible combinations of tasks.
  2. For each combination, calculate the total time required to complete all tasks.
  3. Check if the total time is within the given time limit.
  4. If it is, update the maximum number of tasks that can be completed.
- This approach comes to mind first because it is a straightforward way to solve the problem, but it has a high time complexity due to the generation of all possible combinations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxTasks(std::vector<std::vector<int>>& tasks, int limit, int time) {
    int maxTasks = 0;
    int n = tasks.size();
    for (int i = 1; i <= n; i++) {
        // Generate all possible combinations of tasks
        for (int mask = 0; mask < (1 << n); mask++) {
            if (__builtin_popcount(mask) == i) {
                int totalTime = 0;
                for (int j = 0; j < n; j++) {
                    if ((mask & (1 << j)) != 0) {
                        totalTime += tasks[j][1];
                    }
                }
                // Check if the total time is within the given time limit
                if (totalTime <= time) {
                    maxTasks = std::max(maxTasks, i);
                }
            }
        }
    }
    return maxTasks;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of tasks. This is because we generate all possible combinations of tasks and calculate the total time for each combination.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum number of tasks and the total time.
> - **Why these complexities occur:** The high time complexity occurs because we generate all possible combinations of tasks, which has an exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a priority queue to store the tasks that can be completed within the given time limit.
- Detailed breakdown:
  1. Sort the tasks by their durations in ascending order.
  2. Initialize a priority queue to store the tasks that can be completed within the given time limit.
  3. Iterate through the sorted tasks and add them to the priority queue if the total time is within the given time limit.
  4. If the priority queue has more tasks than the limit on the number of concurrent tasks, remove the task with the longest duration from the queue.
- This approach is optimal because it ensures that we always complete the tasks with the shortest durations first, which maximizes the number of tasks that can be completed within the given time limit.

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

int maxTasks(std::vector<std::vector<int>>& tasks, int limit, int time) {
    std::sort(tasks.begin(), tasks.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[1] < b[1];
    });
    int maxTasks = 0;
    std::priority_queue<int> pq;
    int totalTime = 0;
    for (const auto& task : tasks) {
        if (pq.size() < limit) {
            pq.push(task[1]);
            totalTime += task[1];
            maxTasks++;
        } else if (task[1] < pq.top()) {
            totalTime -= pq.top();
            pq.pop();
            pq.push(task[1]);
            totalTime += task[1];
        }
        if (totalTime > time) {
            break;
        }
    }
    return maxTasks;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of tasks. This is because we sort the tasks and use a priority queue to store the tasks that can be completed within the given time limit.
> - **Space Complexity:** $O(n)$, as we use a priority queue to store the tasks that can be completed within the given time limit.
> - **Optimality proof:** This approach is optimal because it ensures that we always complete the tasks with the shortest durations first, which maximizes the number of tasks that can be completed within the given time limit.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, priority queues, and greedy algorithms.
- Problem-solving patterns identified: using a priority queue to store tasks that can be completed within a given time limit.
- Optimization techniques learned: sorting tasks by their durations and using a priority queue to store the tasks that can be completed within the given time limit.

**Mistakes to Avoid:**
- Common implementation errors: not checking if the total time is within the given time limit before adding a task to the priority queue.
- Edge cases to watch for: when the limit on the number of concurrent tasks is 1, we should only consider the tasks with the shortest durations.
- Performance pitfalls: using a brute force approach that generates all possible combinations of tasks, which has a high time complexity.
- Testing considerations: testing the algorithm with different inputs and edge cases to ensure that it produces the correct output.