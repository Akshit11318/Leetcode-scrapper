## Course Schedule III

**Problem Link:** https://leetcode.com/problems/course-schedule-iii/description

**Problem Statement:**
- Input format and constraints: You are given a list of `n` courses where each course is represented as a pair of integers `[duration, deadline]`. The duration of each course is `duration` days and the deadline to complete the course is `deadline` days after the start date.
- Expected output format: Return the maximum number of courses that can be completed on or before their deadlines.
- Key requirements and edge cases to consider: The total duration of all selected courses must not exceed the deadline of the last selected course. Courses can be completed in any order.
- Example test cases with explanations:
  - Example 1: Input: `[[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]`. Output: `3`. Explanation: We can complete the courses with durations 100, 200, and 1000 days on or before their deadlines.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of courses to find the maximum number of courses that can be completed on or before their deadlines.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of courses.
  2. For each combination, calculate the total duration and check if it is less than or equal to the deadline of the last selected course.
  3. If the total duration is less than or equal to the deadline, update the maximum number of courses that can be completed.
- Why this approach comes to mind first: It is a straightforward approach to try all possible combinations and check if they meet the conditions.

```cpp
#include <vector>
#include <algorithm>

int scheduleCourse(std::vector<std::vector<int>>& courses) {
    int n = courses.size();
    std::sort(courses.begin(), courses.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[1] < b[1];
    });
    
    int maxCourses = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        int totalDuration = 0;
        int numCourses = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                totalDuration += courses[i][0];
                numCourses++;
                if (totalDuration > courses[i][1]) {
                    break;
                }
            }
        }
        if (totalDuration <= courses[n-1][1] && numCourses > maxCourses) {
            maxCourses = numCourses;
        }
    }
    return maxCourses;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of courses. This is because we generate all possible combinations of courses and for each combination, we iterate through all courses to calculate the total duration.
> - **Space Complexity:** $O(n)$, where $n$ is the number of courses. This is because we need to store the courses and their deadlines.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it tries all possible combinations of courses, which results in exponential time complexity. The space complexity is linear because we only need to store the courses and their deadlines.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a priority queue to store the courses with the longest duration first. We iterate through the sorted courses and for each course, we check if adding it to the current schedule exceeds the deadline. If it does, we remove the course with the longest duration from the schedule and add the current course.
- Detailed breakdown of the approach:
  1. Sort the courses by their deadlines.
  2. Initialize a priority queue to store the courses with the longest duration first.
  3. Iterate through the sorted courses and for each course, check if adding it to the current schedule exceeds the deadline.
  4. If it does, remove the course with the longest duration from the schedule and add the current course.
- Proof of optimality: This approach is optimal because it always chooses the course with the longest duration first and removes the course with the longest duration when the deadline is exceeded. This ensures that the maximum number of courses are completed on or before their deadlines.

```cpp
#include <vector>
#include <queue>
#include <algorithm>

int scheduleCourse(std::vector<std::vector<int>>& courses) {
    int n = courses.size();
    std::sort(courses.begin(), courses.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        return a[1] < b[1];
    });
    
    std::priority_queue<int> pq;
    int totalDuration = 0;
    for (int i = 0; i < n; i++) {
        if (totalDuration + courses[i][0] <= courses[i][1]) {
            totalDuration += courses[i][0];
            pq.push(courses[i][0]);
        } else if (!pq.empty() && pq.top() > courses[i][0]) {
            totalDuration -= pq.top();
            pq.pop();
            totalDuration += courses[i][0];
            pq.push(courses[i][0]);
        }
    }
    return pq.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of courses. This is because we sort the courses and use a priority queue to store the courses with the longest duration first.
> - **Space Complexity:** $O(n)$, where $n$ is the number of courses. This is because we need to store the courses and their deadlines.
> - **Optimality proof:** This approach is optimal because it always chooses the course with the longest duration first and removes the course with the longest duration when the deadline is exceeded. This ensures that the maximum number of courses are completed on or before their deadlines.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, priority queue.
- Problem-solving patterns identified: Sorting, iterating through the sorted data, using a priority queue to store the data.
- Optimization techniques learned: Using a priority queue to store the data with the longest duration first, removing the course with the longest duration when the deadline is exceeded.
- Similar problems to practice: Scheduling problems, greedy algorithms.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the total duration exceeds the deadline, not removing the course with the longest duration when the deadline is exceeded.
- Edge cases to watch for: Courses with the same deadline, courses with zero duration.
- Performance pitfalls: Using a brute force approach, not using a priority queue to store the data with the longest duration first.
- Testing considerations: Test the code with different inputs, including edge cases and large inputs.