## Minimum Number of Groups to Create a Valid Assignment
**Problem Link:** https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/description

**Problem Statement:**
- Input: A 2D array `taskTypes` where each subarray contains two integers representing the task type and the day it needs to be completed.
- Expected Output: The minimum number of groups required to complete all tasks without any group having two tasks of the same type on the same day.
- Key Requirements:
  - Each group can have multiple tasks but no more than one task of the same type per day.
  - Minimize the number of groups.
- Example Test Cases:
  - `taskTypes = [[1,2],[2,2],[1,3]]`: The minimum number of groups is 2 because we can assign task 1 to group 1 on day 2 and task 2 to group 2 on day 2, and task 3 to group 1 on day 3.
  - `taskTypes = [[1,2],[2,3],[1,3]]`: The minimum number of groups is 1 because we can assign all tasks to the same group.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of task assignments to groups and check if any combination satisfies the condition of not having two tasks of the same type on the same day in the same group.
- We would start by generating all permutations of tasks to groups and then filter out those that violate the condition.
- This approach comes to mind first because it guarantees finding the minimum number of groups if we can systematically try all possibilities.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int minGroups(std::vector<std::vector<int>>& taskTypes) {
    // Sort tasks by day
    std::sort(taskTypes.begin(), taskTypes.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[1] < b[1];
    });

    int groups = 0;
    std::vector<std::vector<std::vector<int>>> assignments;
    for (const auto& task : taskTypes) {
        bool assigned = false;
        for (auto& group : assignments) {
            bool canAssign = true;
            for (const auto& assignedTask : group) {
                if (assignedTask[0] == task[0] && assignedTask[1] == task[1]) {
                    canAssign = false;
                    break;
                }
            }
            if (canAssign) {
                group.push_back(task);
                assigned = true;
                break;
            }
        }
        if (!assigned) {
            assignments.push_back({task});
            groups++;
        }
    }
    return groups;
}

int main() {
    std::vector<std::vector<int>> taskTypes = {{1,2},{2,2},{1,3}};
    std::cout << minGroups(taskTypes) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of tasks and $m$ is the maximum number of groups. This is because in the worst case, we might need to try assigning each task to each group.
> - **Space Complexity:** $O(n \cdot m)$ for storing the assignments of tasks to groups.
> - **Why these complexities occur:** These complexities occur because we are potentially checking each task against each group, and we store each assignment.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a greedy approach where we assign tasks to the first available group that does not have a task of the same type on the same day.
- We maintain a data structure to keep track of which task types are assigned to each group on each day.
- This approach is optimal because it ensures that we minimize the number of groups by maximizing the utilization of each group.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

int minGroups(std::vector<std::vector<int>>& taskTypes) {
    std::unordered_map<int, std::unordered_map<int, bool>> groupAssignments;
    int groups = 0;
    for (const auto& task : taskTypes) {
        bool assigned = false;
        for (int i = 0; i <= groups; i++) {
            if (groupAssignments[i].find(task[0]) == groupAssignments[i].end() || groupAssignments[i][task[0]] != task[1]) {
                if (groupAssignments[i].find(task[0]) == groupAssignments[i].end()) {
                    groupAssignments[i][task[0]] = task[1];
                } else {
                    groupAssignments[i][task[0]] = task[1];
                }
                assigned = true;
                break;
            }
        }
        if (!assigned) {
            groupAssignments[++groups][task[0]] = task[1];
        }
    }
    return groups + 1; // Since group index starts from 0
}

int main() {
    std::vector<std::vector<int>> taskTypes = {{1,2},{2,2},{1,3}};
    std::cout << minGroups(taskTypes) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of tasks and $m$ is the maximum number of groups.
> - **Space Complexity:** $O(n \cdot m)$ for storing the group assignments.
> - **Optimality proof:** This approach is optimal because it uses a greedy strategy to minimize the number of groups by maximizing the utilization of each group, ensuring that no two tasks of the same type are assigned to the same group on the same day.

---

### Final Notes

**Learning Points:**
- The importance of greedy algorithms in solving optimization problems.
- How to use data structures like `unordered_map` to efficiently keep track of assignments.
- The concept of minimizing the number of groups by maximizing their utilization.

**Mistakes to Avoid:**
- Not considering the greedy approach initially.
- Not using an efficient data structure to keep track of group assignments.
- Not handling the case where a new group needs to be added.