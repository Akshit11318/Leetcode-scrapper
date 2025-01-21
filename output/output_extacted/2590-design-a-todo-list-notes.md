## Design a Todo List
**Problem Link:** https://leetcode.com/problems/design-a-todo-list/description

**Problem Statement:**
- Input format and constraints: Design a simple `TodoList` class with methods to add, complete, and clear tasks. The `TodoList` class should have methods `addTask(taskId)`, `completeTask(taskId)`, `removeTask(taskId)`, and `listTasks()`.
- Expected output format: The `listTasks()` method should return a list of task IDs that are not completed.
- Key requirements and edge cases to consider: 
  - A task can be added only once.
  - A task can be completed only if it exists and is not already completed.
  - A task can be removed only if it exists.
- Example test cases with explanations:
  - Add task 1, then complete task 1, and list tasks should return an empty list.
  - Add task 1, then remove task 1, and list tasks should return an empty list.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Create a class `TodoList` with methods to add, complete, and remove tasks. Use a `vector` to store all tasks and a `set` to keep track of completed tasks.
- Step-by-step breakdown of the solution:
  1. Create a `TodoList` class with a `vector` to store all tasks and a `set` to keep track of completed tasks.
  2. Implement the `addTask(taskId)` method to add a task to the `vector` if it does not already exist.
  3. Implement the `completeTask(taskId)` method to add a task to the `set` of completed tasks if it exists and is not already completed.
  4. Implement the `removeTask(taskId)` method to remove a task from the `vector` if it exists.
  5. Implement the `listTasks()` method to return a list of task IDs that are not completed.
- Why this approach comes to mind first: It is a straightforward solution that uses common data structures to solve the problem.

```cpp
class TodoList {
public:
    vector<int> tasks;
    set<int> completed;

    void addTask(int taskId) {
        if (find(tasks.begin(), tasks.end(), taskId) == tasks.end()) {
            tasks.push_back(taskId);
        }
    }

    void completeTask(int taskId) {
        if (find(tasks.begin(), tasks.end(), taskId) != tasks.end() && completed.find(taskId) == completed.end()) {
            completed.insert(taskId);
        }
    }

    void removeTask(int taskId) {
        if (find(tasks.begin(), tasks.end(), taskId) != tasks.end()) {
            tasks.erase(remove(tasks.begin(), tasks.end(), taskId), tasks.end());
            completed.erase(taskId);
        }
    }

    vector<int> listTasks() {
        vector<int> result;
        for (int task : tasks) {
            if (completed.find(task) == completed.end()) {
                result.push_back(task);
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for the `addTask`, `completeTask`, and `removeTask` methods, where $n$ is the number of tasks. The `listTasks` method has a time complexity of $O(n)$ as well, where $n$ is the number of tasks.
> - **Space Complexity:** $O(n)$, where $n$ is the number of tasks.
> - **Why these complexities occur:** The time complexity is $O(n)$ because we are using `vector` and `set` operations that have a linear time complexity in the worst case. The space complexity is $O(n)$ because we are storing all tasks in the `vector` and `set`.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use an `unordered_map` to store tasks and their completion status. This allows for constant time complexity for the `addTask`, `completeTask`, and `removeTask` methods.
- Detailed breakdown of the approach:
  1. Create a `TodoList` class with an `unordered_map` to store tasks and their completion status.
  2. Implement the `addTask(taskId)` method to add a task to the `unordered_map` if it does not already exist.
  3. Implement the `completeTask(taskId)` method to mark a task as completed in the `unordered_map` if it exists and is not already completed.
  4. Implement the `removeTask(taskId)` method to remove a task from the `unordered_map` if it exists.
  5. Implement the `listTasks()` method to return a list of task IDs that are not completed.
- Why further optimization is impossible: This approach has the best possible time complexity for the given problem, as we are using an `unordered_map` to store tasks and their completion status.

```cpp
class TodoList {
public:
    unordered_map<int, bool> tasks;

    void addTask(int taskId) {
        if (tasks.find(taskId) == tasks.end()) {
            tasks[taskId] = false;
        }
    }

    void completeTask(int taskId) {
        if (tasks.find(taskId) != tasks.end() && !tasks[taskId]) {
            tasks[taskId] = true;
        }
    }

    void removeTask(int taskId) {
        if (tasks.find(taskId) != tasks.end()) {
            tasks.erase(taskId);
        }
    }

    vector<int> listTasks() {
        vector<int> result;
        for (auto& task : tasks) {
            if (!task.second) {
                result.push_back(task.first);
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for the `addTask`, `completeTask`, and `removeTask` methods. The `listTasks` method has a time complexity of $O(n)$, where $n$ is the number of tasks.
> - **Space Complexity:** $O(n)$, where $n$ is the number of tasks.
> - **Optimality proof:** This approach has the best possible time complexity for the given problem, as we are using an `unordered_map` to store tasks and their completion status.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using an `unordered_map` to store tasks and their completion status allows for constant time complexity for the `addTask`, `completeTask`, and `removeTask` methods.
- Problem-solving patterns identified: Using a data structure that allows for efficient insertion, deletion, and search operations can significantly improve the performance of the solution.
- Optimization techniques learned: Using an `unordered_map` instead of a `vector` or `set` can improve the time complexity of the solution.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a task exists before completing or removing it can lead to errors.
- Edge cases to watch for: Handling cases where a task is added, completed, or removed multiple times can be tricky.
- Performance pitfalls: Using a data structure with a high time complexity for insertion, deletion, or search operations can significantly degrade the performance of the solution.
- Testing considerations: Thoroughly testing the solution with different input scenarios can help identify errors and edge cases.