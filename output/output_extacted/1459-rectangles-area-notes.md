## Rectangles Area

**Problem Link:** https://leetcode.com/problems/rectangles-area/description

**Problem Statement:**
- Input format and constraints: Given a set of rectangles, find the total area of all rectangles.
- Expected output format: The total area of all rectangles.
- Key requirements and edge cases to consider: 
  - Rectangles may overlap.
  - Rectangles may have zero area.
- Example test cases with explanations:
  - Example 1: rectangles = [[0,0,2,2],[1,1,3,3]], return 7.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the area of each rectangle and add them up.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the total area.
  2. Iterate over each rectangle.
  3. For each rectangle, calculate its area by multiplying the width and height.
  4. Add the area of the current rectangle to the total area.
- Why this approach comes to mind first: It's the most straightforward way to solve the problem.

```cpp
class Solution {
public:
    int rectangleArea(vector<vector<int>>& rectangles) {
        int totalArea = 0;
        for (auto& rectangle : rectangles) {
            int x1 = rectangle[0], y1 = rectangle[1], x2 = rectangle[2], y2 = rectangle[3];
            int width = x2 - x1, height = y2 - y1;
            totalArea += width * height;
        }
        return totalArea;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rectangles, because we iterate over each rectangle once.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the total area.
> - **Why these complexities occur:** We only need to iterate over each rectangle once to calculate its area, so the time complexity is linear. We don't need any additional data structures, so the space complexity is constant.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach. We can't do better than calculating the area of each rectangle and adding them up.
- Detailed breakdown of the approach: The same as the brute force approach.
- Proof of optimality: We can't do better than $O(n)$ time complexity because we need to at least look at each rectangle once. We can't do better than $O(1)$ space complexity because we don't need any additional data structures.
- Why further optimization is impossible: We can't avoid calculating the area of each rectangle, so we can't do better than $O(n)$ time complexity.

```cpp
class Solution {
public:
    int rectangleArea(vector<vector<int>>& rectangles) {
        int totalArea = 0;
        for (auto& rectangle : rectangles) {
            int x1 = rectangle[0], y1 = rectangle[1], x2 = rectangle[2], y2 = rectangle[3];
            int width = x2 - x1, height = y2 - y1;
            totalArea += width * height;
        }
        return totalArea;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rectangles.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the total area.
> - **Optimality proof:** We can't do better than $O(n)$ time complexity because we need to at least look at each rectangle once. We can't do better than $O(1)$ space complexity because we don't need any additional data structures.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, basic arithmetic operations.
- Problem-solving patterns identified: Calculate the area of each rectangle and add them up.
- Optimization techniques learned: None, because the brute force approach is already optimal.
- Similar problems to practice: Other problems that involve calculating areas or volumes.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the total area variable, forgetting to add the area of each rectangle to the total area.
- Edge cases to watch for: Rectangles with zero area, rectangles that overlap.
- Performance pitfalls: None, because the optimal approach has a linear time complexity and constant space complexity.
- Testing considerations: Test with rectangles that have different areas, test with rectangles that overlap, test with rectangles that have zero area.