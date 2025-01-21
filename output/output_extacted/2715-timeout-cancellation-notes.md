## Timeout Cancellation
**Problem Link:** https://leetcode.com/problems/timeout-cancellation/description

**Problem Statement:**
- Input format: An array of tasks, each task being an array of two integers `[index, time]`.
- Constraints: `1 <= tasks.length <= 10^5`, `1 <= index <= 10^6`, `1 <= time <= 10^6`.
- Expected output format: The index of the task that should be cancelled to minimize the total waiting time.
- Key requirements and edge cases to consider: The goal is to minimize the total waiting time by cancelling one task. The waiting time of a task is the sum of the times of all tasks scheduled before it.
- Example test cases with explanations:
  - `tasks = [[1,2],[2,3],[3,4]]`: The optimal solution is to cancel the task with index 3, resulting in a total waiting time of 2.
  - `tasks = [[1,1],[2,1],[3,1]]`: The optimal solution is to cancel any task, as the total waiting time will be the same.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible cancellations of a task and calculate the resulting total waiting time.
- Step-by-step breakdown of the solution:
  1. Iterate over each task in the array.
  2. For each task, calculate the total waiting time if this task is cancelled.
  3. Keep track of the task that results in the minimum total waiting time.
- Why this approach comes to mind first: It's a straightforward approach that checks all possibilities.

```cpp
int findMinTotalWaitingTime(vector<vector<int>>& tasks) {
    int minWaitingTime = INT_MAX;
    int minIndex = -1;
    int n = tasks.size();
    for (int i = 0; i < n; i++) {
        int waitingTime = 0;
        int time = 0;
        for (int j = 0; j < n; j++) {
            if (i != j) {
                time += tasks[j][1];
                waitingTime += time;
            }
        }
        if (waitingTime < minWaitingTime) {
            minWaitingTime = waitingTime;
            minIndex = tasks[i][0];
        }
    }
    return minIndex;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of tasks. This is because for each task, we're calculating the total waiting time by iterating over all tasks.
> - **Space Complexity:** $O(1)$, as we're using a constant amount of space to store the minimum waiting time and the index of the task that achieves it.
> - **Why these complexities occur:** The time complexity is high because we're using a nested loop to calculate the waiting time for each task. The space complexity is low because we're only using a few variables to store the minimum waiting time and the corresponding index.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can calculate the total waiting time by summing up the times of all tasks scheduled before each task, without actually scheduling the tasks.
- Detailed breakdown of the approach:
  1. Sort the tasks by their times.
  2. Initialize the total waiting time to 0.
  3. Iterate over the sorted tasks, adding the time of each task to the total waiting time, and subtracting the time of the current task from the total waiting time.
  4. Keep track of the task that results in the minimum total waiting time.
- Proof of optimality: This approach is optimal because it calculates the total waiting time in a single pass, without having to try all possible cancellations.

```cpp
int findMinTotalWaitingTime(vector<vector<int>>& tasks) {
    sort(tasks.begin(), tasks.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });
    int minWaitingTime = INT_MAX;
    int minIndex = -1;
    int totalWaitingTime = 0;
    int totalTime = 0;
    for (int i = 0; i < tasks.size(); i++) {
        totalTime += tasks[i][1];
        totalWaitingTime += totalTime - tasks[i][1];
        if (totalWaitingTime < minWaitingTime) {
            minWaitingTime = totalWaitingTime;
            minIndex = tasks[i][0];
        }
    }
    return minIndex;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of tasks. This is because we're sorting the tasks by their times.
> - **Space Complexity:** $O(1)$, as we're using a constant amount of space to store the minimum waiting time and the index of the task that achieves it.
> - **Optimality proof:** This approach is optimal because it calculates the total waiting time in a single pass, without having to try all possible cancellations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, dynamic programming.
- Problem-solving patterns identified: Using a single pass to calculate the total waiting time.
- Optimization techniques learned: Avoiding unnecessary calculations by using a single pass.
- Similar problems to practice: Scheduling problems, dynamic programming problems.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the tasks by their times, not using a single pass to calculate the total waiting time.
- Edge cases to watch for: Tasks with the same time, tasks with a time of 0.
- Performance pitfalls: Using a brute force approach, not using a single pass to calculate the total waiting time.
- Testing considerations: Testing with different inputs, testing with edge cases.