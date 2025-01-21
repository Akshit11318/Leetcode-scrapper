## Avoid Flood in the City
**Problem Link:** https://leetcode.com/problems/avoid-flood-in-the-city/description

**Problem Statement:**
- Input format: You are given an integer array `heights` of length `n`, representing the height of the water in the city on each day.
- Constraints: The length of the `heights` array is between $1$ and $10^5$. The values in the `heights` array are between $1$ and $10^5$.
- Expected output format: Return an array of integers `result` where `result[i]` is the height of the water in the city on day `i` after taking the necessary actions to avoid flooding, or `-1` if it is not possible to avoid flooding.
- Key requirements and edge cases to consider:
  - If the height of the water is `0` on a day, it means the city is dry on that day.
  - If the height of the water is greater than `0` on a day, it means the city is flooded on that day.
  - To avoid flooding, you can choose to dry the city on a day when the city is flooded, but you can only do this if the city is not flooded on the previous day.
- Example test cases with explanations:
  - Input: `heights = [1,0,2,0,3,1]`
    - Output: `[1,0,2,0,3,-1]`
    - Explanation: On day `4`, the city is flooded with a height of `3`, and on day `5`, the city is flooded with a height of `1`. Since the city is flooded on two consecutive days, it is not possible to avoid flooding.
  - Input: `heights = [2,3,0,0,3,1,0,1,0,2,0]`
    - Output: `[2,3,0,0,3,1,0,1,0,2,0]`
    - Explanation: On day `1`, the city is flooded with a height of `2`, and on day `2`, the city is flooded with a height of `3`. Since the city is not flooded on day `3`, we can dry the city on day `3` to avoid flooding.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible combinations of drying the city on each day to avoid flooding.
- Step-by-step breakdown of the solution:
  1. Iterate through each day in the `heights` array.
  2. For each day, check if the city is flooded (i.e., the height of the water is greater than `0`).
  3. If the city is flooded, try drying the city on the current day and recursively check if it is possible to avoid flooding on the remaining days.
  4. If it is not possible to avoid flooding on the remaining days, try not drying the city on the current day and recursively check if it is possible to avoid flooding on the remaining days.
- Why this approach comes to mind first: This approach is intuitive because it tries all possible combinations of drying the city on each day to avoid flooding.

```cpp
vector<int> avoidFlood(vector<int>& heights) {
    vector<int> result(heights.size(), -1);
    function<bool(int)> dfs = [&](int day) {
        if (day == heights.size()) return true;
        if (heights[day] == 0) {
            result[day] = 0;
            return dfs(day + 1);
        }
        for (int i = day + 1; i < heights.size(); i++) {
            if (heights[i] == heights[day] && result[i] == -1) {
                result[i] = heights[i];
                if (dfs(day + 1)) return true;
                result[i] = -1;
            }
        }
        return false;
    };
    if (dfs(0)) return result;
    else return {};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ where $n$ is the number of days in the `heights` array. This is because in the worst case, we try all possible combinations of drying the city on each day.
> - **Space Complexity:** $O(n)$ where $n$ is the number of days in the `heights` array. This is because we use a recursive function call stack of maximum depth $n$.
> - **Why these complexities occur:** These complexities occur because we use a recursive function to try all possible combinations of drying the city on each day.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to use a `map` to store the days when the city is flooded with the same height of water.
- Detailed breakdown of the approach:
  1. Iterate through each day in the `heights` array.
  2. For each day, check if the city is flooded (i.e., the height of the water is greater than `0`).
  3. If the city is flooded, check if there is a previous day when the city was flooded with the same height of water.
  4. If there is a previous day when the city was flooded with the same height of water, try to dry the city on the current day.
  5. If it is not possible to dry the city on the current day, return an empty array because it is not possible to avoid flooding.
- Proof of optimality: This approach is optimal because it uses a `map` to store the days when the city is flooded with the same height of water, which allows us to efficiently check if there is a previous day when the city was flooded with the same height of water.

```cpp
vector<int> avoidFlood(vector<int>& heights) {
    vector<int> result(heights.size(), 1);
    unordered_map<int, int> dryDay;
    for (int i = 0; i < heights.size(); i++) {
        if (heights[i] == 0) {
            result[i] = 0;
        } else {
            if (dryDay.count(heights[i])) {
                int dryIndex = dryDay[heights[i]];
                if (result[dryIndex] == 1) {
                    result[dryIndex] = 0;
                    dryDay[heights[i]] = i;
                    result[i] = -1;
                } else {
                    return {};
                }
            } else {
                dryDay[heights[i]] = i;
                result[i] = -1;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of days in the `heights` array. This is because we iterate through each day in the `heights` array once.
> - **Space Complexity:** $O(n)$ where $n$ is the number of days in the `heights` array. This is because we use a `map` to store the days when the city is flooded with the same height of water.
> - **Optimality proof:** This approach is optimal because it uses a `map` to store the days when the city is flooded with the same height of water, which allows us to efficiently check if there is a previous day when the city was flooded with the same height of water.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `map` to store the days when the city is flooded with the same height of water.
- Problem-solving patterns identified: Using a greedy approach to try to dry the city on the current day if there is a previous day when the city was flooded with the same height of water.
- Optimization techniques learned: Using a `map` to efficiently check if there is a previous day when the city was flooded with the same height of water.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if there is a previous day when the city was flooded with the same height of water before trying to dry the city on the current day.
- Edge cases to watch for: When the city is flooded on two consecutive days, it is not possible to avoid flooding.
- Performance pitfalls: Using a recursive function to try all possible combinations of drying the city on each day, which can lead to exponential time complexity.
- Testing considerations: Test the function with different inputs, including edge cases, to ensure that it works correctly.