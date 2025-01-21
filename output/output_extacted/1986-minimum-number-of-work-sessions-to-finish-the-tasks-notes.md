## Minimum Number of Work Sessions to Finish the Tasks

**Problem Link:** https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/description

**Problem Statement:**
- Input: `tasks` - a list of integers representing the duration of each task.
- Constraints: `1 <= tasks.length <= 14`, `1 <= tasks[i] <= 2^10 - 1`.
- Expected Output: The minimum number of work sessions required to complete all tasks, given that each session can last at most 10 hours.
- Key Requirements: Find the minimum number of sessions such that the sum of tasks in each session does not exceed 10 hours.
- Edge Cases: Tasks cannot be split across sessions, and each task must be completed in one session.

**Example Test Cases:**
- `tasks = [2,3,3]`, Output: `2`
- Explanation: We can have two sessions, one with tasks of duration 2 and 3, and another with the remaining task of duration 3.
- `tasks = [10,10,10]`, Output: `3`
- Explanation: Each task requires a separate session since the maximum duration per session is 10 hours.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of tasks in different sessions to find the minimum number of sessions required.
- Step-by-step breakdown:
  1. Generate all possible subsets of tasks.
  2. For each subset, calculate the total duration.
  3. If the total duration is less than or equal to 10, consider this subset as one session.
  4. Repeat the process for the remaining tasks.
- Why this approach comes to mind first: It's a straightforward way to consider all possibilities, but it's inefficient due to the large number of possible subsets.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minSessions(vector<int>& tasks) {
    int n = tasks.size();
    sort(tasks.rbegin(), tasks.rend()); // Sort tasks in descending order
    vector<int> sessions;
    
    for (int task : tasks) {
        bool added = false;
        for (int& session : sessions) {
            if (session + task <= 10) {
                session += task;
                added = true;
                break;
            }
        }
        if (!added) {
            sessions.push_back(task);
        }
    }
    
    return sessions.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ due to generating all possible subsets in the worst case, where $n$ is the number of tasks.
> - **Space Complexity:** $O(n)$ for storing the sessions.
> - **Why these complexities occur:** The brute force approach involves trying all possible combinations of tasks, leading to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Sort the tasks in descending order and use a greedy approach to assign tasks to sessions.
- Detailed breakdown:
  1. Sort the tasks in descending order to prioritize longer tasks.
  2. Initialize an empty list of sessions.
  3. Iterate through the sorted tasks. For each task, try to add it to an existing session if possible. If not, create a new session.
- Proof of optimality: This approach ensures that we minimize the number of sessions by always trying to fill existing sessions before creating new ones.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minSessions(vector<int>& tasks) {
    int n = tasks.size();
    sort(tasks.rbegin(), tasks.rend()); // Sort tasks in descending order
    vector<int> sessions;
    
    for (int task : tasks) {
        bool added = false;
        for (int& session : sessions) {
            if (session + task <= 10) {
                session += task;
                added = true;
                break;
            }
        }
        if (!added) {
            sessions.push_back(task);
        }
    }
    
    return sessions.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting the tasks, where $n$ is the number of tasks.
> - **Space Complexity:** $O(n)$ for storing the sessions.
> - **Optimality proof:** The greedy approach ensures that we always try to fill existing sessions before creating new ones, leading to the minimum number of sessions required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithms, sorting.
- Problem-solving patterns identified: Prioritizing tasks based on their duration to minimize the number of sessions.
- Optimization techniques learned: Using a greedy approach to assign tasks to sessions.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the tasks in descending order, not checking if a task can be added to an existing session before creating a new one.
- Edge cases to watch for: Tasks with duration greater than 10 hours, empty input list.
- Performance pitfalls: Using a brute force approach that tries all possible combinations of tasks.
- Testing considerations: Test the function with tasks of varying durations, including edge cases.