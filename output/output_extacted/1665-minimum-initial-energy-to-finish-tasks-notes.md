## Minimum Initial Energy to Finish Tasks

**Problem Link:** https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/description

**Problem Statement:**
- Input format and constraints: Given `n` tasks where each task is represented as an array of two integers, `tasks[i] = [actualEnergy, minimumInitialEnergy]`, where `actualEnergy` is the actual energy required to complete the task and `minimumInitialEnergy` is the minimum initial energy required to start the task. The goal is to find the minimum initial energy required to finish all tasks.
- Expected output format: The minimum initial energy required.
- Key requirements and edge cases to consider: The tasks can be performed in any order, and the initial energy decreases by `actualEnergy` after completing a task but never goes below 0.
- Example test cases with explanations: For example, given `tasks = [[1,2],[2,6],[5,3],[4,5]]`, the minimum initial energy required is 7.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible orders of tasks and calculate the minimum initial energy required for each order.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of tasks.
  2. For each permutation, calculate the minimum initial energy required.
  3. Update the minimum initial energy if a smaller value is found.
- Why this approach comes to mind first: It is a straightforward approach that considers all possibilities.

```cpp
#include <algorithm>
#include <vector>

int minimumEffort(std::vector<std::vector<int>>& tasks) {
    std::sort(tasks.begin(), tasks.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[1] - a[0] > b[1] - b[0];
    });
    int initialEnergy = 0, currentEnergy = 0;
    for (const auto& task : tasks) {
        int actualEnergy = task[0], minInitialEnergy = task[1];
        if (currentEnergy < minInitialEnergy) {
            initialEnergy += minInitialEnergy - currentEnergy;
            currentEnergy = minInitialEnergy;
        }
        currentEnergy -= actualEnergy;
    }
    return initialEnergy;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of tasks, due to sorting.
> - **Space Complexity:** $O(n)$ for sorting in the worst case.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and the space complexity is due to the sorting algorithm's internal memory usage.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Sort the tasks based on the difference between the minimum initial energy and the actual energy required. This way, tasks with higher differences are performed first, minimizing the initial energy required.
- Detailed breakdown of the approach:
  1. Sort the tasks based on the difference between the minimum initial energy and the actual energy required.
  2. Initialize the minimum initial energy and the current energy.
  3. Iterate through the sorted tasks, updating the minimum initial energy and the current energy as necessary.
- Proof of optimality: This approach is optimal because it ensures that tasks with higher differences are performed first, minimizing the initial energy required.

```cpp
int minimumEffort(std::vector<std::vector<int>>& tasks) {
    std::sort(tasks.begin(), tasks.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[1] - a[0] > b[1] - b[0];
    });
    int initialEnergy = 0, currentEnergy = 0;
    for (const auto& task : tasks) {
        int actualEnergy = task[0], minInitialEnergy = task[1];
        if (currentEnergy < minInitialEnergy) {
            initialEnergy += minInitialEnergy - currentEnergy;
            currentEnergy = minInitialEnergy;
        }
        currentEnergy -= actualEnergy;
    }
    return initialEnergy;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of tasks, due to sorting.
> - **Space Complexity:** $O(n)$ for sorting in the worst case.
> - **Optimality proof:** The approach is optimal because it minimizes the initial energy required by performing tasks with higher differences first.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, greedy algorithm.
- Problem-solving patterns identified: Minimizing the initial energy required by performing tasks with higher differences first.
- Optimization techniques learned: Sorting tasks based on the difference between the minimum initial energy and the actual energy required.
- Similar problems to practice: Other problems involving sorting and greedy algorithms.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the minimum initial energy and the current energy correctly.
- Edge cases to watch for: Tasks with the same difference between the minimum initial energy and the actual energy required.
- Performance pitfalls: Using an inefficient sorting algorithm.
- Testing considerations: Test the solution with different inputs and edge cases to ensure correctness.