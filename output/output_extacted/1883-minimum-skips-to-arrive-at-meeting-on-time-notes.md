## Minimum Skips to Arrive at Meeting on Time
**Problem Link:** https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/description

**Problem Statement:**
- Input: `distances` array representing the distance to each segment of the road, `speed` representing the speed limit, `hoursBefore` representing the hours before the meeting the person needs to arrive.
- Output: The minimum number of `skips` required to arrive at the meeting on time.
- Key requirements: Calculate the time taken to travel each segment at the given speed, then determine the minimum number of skips needed to ensure the total travel time does not exceed the allowed time before the meeting.
- Example test cases: 
  - Example 1: `distances = [1,2,3,4]`, `speed = 5`, `hoursBefore = 3`, Output: `2`.
  - Example 2: `distances = [7,22,57]`, `speed = 7`, `hoursBefore = 5`, Output: `1`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of skips to find the minimum that satisfies the condition of arriving on time.
- Step-by-step breakdown: 
  1. Generate all possible combinations of skips for the given segments.
  2. For each combination, calculate the total travel time considering the skips.
  3. Check if the total travel time is less than or equal to the allowed time before the meeting.
  4. Keep track of the minimum number of skips that satisfy the condition.

```cpp
#include <vector>
#include <cmath>

int minSkips(std::vector<int>& distances, int speed, int hoursBefore) {
    int n = distances.size();
    double allowedTime = hoursBefore * 60.0; // Convert hours to minutes
    
    int minSkips = n; // Initialize with maximum possible skips
    
    // Try all possible combinations of skips
    for (int mask = 0; mask < (1 << n); ++mask) {
        double totalTime = 0.0;
        int skips = 0;
        
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) == 0) { // If the bit is not set, do not skip
                totalTime += std::ceil(distances[i] / (double)speed) * 60.0; // Calculate time taken for this segment
            } else {
                skips++;
            }
        }
        
        if (totalTime <= allowedTime && skips < minSkips) {
            minSkips = skips;
        }
    }
    
    return minSkips;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of segments. This is because we generate all possible combinations of skips (which is $2^n$) and for each combination, we iterate through the segments to calculate the total time.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum skips and the current combination of skips.
> - **Why these complexities occur:** The brute force approach involves trying all possible combinations of skips, leading to exponential time complexity. However, the space complexity remains constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use dynamic programming to calculate the minimum number of skips needed to arrive on time, rather than trying all combinations.
- Detailed breakdown: 
  1. Initialize a DP table to store the minimum number of skips needed for each segment and each possible remaining time.
  2. Iterate through each segment and for each possible remaining time, calculate the minimum number of skips needed by either skipping the current segment or not.
  3. Use the DP table to find the minimum number of skips needed to arrive on time.

```cpp
#include <vector>
#include <climits>

int minSkips(std::vector<int>& distances, int speed, int hoursBefore) {
    int n = distances.size();
    int allowedTime = hoursBefore * 60; // Convert hours to minutes
    
    // Initialize DP table
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(allowedTime + 1, INT_MAX));
    dp[0][0] = 0; // Base case: 0 skips for 0 time
    
    for (int i = 1; i <= n; ++i) {
        int time = std::ceil(distances[i - 1] / (double)speed) * 60; // Calculate time taken for this segment
        
        for (int j = 0; j <= allowedTime; ++j) {
            if (j < time) { // If not enough time, must skip
                dp[i][j] = dp[i - 1][j];
            } else { // Otherwise, choose the minimum between skipping and not skipping
                dp[i][j] = std::min(dp[i - 1][j], dp[i - 1][j - time] + 1);
            }
        }
    }
    
    // Find the minimum number of skips needed to arrive on time
    int minSkips = INT_MAX;
    for (int i = 0; i <= allowedTime; ++i) {
        if (dp[n][i] < minSkips) {
            minSkips = dp[n][i];
        }
    }
    
    return minSkips;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot allowedTime)$, where $n$ is the number of segments and $allowedTime$ is the allowed time before the meeting in minutes.
> - **Space Complexity:** $O(n \cdot allowedTime)$, as we use a DP table of size $n \times allowedTime$.
> - **Optimality proof:** This approach is optimal because it considers all possible combinations of skips and times in a systematic and efficient manner, avoiding the need to try all possible combinations explicitly.

---

### Final Notes

**Learning Points:**
- The importance of dynamic programming in solving problems that involve finding the minimum or maximum of something under certain constraints.
- How to apply dynamic programming to solve problems that involve making choices (in this case, skipping or not skipping segments).
- The trade-off between time and space complexity in dynamic programming solutions.

**Mistakes to Avoid:**
- Not considering all possible combinations of skips and times.
- Not using dynamic programming to avoid trying all possible combinations explicitly.
- Not initializing the DP table correctly.
- Not considering the base case correctly.

---