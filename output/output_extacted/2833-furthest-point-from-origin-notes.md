## Furthest Point from Origin

**Problem Link:** https://leetcode.com/problems/furthest-point-from-origin/description

**Problem Statement:**
- Input format: An array of points where each point is an array of two integers.
- Constraints: 1 <= points.length <= 100, -10^4 <= points[i][0] <= 10^4, -10^4 <= points[i][1] <= 10^4.
- Expected output format: The index of the point that is furthest from the origin.
- Key requirements and edge cases to consider: The origin is (0,0), and the distance of a point from the origin is calculated using the formula $\sqrt{x^2 + y^2}$.
- Example test cases with explanations: For example, if the input is `[[1,3],[-2,2]]`, the output should be `0` because the point `(1,3)` is furthest from the origin.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the distance of each point from the origin and keep track of the index of the point with the maximum distance.
- Step-by-step breakdown of the solution: 
  1. Initialize `max_distance` to a very small value and `max_index` to -1.
  2. Iterate over each point in the array.
  3. For each point, calculate its distance from the origin using the formula $\sqrt{x^2 + y^2}$.
  4. If the calculated distance is greater than `max_distance`, update `max_distance` and `max_index`.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that directly addresses the problem statement.

```cpp
class Solution {
public:
    int maxDistance(int** points, int pointsSize, int* pointsColSize) {
        int max_index = 0;
        double max_distance = -1;
        for (int i = 0; i < pointsSize; i++) {
            double distance = sqrt(pow(points[i][0], 2) + pow(points[i][1], 2));
            if (distance > max_distance) {
                max_distance = distance;
                max_index = i;
            }
        }
        return max_index;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of points, because we are iterating over each point once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store `max_distance` and `max_index`.
> - **Why these complexities occur:** The time complexity is linear because we are performing a constant amount of work for each point, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach, because the problem requires calculating the distance of each point from the origin.
- Detailed breakdown of the approach: 
  1. Initialize `max_distance` to a very small value and `max_index` to -1.
  2. Iterate over each point in the array.
  3. For each point, calculate its distance from the origin using the formula $\sqrt{x^2 + y^2}$.
  4. If the calculated distance is greater than `max_distance`, update `max_distance` and `max_index`.
- Proof of optimality: This solution is optimal because it has a time complexity of $O(n)$, which is the minimum time complexity required to solve this problem, because we must examine each point at least once.
- Why further optimization is impossible: We cannot optimize further because we must calculate the distance of each point from the origin, which requires iterating over each point.

```cpp
class Solution {
public:
    int maxDistance(int** points, int pointsSize, int* pointsColSize) {
        int max_index = 0;
        double max_distance = -1;
        for (int i = 0; i < pointsSize; i++) {
            double distance = sqrt(pow(points[i][0], 2) + pow(points[i][1], 2));
            if (distance > max_distance) {
                max_distance = distance;
                max_index = i;
            }
        }
        return max_index;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of points, because we are iterating over each point once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store `max_distance` and `max_index`.
> - **Optimality proof:** This solution is optimal because it has a time complexity of $O(n)$, which is the minimum time complexity required to solve this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and calculation of distances.
- Problem-solving patterns identified: The need to iterate over each point and calculate its distance from the origin.
- Optimization techniques learned: None, because the optimal solution is the same as the brute force approach.
- Similar problems to practice: Other problems that involve calculating distances or iterating over points.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing `max_distance` to a very small value, or not updating `max_index` correctly.
- Edge cases to watch for: Points with very large or very small coordinates, or points that are very close to the origin.
- Performance pitfalls: Using a data structure that has a high time complexity, such as a sorted array or a heap.
- Testing considerations: Testing the solution with a variety of inputs, including points with large and small coordinates, and points that are close to the origin.