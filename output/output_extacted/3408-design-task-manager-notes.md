## Design Task Manager
**Problem Link:** https://leetcode.com/problems/design-task-manager/description

**Problem Statement:**
- Input format and constraints: The input is a series of operations, including creating tasks, changing task state, and getting task count.
- Expected output format: The output should be the result of the `getTaskCount` operation.
- Key requirements and edge cases to consider: Tasks can be in different states (e.g., "pending", "running", "done"), and the task manager should handle these states correctly.
- Example test cases with explanations:
  - Creating tasks and checking the count.
  - Changing the state of tasks and verifying the count.
  - Handling edge cases such as invalid task IDs or states.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To implement a task manager, we need to keep track of tasks and their states. A straightforward approach is to use a data structure like a map or a list to store tasks.
- Step-by-step breakdown of the solution:
  1. Create a data structure to store tasks.
  2. Implement the `create` operation to add tasks to the data structure.
  3. Implement the `changeState` operation to update the state of tasks.
  4. Implement the `getTaskCount` operation to count tasks based on their state.
- Why this approach comes to mind first: It directly addresses the requirements without considering optimizations.

```cpp
class TaskManager {
public:
    void create(int taskId) {
        tasks[taskId] = "pending";
    }

    void changeState(int taskId, string state) {
        if (tasks.find(taskId) != tasks.end()) {
            tasks[taskId] = state;
        }
    }

    int getTaskCount(string state) {
        int count = 0;
        for (auto& task : tasks) {
            if (task.second == state) {
                count++;
            }
        }
        return count;
    }

private:
    unordered_map<int, string> tasks;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for the `getTaskCount` operation, where $n$ is the number of tasks, because we potentially iterate over all tasks.
> - **Space Complexity:** $O(n)$ for storing tasks, where $n$ is the number of tasks.
> - **Why these complexities occur:** The brute force approach requires iterating over all tasks to count them based on their state, leading to linear time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating over all tasks to count them, we can maintain separate counts for each state as tasks are created and their states are changed.
- Detailed breakdown of the approach:
  1. Use a map to store tasks and their states.
  2. Use another map to store the count of tasks for each state.
  3. Update the count map whenever a task is created or its state is changed.
- Proof of optimality: This approach reduces the time complexity of the `getTaskCount` operation to constant time, which is optimal.

```cpp
class TaskManager {
public:
    void create(int taskId) {
        tasks[taskId] = "pending";
        stateCounts["pending"]++;
    }

    void changeState(int taskId, string state) {
        if (tasks.find(taskId) != tasks.end()) {
            stateCounts[tasks[taskId]]--;
            tasks[taskId] = state;
            stateCounts[state]++;
        }
    }

    int getTaskCount(string state) {
        return stateCounts[state];
    }

private:
    unordered_map<int, string> tasks;
    unordered_map<string, int> stateCounts;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for the `getTaskCount` operation, because we directly access the count for a given state.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of tasks and $m$ is the number of unique states, for storing tasks and state counts.
> - **Optimality proof:** The optimal approach achieves constant time complexity for counting tasks by state, which is the best possible complexity for this operation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using separate data structures to optimize query operations.
- Problem-solving patterns identified: Maintaining aggregate information (like counts) as data changes.
- Optimization techniques learned: Reducing time complexity by avoiding unnecessary iterations.
- Similar problems to practice: Other problems involving maintaining and querying data efficiently.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to update counts when task states change.
- Edge cases to watch for: Handling tasks that do not exist when changing their state.
- Performance pitfalls: Using data structures that lead to high time complexity for frequent operations.
- Testing considerations: Thoroughly testing all operations, including edge cases and performance under load.