## Find the Subtasks That Did Not Execute
**Problem Link:** https://leetcode.com/problems/find-the-subtasks-that-did-not-execute/description

**Problem Statement:**
- Input: `tasks` - a list of tasks, where each task is an array `[task_id, subtask_id]`, and `space` - a list of subtask IDs that executed.
- Constraints: 
  - `1 <= tasks.length <= 10^5`
  - `1 <= task_id, subtask_id <= 10^5`
- Expected output: A list of task IDs that have at least one subtask that did not execute.
- Key requirements and edge cases to consider: 
  - A task is considered as not executed if any of its subtasks did not execute.
  - If all subtasks of a task execute, the task is considered as executed.

**Example Test Cases:**
- Example 1:
  - Input: `tasks = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [3, 1]]`, `space = [1, 2]`
  - Output: `[1, 3]`
  - Explanation: Task 1 has subtask 3 that did not execute. Task 3 has subtask 1 that did not execute.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate over each task and its subtasks to check if any subtask did not execute.
- For each task, check all its subtasks to see if they are in the `space` list.
- If any subtask of a task is not in the `space` list, add the task to the result list.

```cpp
vector<int> findNonExecutedTasks(vector<vector<int>>& tasks, vector<int>& space) {
    // Create a set for faster lookup of executed subtasks
    unordered_set<int> executedSubtasks(space.begin(), space.end());
    
    // Create a map to store tasks and their subtasks
    unordered_map<int, vector<int>> taskSubtasks;
    for (auto& task : tasks) {
        taskSubtasks[task[0]].push_back(task[1]);
    }
    
    // Initialize result list
    vector<int> nonExecutedTasks;
    
    // Iterate over tasks
    for (auto& task : taskSubtasks) {
        bool hasNonExecutedSubtask = false;
        for (int subtask : task.second) {
            if (executedSubtasks.find(subtask) == executedSubtasks.end()) {
                hasNonExecutedSubtask = true;
                break;
            }
        }
        if (hasNonExecutedSubtask) {
            nonExecutedTasks.push_back(task.first);
        }
    }
    
    return nonExecutedTasks;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of tasks and $m$ is the total number of subtasks. This is because we are iterating over all tasks and subtasks once.
> - **Space Complexity:** $O(n + m)$ for storing the `executedSubtasks` set and the `taskSubtasks` map.
> - **Why these complexities occur:** The brute force approach requires iterating over all tasks and subtasks to check for execution status, leading to linear time complexity. The space complexity is also linear due to the need to store all tasks and subtasks in data structures for efficient lookup.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach remains similar to the brute force approach but focuses on minimizing unnecessary iterations and optimizing data structures for faster lookup.
- Use a `unordered_set` for `space` to ensure fast lookup of executed subtasks.
- Use a `unordered_map` to group tasks by their IDs and store their subtasks. This allows for efficient iteration over tasks and their subtasks.

```cpp
vector<int> findNonExecutedTasksOptimal(vector<vector<int>>& tasks, vector<int>& space) {
    unordered_set<int> executedSubtasks(space.begin(), space.end());
    unordered_map<int, vector<int>> taskSubtasks;
    for (auto& task : tasks) {
        taskSubtasks[task[0]].push_back(task[1]);
    }
    
    vector<int> nonExecutedTasks;
    for (auto& task : taskSubtasks) {
        bool hasNonExecutedSubtask = false;
        for (int subtask : task.second) {
            if (executedSubtasks.find(subtask) == executedSubtasks.end()) {
                hasNonExecutedSubtask = true;
                break;
            }
        }
        if (hasNonExecutedSubtask) {
            nonExecutedTasks.push_back(task.first);
        }
    }
    
    return nonExecutedTasks;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of tasks and $m$ is the total number of subtasks. This is because we are iterating over all tasks and subtasks once.
> - **Space Complexity:** $O(n + m)$ for storing the `executedSubtasks` set and the `taskSubtasks` map.
> - **Optimality proof:** This approach is optimal because it requires at least one pass through all tasks and subtasks to determine their execution status, leading to a linear time complexity. The use of efficient data structures like `unordered_set` and `unordered_map` minimizes the constant factors, making it the most efficient solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, lookup, and grouping of data.
- Problem-solving patterns identified: Using data structures like sets and maps for efficient lookup and grouping.
- Optimization techniques learned: Minimizing unnecessary iterations and using efficient data structures.
- Similar problems to practice: Problems involving data grouping, lookup, and iteration.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect use of data structures, failure to handle edge cases.
- Edge cases to watch for: Empty input lists, tasks with no subtasks, subtasks that are not in the `space` list.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to higher than necessary time or space complexity.
- Testing considerations: Ensure to test with various input sizes, edge cases, and scenarios to validate the solution's correctness and performance.