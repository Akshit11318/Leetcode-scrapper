## Employee Free Time
**Problem Link:** https://leetcode.com/problems/employee-free-time/description

**Problem Statement:**
- Input format: A list of intervals representing the busy time of each employee, where each interval is a pair of integers `[start, end]`.
- Constraints: The input list is not empty, and each interval is valid (i.e., `start <= end`).
- Expected output format: A list of intervals representing the common free time of all employees.
- Key requirements and edge cases to consider:
  - Handle the case where the input list is empty.
  - Handle the case where there are no common free intervals.
- Example test cases with explanations:
  - `[[1,3],[2,4]]` should return `[[5, INF]]` because there are no common free intervals.
  - `[[1,3],[5,7],[9,12]]` should return `[[3,5],[7,9]]` because these are the common free intervals.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible intervals and check if they are free for all employees.
- Step-by-step breakdown of the solution:
  1. Generate all possible intervals up to a certain limit (e.g., the maximum end time of all intervals).
  2. For each generated interval, check if it is free for all employees.
  3. If an interval is free for all employees, add it to the result list.
- Why this approach comes to mind first: It is a straightforward and intuitive approach, but it is not efficient.

```cpp
vector<Interval> employeeFreeTime(vector<vector<Interval>>& schedule) {
    vector<Interval> result;
    int maxEndTime = 0;
    for (auto& employee : schedule) {
        for (auto& interval : employee) {
            maxEndTime = max(maxEndTime, interval.end);
        }
    }
    for (int i = 0; i <= maxEndTime; i++) {
        bool isFree = true;
        for (auto& employee : schedule) {
            bool isBusy = false;
            for (auto& interval : employee) {
                if (interval.start <= i && i <= interval.end) {
                    isBusy = true;
                    break;
                }
            }
            if (!isBusy) {
                isFree = false;
                break;
            }
        }
        if (isFree) {
            result.push_back({i, i});
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m \times t)$, where $n$ is the number of employees, $m$ is the average number of intervals per employee, and $t$ is the maximum end time of all intervals.
> - **Space Complexity:** $O(t)$, where $t$ is the maximum end time of all intervals.
> - **Why these complexities occur:** The time complexity occurs because we are generating all possible intervals and checking if they are free for all employees. The space complexity occurs because we are storing the result list.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a priority queue to store the start and end times of all intervals, and then iterate through the queue to find the common free intervals.
- Detailed breakdown of the approach:
  1. Create a priority queue to store the start and end times of all intervals.
  2. Iterate through the queue and find the common free intervals.
  3. If a common free interval is found, add it to the result list.
- Proof of optimality: This approach is optimal because it only requires a single pass through the queue, and it uses a priority queue to efficiently find the common free intervals.

```cpp
vector<Interval> employeeFreeTime(vector<vector<Interval>>& schedule) {
    vector<Interval> result;
    vector<vector<int>> times;
    for (auto& employee : schedule) {
        for (auto& interval : employee) {
            times.push_back({interval.start, 1});
            times.push_back({interval.end, -1});
        }
    }
    sort(times.begin(), times.end(), [](vector<int>& a, vector<int>& b) {
        return a[0] < b[0] || (a[0] == b[0] && a[1] < b[1]);
    });
    int count = 0;
    int prev = -1;
    for (auto& time : times) {
        if (count == 0 && prev != -1) {
            result.push_back({prev, time[0]});
        }
        count += time[1];
        prev = time[0];
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m \times log(n \times m))$, where $n$ is the number of employees and $m$ is the average number of intervals per employee.
> - **Space Complexity:** $O(n \times m)$, where $n$ is the number of employees and $m$ is the average number of intervals per employee.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the queue, and it uses a priority queue to efficiently find the common free intervals.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queue, sorting, and iteration.
- Problem-solving patterns identified: Using a priority queue to efficiently find common free intervals.
- Optimization techniques learned: Using a single pass through the queue and a priority queue to reduce time complexity.
- Similar problems to practice: Finding common free intervals in a list of intervals, finding the maximum free interval in a list of intervals.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not using a priority queue, and not iterating through the queue correctly.
- Edge cases to watch for: Handling the case where the input list is empty, handling the case where there are no common free intervals.
- Performance pitfalls: Using a brute force approach, not using a priority queue, and not iterating through the queue correctly.
- Testing considerations: Testing the approach with different input cases, testing the approach with edge cases, and testing the approach with large input sizes.