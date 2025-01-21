## Amount of New Area Painted Each Day

**Problem Link:** https://leetcode.com/problems/amount-of-new-area-painted-each-day/description

**Problem Statement:**
- Input: A list of `intervals` representing the start and end days of painting for each worker.
- Output: A list of integers representing the amount of new area painted each day.
- Key requirements and edge cases to consider: 
  - Each worker paints a new area every day.
  - If a worker paints on a day where another worker has already painted, the area is not considered new.
  - The input intervals are non-empty and sorted by start day.
- Example test cases with explanations:
  - Given `intervals = [[1,3],[2,4],[4,5]]`, return `[2,1,1,1]`.
  - Explanation: 
    - Day 1: Worker 1 paints 2 new areas.
    - Day 2: Worker 1 and Worker 2 paint 1 new area each.
    - Day 3: Worker 1 paints 1 new area.
    - Day 4: Worker 3 paints 1 new area.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each day and check which workers are painting.
- Step-by-step breakdown of the solution:
  1. Initialize a set to keep track of painted areas.
  2. Iterate over each day.
  3. For each day, iterate over each worker's interval.
  4. If the worker is painting on the current day and the area is not already painted, increment the count of new areas.
- Why this approach comes to mind first: It directly simulates the problem description, making it easy to understand and implement.

```cpp
#include <vector>
#include <set>

vector<int> amountPainted(vector<vector<int>>& intervals) {
    set<int> paintedAreas;
    vector<int> newAreasEachDay;
    
    for (int day = 1; day <= intervals.back()[1]; day++) {
        int newAreas = 0;
        for (auto& interval : intervals) {
            if (interval[0] <= day && day <= interval[1]) {
                for (int area = interval[0]; area <= interval[1]; area++) {
                    if (paintedAreas.find(area) == paintedAreas.end()) {
                        paintedAreas.insert(area);
                        newAreas++;
                    }
                }
            }
        }
        newAreasEachDay.push_back(newAreas);
    }
    
    return newAreasEachDay;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot d)$, where $n$ is the number of intervals, $m$ is the maximum length of an interval, and $d$ is the number of days.
> - **Space Complexity:** $O(n \cdot m)$ for storing painted areas.
> - **Why these complexities occur:** The nested loops over intervals, days, and areas within intervals lead to the time complexity. The set used to track painted areas contributes to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of iterating over each day and then over each worker's interval, we can iterate over each worker's interval and mark the days they paint.
- Detailed breakdown of the approach:
  1. Initialize a vector to store the count of new areas each day.
  2. Iterate over each worker's interval.
  3. For each interval, iterate over the days the worker paints.
  4. If the area is not already painted, increment the count of new areas for that day.
- Proof of optimality: This approach ensures that we only count new areas once and do so in a single pass over the intervals and days, making it more efficient than the brute force approach.

```cpp
#include <vector>

vector<int> amountPainted(vector<vector<int>>& intervals) {
    int maxDay = 0;
    for (auto& interval : intervals) {
        maxDay = max(maxDay, interval[1]);
    }
    
    vector<int> newAreasEachDay(maxDay, 0);
    vector<bool> paintedAreas(maxDay + 1, false);
    
    for (auto& interval : intervals) {
        for (int day = interval[0]; day <= interval[1]; day++) {
            if (!paintedAreas[day]) {
                newAreasEachDay[day - 1]++;
                paintedAreas[day] = true;
            }
        }
    }
    
    return newAreasEachDay;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of intervals and $m$ is the maximum length of an interval.
> - **Space Complexity:** $O(m)$ for storing painted areas and new areas each day.
> - **Optimality proof:** This approach has a significant reduction in time complexity compared to the brute force method by avoiding unnecessary iterations over areas within intervals for each day.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over intervals, marking painted areas, and counting new areas each day.
- Problem-solving patterns identified: Breaking down the problem into smaller, more manageable parts (intervals and days).
- Optimization techniques learned: Reducing unnecessary iterations and using data structures (like vectors) to efficiently track and update information.
- Similar problems to practice: Problems involving scheduling, resource allocation, and tracking changes over time.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly initializing or updating the count of new areas each day.
- Edge cases to watch for: Handling intervals that start or end on the same day, ensuring all days within an interval are considered.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexities.
- Testing considerations: Thoroughly testing the function with various input scenarios, including edge cases and large inputs.