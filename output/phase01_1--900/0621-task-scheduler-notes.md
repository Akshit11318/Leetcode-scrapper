## Task Scheduler

**Problem Link:** https://leetcode.com/problems/task-scheduler/description

**Problem Statement:**
- Input format and constraints: Given a `tasks` array of size `n`, where each element `tasks[i]` represents the type of task to be scheduled, and a `n` integer representing the cooldown period, we need to find the least number of units of time that the CPU will take to finish all the given tasks.
- Expected output format: The function should return the minimum number of units of time that the CPU will take to finish all the given tasks.
- Key requirements and edge cases to consider: The CPU needs to cooldown for `n` units of time before scheduling the same task again. If there are multiple tasks that can be scheduled, we can schedule any of them.
- Example test cases with explanations: 
    - Input: `tasks = ["A","A","A","B","B","B"]`, `n = 2`
    - Output: `8`
    - Explanation: 
        - First, we schedule "A" for 3 units of time. 
        - Then, we cooldown for 2 units of time and schedule "B" for 3 units of time. 
        - Finally, we cooldown for 2 units of time. 
        - So, the total time taken is 3 + 2 + 3 + 2 = 10 units of time.
    - Input: `tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]`, `n = 2`
    - Output: `16`
    - Explanation: 
        - We schedule "A" for 6 units of time. 
        - Then, we cooldown for 2 units of time and schedule "B" for 1 unit of time. 
        - Then, we cooldown for 2 units of time and schedule "C" for 1 unit of time. 
        - Then, we cooldown for 2 units of time and schedule "D" for 1 unit of time. 
        - Then, we cooldown for 2 units of time and schedule "E" for 1 unit of time. 
        - Then, we cooldown for 2 units of time and schedule "F" for 1 unit of time. 
        - Then, we cooldown for 2 units of time and schedule "G" for 1 unit of time. 
        - So, the total time taken is 6 + 2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 = 24 units of time.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem using a brute force approach, we can generate all possible schedules and calculate the time taken for each schedule.
- Step-by-step breakdown of the solution: 
    1. Generate all possible schedules.
    2. For each schedule, calculate the time taken.
    3. Keep track of the minimum time taken.
- Why this approach comes to mind first: This approach comes to mind first because it is straightforward and easy to implement. However, it is not efficient and will not work for large inputs.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int leastInterval(vector<char>& tasks, int n) {
    int size = tasks.size();
    vector<int> count(26, 0);
    for (char task : tasks) {
        count[task - 'A']++;
    }
    int maxCount = 0;
    int maxCountTasks = 0;
    for (int i = 0; i < 26; i++) {
        if (count[i] > maxCount) {
            maxCount = count[i];
            maxCountTasks = 1;
        } else if (count[i] == maxCount) {
            maxCountTasks++;
        }
    }
    int ans = (maxCount - 1) * (n + 1) + maxCountTasks;
    return max(size, ans);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of tasks.
> - **Space Complexity:** $O(1)$ as we are using a constant amount of space to store the count of each task.
> - **Why these complexities occur:** The time complexity is $O(n)$ because we are iterating over all tasks to calculate the count of each task. The space complexity is $O(1)$ because we are using a constant amount of space to store the count of each task.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight here is to understand that the maximum frequency task will determine the minimum time units required to complete all tasks. We can calculate this by finding the maximum frequency of any task and then calculating the total time units required to complete all tasks with this frequency.
- Detailed breakdown of the approach: 
    1. Calculate the frequency of each task.
    2. Find the maximum frequency and the number of tasks with this frequency.
    3. Calculate the total time units required to complete all tasks with this frequency.
- Proof of optimality: This approach is optimal because it takes into account the maximum frequency task and the cooldown period, which are the two main factors that determine the minimum time units required to complete all tasks.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int leastInterval(vector<char>& tasks, int n) {
    vector<int> count(26, 0);
    for (char task : tasks) {
        count[task - 'A']++;
    }
    int maxCount = 0;
    int maxCountTasks = 0;
    for (int i = 0; i < 26; i++) {
        if (count[i] > maxCount) {
            maxCount = count[i];
            maxCountTasks = 1;
        } else if (count[i] == maxCount) {
            maxCountTasks++;
        }
    }
    int ans = (maxCount - 1) * (n + 1) + maxCountTasks;
    return max((int)tasks.size(), ans);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of tasks.
> - **Space Complexity:** $O(1)$ as we are using a constant amount of space to store the count of each task.
> - **Optimality proof:** This approach is optimal because it takes into account the maximum frequency task and the cooldown period, which are the two main factors that determine the minimum time units required to complete all tasks. The time complexity is $O(n)$ because we are iterating over all tasks to calculate the count of each task. The space complexity is $O(1)$ because we are using a constant amount of space to store the count of each task.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of scheduling tasks with a cooldown period.
- Problem-solving patterns identified: The problem requires identifying the maximum frequency task and calculating the total time units required to complete all tasks with this frequency.
- Optimization techniques learned: The problem requires optimizing the solution by taking into account the maximum frequency task and the cooldown period.
- Similar problems to practice: Other problems that involve scheduling tasks with a cooldown period, such as the "Task Scheduler II" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not taking into account the maximum frequency task and the cooldown period.
- Edge cases to watch for: The case where the maximum frequency task has a frequency of 1, and the case where the cooldown period is 0.
- Performance pitfalls: Not optimizing the solution by taking into account the maximum frequency task and the cooldown period.
- Testing considerations: Testing the solution with different inputs, such as different task frequencies and cooldown periods.