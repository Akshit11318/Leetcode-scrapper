## The First Day of the Maximum Recorded Degree in Each City

**Problem Link:** https://leetcode.com/problems/the-first-day-of-the-maximum-recorded-degree-in-each-city/description

**Problem Statement:**
- Input format: A 2D array `dailyTemperatures` of size `n x m`, where `n` is the number of cities and `m` is the number of days. `dailyTemperatures[i][j]` represents the temperature in city `i` on day `j`.
- Constraints: `1 <= n <= 1000`, `1 <= m <= 1000`, `-10^5 <= dailyTemperatures[i][j] <= 10^5`.
- Expected output format: An array `result` of size `n`, where `result[i]` is the first day when the maximum temperature was recorded in city `i`.
- Key requirements and edge cases to consider: Handling cases where the maximum temperature occurs multiple times, and cases where the input array is empty or contains invalid data.
- Example test cases with explanations:
  - Example 1: `dailyTemperatures = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, Output: `[0, 0, 0]`.
  - Example 2: `dailyTemperatures = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]`, Output: `[0, 0, 0]`.

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each city and find the maximum temperature. Then, iterate over each day to find the first occurrence of the maximum temperature.
- Step-by-step breakdown of the solution:
  1. Initialize an array `result` to store the first day of the maximum temperature for each city.
  2. Iterate over each city `i`.
  3. Find the maximum temperature `maxTemp` in city `i`.
  4. Iterate over each day `j` in city `i` to find the first occurrence of `maxTemp`.
  5. Store the first occurrence of `maxTemp` in `result[i]`.
- Why this approach comes to mind first: It is a straightforward approach that directly addresses the problem statement.

```cpp
vector<int> dailyTemperatures(vector<vector<int>>& dailyTemperatures) {
    int n = dailyTemperatures.size();
    vector<int> result(n, -1);
    
    for (int i = 0; i < n; i++) {
        int maxTemp = INT_MIN;
        for (int j = 0; j < dailyTemperatures[i].size(); j++) {
            maxTemp = max(maxTemp, dailyTemperatures[i][j]);
        }
        
        for (int j = 0; j < dailyTemperatures[i].size(); j++) {
            if (dailyTemperatures[i][j] == maxTemp) {
                result[i] = j;
                break;
            }
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m^2)$, where $n$ is the number of cities and $m$ is the number of days. This is because we iterate over each city and then over each day twice (once to find the maximum temperature and once to find the first occurrence of the maximum temperature).
> - **Space Complexity:** $O(n)$, where $n$ is the number of cities. This is because we store the result for each city in an array of size $n$.
> - **Why these complexities occur:** The time complexity is high because we use nested loops to find the maximum temperature and its first occurrence. The space complexity is low because we only store the result for each city.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can find the maximum temperature and its first occurrence in a single pass over the days for each city.
- Detailed breakdown of the approach:
  1. Initialize an array `result` to store the first day of the maximum temperature for each city.
  2. Iterate over each city `i`.
  3. Initialize `maxTemp` to the temperature on the first day in city `i`.
  4. Iterate over each day `j` in city `i`.
  5. If the temperature on day `j` is greater than `maxTemp`, update `maxTemp` and store the current day `j` in `result[i]`.
- Why further optimization is impossible: We must iterate over each day for each city to find the maximum temperature and its first occurrence.

```cpp
vector<int> dailyTemperatures(vector<vector<int>>& dailyTemperatures) {
    int n = dailyTemperatures.size();
    vector<int> result(n, -1);
    
    for (int i = 0; i < n; i++) {
        int maxTemp = dailyTemperatures[i][0];
        result[i] = 0;
        
        for (int j = 1; j < dailyTemperatures[i].size(); j++) {
            if (dailyTemperatures[i][j] > maxTemp) {
                maxTemp = dailyTemperatures[i][j];
                result[i] = j;
            }
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of cities and $m$ is the number of days. This is because we iterate over each city and then over each day once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of cities. This is because we store the result for each city in an array of size $n$.
> - **Optimality proof:** This is the optimal solution because we must iterate over each day for each city to find the maximum temperature and its first occurrence.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and array manipulation.
- Problem-solving patterns identified: Finding the maximum value and its first occurrence in an array.
- Optimization techniques learned: Reducing the number of iterations and using a single pass to find the maximum value and its first occurrence.
- Similar problems to practice: Finding the minimum value and its first occurrence, finding the maximum and minimum values in an array, and finding the first occurrence of a given value in an array.

**Mistakes to Avoid:**
- Common implementation errors: Using incorrect array indices, not initializing variables, and not handling edge cases.
- Edge cases to watch for: Empty input arrays, arrays with a single element, and arrays with duplicate maximum values.
- Performance pitfalls: Using unnecessary iterations and not optimizing the solution for large input sizes.
- Testing considerations: Testing with different input sizes, testing with edge cases, and testing with duplicate maximum values.