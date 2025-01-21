## Random Point in Non-Overlapping Rectangles

**Problem Link:** https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/description

**Problem Statement:**
- Input format: A list of rectangles where each rectangle is represented as a list of four integers `[x, y, w, h]`, representing the x and y coordinates of the bottom-left corner, and the width and height of the rectangle.
- Constraints: The given rectangles do not overlap and cover a total area of $N$.
- Expected output format: Implement a class `Solution` with two methods: `Solution(vector<vector<int>>& rects)` to initialize the solution with the given rectangles, and `vector<int> pickRandomPoint()` to return a random point in the non-overlapping rectangles.
- Key requirements and edge cases to consider: Ensure that each point in the rectangles is equally likely to be returned.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To ensure each point is equally likely to be returned, we could store all points in a data structure and then select one randomly.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store all points.
  2. For each rectangle, calculate all points within the rectangle and add them to the list.
  3. When `pickRandomPoint()` is called, return a random point from the list.
- Why this approach comes to mind first: It directly addresses the requirement of equal likelihood by explicitly storing all points.

```cpp
class Solution {
public:
    vector<vector<int>> points;
    
    Solution(vector<vector<int>>& rects) {
        for (auto& rect : rects) {
            int x = rect[0], y = rect[1], w = rect[2], h = rect[3];
            for (int i = x; i <= x + w; i++) {
                for (int j = y; j <= y + h; j++) {
                    points.push_back({i, j});
                }
            }
        }
    }
    
    vector<int> pickRandomPoint() {
        int idx = rand() % points.size();
        return points[idx];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$ for initialization where $N$ is the total number of points across all rectangles, and $O(1)$ for `pickRandomPoint()`.
> - **Space Complexity:** $O(N)$ to store all points.
> - **Why these complexities occur:** The brute force approach requires storing every point, leading to linear time and space complexity with respect to the total number of points.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of storing all points, we can store the rectangles and their areas. When `pickRandomPoint()` is called, first select a rectangle randomly based on its area, then select a random point within that rectangle.
- Detailed breakdown of the approach:
  1. Initialize the solution with rectangles and calculate the total area.
  2. Store the cumulative area of the rectangles.
  3. When `pickRandomPoint()` is called, generate a random number between 0 and the total area.
  4. Find the rectangle that corresponds to the generated random number using binary search.
  5. Generate another random number to select a point within the chosen rectangle.
- Why further optimization is impossible: This approach ensures each point is equally likely to be returned without storing all points, achieving optimal space complexity.

```cpp
class Solution {
public:
    vector<vector<int>> rects;
    vector<int> areas;
    int totalArea;
    
    Solution(vector<vector<int>>& rects) {
        this->rects = rects;
        areas.resize(rects.size());
        totalArea = 0;
        for (int i = 0; i < rects.size(); i++) {
            int w = rects[i][2], h = rects[i][3];
            areas[i] = w * h;
            totalArea += areas[i];
            if (i > 0) areas[i] += areas[i-1];
        }
    }
    
    vector<int> pickRandomPoint() {
        int target = rand() % totalArea;
        int idx = lower_bound(areas.begin(), areas.end(), target + 1) - areas.begin();
        int x = rects[idx][0], y = rects[idx][1], w = rects[idx][2], h = rects[idx][3];
        if (idx > 0) target -= areas[idx-1];
        return {x + target % w, y + target / w};
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$ for initialization where $m$ is the number of rectangles, and $O(\log m)$ for `pickRandomPoint()` due to binary search.
> - **Space Complexity:** $O(m)$ to store the rectangles and their cumulative areas.
> - **Optimality proof:** This approach minimizes storage by only keeping track of rectangles and their areas, and ensures equal likelihood of point selection through the use of random numbers based on area.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Random point selection, binary search for efficient rectangle selection.
- Problem-solving patterns identified: Using area to weight the randomness, applying binary search for efficient lookup.
- Optimization techniques learned: Minimizing storage by leveraging the properties of the input data (rectangles and their areas).
- Similar problems to practice: Other problems involving random selection or geometric calculations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect calculation of areas or cumulative areas, faulty binary search implementation.
- Edge cases to watch for: Empty input, rectangles with zero area.
- Performance pitfalls: Storing all points as in the brute force approach, leading to high memory usage.
- Testing considerations: Ensure that each point in the rectangles has an equal chance of being selected, test with different sets of rectangles.