## Shortest Distance to Target Color
**Problem Link:** https://leetcode.com/problems/shortest-distance-to-target-color/description

**Problem Statement:**
- Input format: You are given an array `colors` of length `n`, a 2D array `queries` of size `q` where `queries[i] = [target, idx]`, and an integer `k`.
- Constraints: `1 <= n <= 1000`, `1 <= q <= 1000`, `1 <= k <= n`, `1 <= idx <= n`, and `1 <= target <= 1000`.
- Expected output format: An array of integers where the `i`th element is the shortest distance between `queries[i][1]` and `target` color in the `colors` array, with a maximum distance of `k`.
- Key requirements and edge cases to consider:
  - Handling cases where the target color is not found within the specified distance `k`.
  - Dealing with queries where the index is at or near the edges of the array, requiring careful consideration of boundary conditions.
- Example test cases with explanations:
  - For `colors = [1,1,2,1,3,2,2,3,3]`, `queries = [[1,3],[2,6],[3,3]]`, and `k = 3`, the output should be `[3,0,3]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to solve this problem is to iterate through the `colors` array from the query index in both directions until we find the target color or we have checked `k` indices in each direction.
- Step-by-step breakdown of the solution:
  1. For each query, initialize the distance to the target color as infinity.
  2. Iterate through the `colors` array to the left and right of the query index up to `k` steps.
  3. If the target color is found within the `k` steps, update the distance to the target color.
  4. If no target color is found within `k` steps, return `-1` or handle as per the problem's requirements.

```cpp
#include <vector>
using namespace std;

vector<int> shortestDistanceColor(vector<int>& colors, vector<vector<int>>& queries, int k) {
    vector<int> result;
    for (auto& query : queries) {
        int target = query[0], idx = query[1] - 1; // Adjust index for 0-based indexing
        int left = idx, right = idx;
        bool found = false;
        for (int i = 1; i <= k; ++i) {
            if (left >= 0 && colors[left] == target) {
                result.push_back(i);
                found = true;
                break;
            }
            if (right < colors.size() && colors[right] == target) {
                result.push_back(i);
                found = true;
                break;
            }
            if (left > 0) left--;
            if (right < colors.size() - 1) right++;
        }
        if (!found) {
            result.push_back(-1); // or handle as per specific problem requirements
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(q \cdot k)$, where $q$ is the number of queries and $k$ is the maximum distance to check. This is because for each query, we potentially check up to $k$ indices in both directions.
> - **Space Complexity:** $O(q)$, for storing the results of the queries.
> - **Why these complexities occur:** The brute force approach requires linear scanning in both directions from each query index, leading to the time complexity. The space complexity is due to storing the results for each query.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of scanning from each query index, we can precompute the distances to each color from every index in the `colors` array. This allows for constant-time lookup for each query.
- Detailed breakdown of the approach:
  1. Initialize a 2D array `distances` of size `n x 1001` (assuming colors are in the range 1 to 1000) with all elements set to infinity.
  2. For each color, perform two passes through the `colors` array: one from left to right and one from right to left. Update the `distances` array with the minimum distance to the current color.
  3. For each query, directly look up the distance to the target color in the `distances` array.

```cpp
#include <vector>
#include <limits>
using namespace std;

vector<int> shortestDistanceColor(vector<int>& colors, vector<vector<int>>& queries, int k) {
    const int n = colors.size();
    const int maxColor = 1000;
    vector<vector<int>> distances(n, vector<int>(maxColor + 1, numeric_limits<int>::max()));
    
    // Left to right pass
    for (int color = 1; color <= maxColor; ++color) {
        int lastOccurrence = -1;
        for (int i = 0; i < n; ++i) {
            if (colors[i] == color) {
                lastOccurrence = i;
            }
            if (lastOccurrence != -1) {
                distances[i][color] = min(distances[i][color], i - lastOccurrence);
            }
        }
    }
    
    // Right to left pass
    for (int color = 1; color <= maxColor; ++color) {
        int lastOccurrence = -1;
        for (int i = n - 1; i >= 0; --i) {
            if (colors[i] == color) {
                lastOccurrence = i;
            }
            if (lastOccurrence != -1) {
                distances[i][color] = min(distances[i][color], lastOccurrence - i);
            }
        }
    }
    
    vector<int> result;
    for (auto& query : queries) {
        int target = query[0], idx = query[1] - 1;
        int minDistance = distances[idx][target];
        result.push_back(minDistance <= k ? minDistance : -1);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot maxColor + q)$, where $n$ is the length of the `colors` array, $maxColor$ is the maximum possible color value, and $q$ is the number of queries. The precomputation step dominates the time complexity.
> - **Space Complexity:** $O(n \cdot maxColor)$, for storing the precomputed distances.
> - **Optimality proof:** This approach is optimal because it reduces the query time to constant, leveraging the precomputation to avoid redundant scans of the `colors` array for each query. The space complexity is a trade-off for achieving this efficiency.