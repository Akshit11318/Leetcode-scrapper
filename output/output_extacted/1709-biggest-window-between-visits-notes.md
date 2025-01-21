## Biggest Window Between Visits
**Problem Link:** [https://leetcode.com/problems/biggest-window-between-visits/description](https://leetcode.com/problems/biggest-window-between-visits/description)

**Problem Statement:**
- Input format and constraints: The problem provides a 2D array `radius` representing the radius of each city and a 2D array `visit` representing the visit times of each city.
- Expected output format: The function should return the maximum window size between visits of any two cities.
- Key requirements and edge cases to consider: We need to handle cases where there are no visits, or the visits are not in the correct order.
- Example test cases with explanations: For example, given `radius = [[1,2,3],[3,2,1]]` and `visit = [[0,0],[2,2]]`, the function should return `2`, because the maximum window size between visits is `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over all possible pairs of cities and calculating the maximum window size between their visits.
- Step-by-step breakdown of the solution:
  1. Iterate over all pairs of cities.
  2. For each pair, find the minimum visit time and the maximum visit time.
  3. Calculate the window size between the minimum and maximum visit times.
  4. Update the maximum window size if the current window size is larger.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has a high time complexity due to the nested loops.

```cpp
int biggestWindowBetweenVisits(vector<vector<int>>& radius, vector<vector<int>>& visit) {
    int maxWindowSize = 0;
    for (int i = 0; i < radius.size(); i++) {
        for (int j = i + 1; j < radius.size(); j++) {
            int minVisitTime = INT_MAX;
            int maxVisitTime = INT_MIN;
            for (int k = 0; k < visit.size(); k++) {
                if (visit[k][0] == i) {
                    minVisitTime = min(minVisitTime, visit[k][1]);
                }
                if (visit[k][0] == j) {
                    minVisitTime = min(minVisitTime, visit[k][1]);
                }
                if (visit[k][0] == i) {
                    maxVisitTime = max(maxVisitTime, visit[k][1]);
                }
                if (visit[k][0] == j) {
                    maxVisitTime = max(maxVisitTime, visit[k][1]);
                }
            }
            if (minVisitTime != INT_MAX && maxVisitTime != INT_MIN) {
                maxWindowSize = max(maxWindowSize, maxVisitTime - minVisitTime);
            }
        }
    }
    return maxWindowSize;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of cities. This is because we have three nested loops.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the maximum window size.
> - **Why these complexities occur:** The time complexity is high because we iterate over all pairs of cities and all visits. The space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a hashmap to store the visit times of each city, and then iterate over the visits to find the maximum window size.
- Detailed breakdown of the approach:
  1. Create a hashmap to store the visit times of each city.
  2. Iterate over the visits and update the hashmap.
  3. Iterate over the visits again and calculate the window size between the minimum and maximum visit times.
  4. Update the maximum window size if the current window size is larger.
- Proof of optimality: This approach is optimal because we only iterate over the visits twice, and we use a hashmap to store the visit times, which allows us to look up the visit times in constant time.

```cpp
int biggestWindowBetweenVisits(vector<vector<int>>& radius, vector<vector<int>>& visit) {
    unordered_map<int, pair<int, int>> cityVisits;
    for (auto& v : visit) {
        if (cityVisits.find(v[0]) == cityVisits.end()) {
            cityVisits[v[0]] = {v[1], v[1]};
        } else {
            cityVisits[v[0]].first = min(cityVisits[v[0]].first, v[1]);
            cityVisits[v[0]].second = max(cityVisits[v[0]].second, v[1]);
        }
    }
    int maxWindowSize = 0;
    for (auto& c1 : cityVisits) {
        for (auto& c2 : cityVisits) {
            if (c1.first != c2.first) {
                maxWindowSize = max(maxWindowSize, abs(c1.second.second - c2.second.first));
            }
        }
    }
    return maxWindowSize;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 + m)$, where $n$ is the number of cities and $m$ is the number of visits. This is because we iterate over the visits twice, and we iterate over the cities to find the maximum window size.
> - **Space Complexity:** $O(n)$, because we use a hashmap to store the visit times of each city.
> - **Optimality proof:** This approach is optimal because we only iterate over the visits twice, and we use a hashmap to store the visit times, which allows us to look up the visit times in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a hashmap to store the visit times of each city, and iterating over the visits to find the maximum window size.
- Problem-solving patterns identified: Using a hashmap to store the visit times, and iterating over the visits to find the maximum window size.
- Optimization techniques learned: Using a hashmap to store the visit times, and iterating over the visits twice to find the maximum window size.
- Similar problems to practice: Finding the maximum window size between visits of any two cities, finding the minimum window size between visits of any two cities.

**Mistakes to Avoid:**
- Common implementation errors: Not using a hashmap to store the visit times, not iterating over the visits twice to find the maximum window size.
- Edge cases to watch for: Not handling cases where there are no visits, or the visits are not in the correct order.
- Performance pitfalls: Not using a hashmap to store the visit times, not iterating over the visits twice to find the maximum window size.
- Testing considerations: Testing the function with different inputs, including cases where there are no visits, or the visits are not in the correct order.