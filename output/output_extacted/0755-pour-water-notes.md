## Pour Water
**Problem Link:** https://leetcode.com/problems/pour-water/description

**Problem Statement:**
- Input: `height` array representing the elevation of each point, `V` the volume of water, and `K` the index where the water starts pouring.
- Expected output: The final state of the `height` array after pouring `V` units of water.
- Key requirements: 
  - Water flows to the lowest adjacent point.
  - If both adjacent points have the same elevation, water flows to the left.
- Edge cases to consider:
  - Handling the boundaries (first and last elements of the array).
  - Ensuring that the water does not flow beyond the boundaries.
- Example test cases:
  - `height = [2,1,0,2]`, `V = 3`, `K = 2`.
  - `height = [3,1,0,2]`, `V = 4`, `K = 2`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to simulate the pouring of water one unit at a time, checking the adjacent points to decide where the water flows.
- Step-by-step breakdown:
  1. Start at index `K`.
  2. Compare the heights of the adjacent points.
  3. Flow the water to the lowest adjacent point, or to the left if they are equal.
  4. Repeat steps 2-3 until all water units have been poured.
- Why this approach comes to mind first: It directly simulates the process described in the problem, making it intuitive.

```cpp
#include <vector>
using namespace std;

vector<int> pourWater(vector<int>& height, int V, int K) {
    int n = height.size();
    for (int i = 0; i < V; ++i) {
        int left = K - 1, right = K + 1;
        int minIndex = K;
        // Check left side
        while (left >= 0 && height[left] <= height[minIndex]) {
            if (height[left] < height[minIndex]) {
                minIndex = left;
            }
            --left;
        }
        // Check right side
        while (right < n && height[right] <= height[minIndex]) {
            if (height[right] < height[minIndex]) {
                minIndex = right;
            }
            ++right;
        }
        // Pour water
        ++height[minIndex];
    }
    return height;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(V \cdot n)$, where $n$ is the number of points. This is because in the worst case, we might need to traverse the entire array for each unit of water.
> - **Space Complexity:** $O(1)$, as we only modify the input array in place.
> - **Why these complexities occur:** The time complexity is high because we potentially scan the array for each unit of water poured, and the space complexity is low because we do not use any additional data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking all points for each unit of water, we can maintain two pointers, one starting from `K` and moving left, and another starting from `K` and moving right. We pour water at the first point where the height is less than the current point.
- Detailed breakdown:
  1. Initialize two pointers, `left` and `right`, at `K`.
  2. For each unit of water, check both directions (left and right) for a point with a lower height.
  3. Pour water at the first point found with a lower height, or at `K` if no such point exists.
- Proof of optimality: This approach ensures that water is poured at the lowest possible point in the most efficient manner, reducing unnecessary scans of the array.

```cpp
vector<int> pourWater(vector<int>& height, int V, int K) {
    int n = height.size();
    for (int i = 0; i < V; ++i) {
        int minIndex = K;
        // Check left side
        for (int j = K - 1; j >= 0; --j) {
            if (height[j] < height[minIndex]) {
                minIndex = j;
            } else if (height[j] > height[minIndex]) {
                break;
            }
        }
        // If left side is not lower, check right side
        if (minIndex == K) {
            for (int j = K + 1; j < n; ++j) {
                if (height[j] < height[minIndex]) {
                    minIndex = j;
                } else if (height[j] > height[minIndex]) {
                    break;
                }
            }
        }
        // Pour water
        ++height[minIndex];
    }
    return height;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(V \cdot n)$, where $n$ is the number of points. This is because in the worst case, for each unit of water, we might need to traverse up to $n$ points.
> - **Space Complexity:** $O(1)$, as we only modify the input array in place.
> - **Optimality proof:** The time complexity remains $O(V \cdot n)$ because we still potentially scan the array for each unit of water. However, this approach is more efficient in practice because it stops scanning as soon as it finds a higher point, reducing unnecessary comparisons.

---

### Final Notes

**Learning Points:**
- The importance of simulating the process described in the problem to understand the flow of water.
- How to optimize the simulation by reducing unnecessary scans of the array.
- The use of two pointers to efficiently find the lowest point in both directions.

**Mistakes to Avoid:**
- Incorrectly handling the boundaries of the array.
- Failing to stop scanning when a higher point is found, leading to unnecessary comparisons.
- Not considering the case where water flows to the left when both adjacent points have the same elevation.