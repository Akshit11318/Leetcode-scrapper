## Maximum Performance of a Team

**Problem Link:** [https://leetcode.com/problems/maximum-performance-of-a-team/description](https://leetcode.com/problems/maximum-performance-of-a-team/description)

**Problem Statement:**
- Input format: You are given two arrays `speed` and `efficiency`, both of length `n`, where `speed[i]` and `efficiency[i]` represent the speed and efficiency of the `i-th` employee respectively.
- Constraints: `1 <= n <= 10^5`, `1 <= speed[i] <= 10^5`, `1 <= efficiency[i] <= 10^5`.
- Expected output format: The maximum performance of a team.
- Key requirements and edge cases to consider: The maximum performance of a team is the maximum sum of the speeds of the employees in the team, divided by the minimum efficiency of the employees in the team.
- Example test cases with explanations: 
    - For `speed = [2, 10, 3, 1, 5, 8]` and `efficiency = [5, 4, 3, 9, 7, 2]`, the maximum performance of a team is `60.0`.
    - For `speed = [1, 1, 1, 1, 1]` and `efficiency = [1, 1, 1, 1, 1]`, the maximum performance of a team is `1.0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of employees and calculate the performance of each combination.
- Step-by-step breakdown of the solution:
    1. Generate all possible combinations of employees.
    2. For each combination, calculate the sum of the speeds and the minimum efficiency.
    3. Calculate the performance of the team by dividing the sum of the speeds by the minimum efficiency.
    4. Update the maximum performance if the current performance is higher.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible combinations of employees.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

double maxPerformance(int n, std::vector<int>& speed, std::vector<int>& efficiency) {
    double maxPerf = 0.0;
    for (int mask = 0; mask < (1 << n); mask++) {
        double speedSum = 0.0;
        double minEff = 1e9;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                speedSum += speed[i];
                minEff = std::min(minEff, efficiency[i]);
            }
        }
        if (minEff != 1e9) {
            maxPerf = std::max(maxPerf, speedSum / minEff);
        }
    }
    return maxPerf;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of employees. This is because we generate all possible combinations of employees and for each combination, we iterate over the employees to calculate the sum of the speeds and the minimum efficiency.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum performance and the current combination of employees.
> - **Why these complexities occur:** The time complexity occurs because we try all possible combinations of employees, which is exponential in the number of employees. The space complexity is constant because we only use a constant amount of space to store the maximum performance and the current combination of employees.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can sort the employees based on their efficiency in descending order. Then, we can use a priority queue to keep track of the employees with the highest speeds.
- Detailed breakdown of the approach:
    1. Sort the employees based on their efficiency in descending order.
    2. Initialize a priority queue to store the employees with the highest speeds.
    3. Iterate over the sorted employees. For each employee, add the employee to the priority queue and update the maximum performance if the current performance is higher.
    4. If the size of the priority queue exceeds the number of employees with the same efficiency, remove the employee with the lowest speed from the priority queue.
- Proof of optimality: This approach is optimal because we consider all possible combinations of employees with the highest efficiencies and we use a priority queue to efficiently keep track of the employees with the highest speeds.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

double maxPerformance(int n, std::vector<int>& speed, std::vector<int>& efficiency) {
    std::vector<std::pair<int, int>> employees;
    for (int i = 0; i < n; i++) {
        employees.push_back({efficiency[i], speed[i]});
    }
    std::sort(employees.begin(), employees.end(), [](const auto& a, const auto& b) {
        return a.first > b.first;
    });
    double maxPerf = 0.0;
    double speedSum = 0.0;
    std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
    for (const auto& employee : employees) {
        speedSum += employee.second;
        pq.push(employee.second);
        while (pq.size() > employee.first) {
            speedSum -= pq.top();
            pq.pop();
        }
        maxPerf = std::max(maxPerf, speedSum / employee.first);
    }
    return maxPerf;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of employees. This is because we sort the employees based on their efficiency and we use a priority queue to keep track of the employees with the highest speeds.
> - **Space Complexity:** $O(n)$, as we use a priority queue to store the employees with the highest speeds.
> - **Optimality proof:** This approach is optimal because we consider all possible combinations of employees with the highest efficiencies and we use a priority queue to efficiently keep track of the employees with the highest speeds.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, priority queue, and greedy algorithm.
- Problem-solving patterns identified: trying all possible combinations of employees and using a priority queue to efficiently keep track of the employees with the highest speeds.
- Optimization techniques learned: using a priority queue to reduce the time complexity.
- Similar problems to practice: problems that involve sorting and using a priority queue to efficiently keep track of the highest or lowest values.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, such as an empty input array.
- Edge cases to watch for: an empty input array, or an array with a single element.
- Performance pitfalls: using a brute force approach that tries all possible combinations of employees, which can lead to an exponential time complexity.
- Testing considerations: testing the function with different input arrays, including edge cases, to ensure that it works correctly and efficiently.