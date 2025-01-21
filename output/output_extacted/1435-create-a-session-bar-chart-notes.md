## Create a Session Bar Chart
**Problem Link:** https://leetcode.com/problems/create-a-session-bar-chart/description

**Problem Statement:**
- Input format: `int[]` `duration` representing the duration of each session and `int` `threshold` representing the threshold.
- Constraints: $1 \leq \text{duration}.length \leq 100$ and $1 \leq \text{duration}[i] \leq 100$.
- Expected output format: A string of length 10, where each character is either '0' or '1', representing whether the session duration is greater than or equal to the threshold in each hour from 0 to 9.
- Key requirements and edge cases to consider: The input array `duration` can be empty, and the threshold can be greater than the maximum duration.

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each hour from 0 to 9 and check how many sessions have a duration greater than or equal to the threshold in that hour.
- Step-by-step breakdown of the solution:
  1. Initialize an array `chart` of size 10 with all elements set to '0'.
  2. For each hour from 0 to 9, count the number of sessions with duration greater than or equal to the threshold.
  3. If the count is greater than 0, set the corresponding element in `chart` to '1'.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, as it directly implements the problem statement.

```cpp
string createSessionBarChart(vector<int>& duration, int threshold) {
    string chart(10, '0');
    for (int hour = 0; hour < 10; hour++) {
        int count = 0;
        for (int d : duration) {
            if (d >= threshold && d <= threshold + hour) {
                count++;
            }
        }
        if (count > 0) {
            chart[hour] = '1';
        }
    }
    return chart;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of sessions and $m$ is the number of hours (10 in this case). This is because we are iterating over each session for each hour.
> - **Space Complexity:** $O(m)$, where $m$ is the number of hours (10 in this case). This is because we are storing the chart as a string of length 10.
> - **Why these complexities occur:** The time complexity occurs because we are using nested loops to iterate over each session for each hour. The space complexity occurs because we are storing the chart as a string.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can iterate over each session only once and update the chart accordingly.
- Detailed breakdown of the approach:
  1. Initialize an array `chart` of size 10 with all elements set to '0'.
  2. For each session, iterate from the threshold to the duration of the session and update the corresponding elements in `chart` to '1'.
- Proof of optimality: This approach has a time complexity of $O(n + m)$, where $n$ is the number of sessions and $m$ is the number of hours (10 in this case). This is because we are iterating over each session only once and updating the chart accordingly.

```cpp
string createSessionBarChart(vector<int>& duration, int threshold) {
    string chart(10, '0');
    for (int d : duration) {
        for (int i = max(0, threshold); i <= min(9, d); i++) {
            chart[i] = '1';
        }
    }
    return chart;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of sessions and $m$ is the number of hours (10 in this case). This is because we are iterating over each session only once and updating the chart accordingly.
> - **Space Complexity:** $O(m)$, where $m$ is the number of hours (10 in this case). This is because we are storing the chart as a string of length 10.
> - **Optimality proof:** This approach is optimal because we are iterating over each session only once and updating the chart accordingly, resulting in the minimum possible time complexity.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and string manipulation.
- Problem-solving patterns identified: Iterating over each element in an array and updating another array accordingly.
- Optimization techniques learned: Reducing the number of iterations by iterating over each element only once.
- Similar problems to practice: Other problems that involve iterating over arrays and updating other arrays accordingly.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the chart array correctly, not updating the chart array correctly.
- Edge cases to watch for: The input array `duration` can be empty, and the threshold can be greater than the maximum duration.
- Performance pitfalls: Iterating over each session multiple times, resulting in a high time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure it works correctly.