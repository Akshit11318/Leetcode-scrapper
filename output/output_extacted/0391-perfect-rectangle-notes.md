## Perfect Rectangle
**Problem Link:** https://leetcode.com/problems/perfect-rectangle/description

**Problem Statement:**
- Input: A list of rectangles where each rectangle is represented by a list of four integers `[x, y, x1, y1]` representing the coordinates of the bottom-left and top-right corners.
- Expected output: `true` if the rectangles can form a perfect rectangle, `false` otherwise.
- Key requirements: 
  - All rectangles must be non-overlapping.
  - The union of all rectangles must form a rectangle.
- Edge cases to consider: 
  - Empty input.
  - Input with a single rectangle.
  - Rectangles with zero area.
- Example test cases with explanations: 
  - `[[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[1,4,2,4]]` returns `true`.
  - `[[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]` returns `false`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible combination of rectangles to see if they form a perfect rectangle.
- Step-by-step breakdown of the solution:
  1. Calculate the total area of all rectangles.
  2. Iterate over all possible x and y coordinates to find the bounding box of all rectangles.
  3. Check if the area of the bounding box is equal to the total area of all rectangles.
- Why this approach comes to mind first: It's a straightforward, brute-force approach to check all possibilities.

```cpp
bool isRectangleCover(vector<vector<int>>& rectangles) {
    int area = 0;
    int minX = INT_MAX, minY = INT_MAX, maxX = INT_MIN, maxY = INT_MIN;
    for (auto& rectangle : rectangles) {
        int x = rectangle[0], y = rectangle[1], x1 = rectangle[2], y1 = rectangle[3];
        area += (x1 - x) * (y1 - y);
        minX = min(minX, x);
        minY = min(minY, y);
        maxX = max(maxX, x1);
        maxY = max(maxY, y1);
    }
    return area == (maxX - minX) * (maxY - minY);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rectangles. This is because we're iterating over all rectangles once.
> - **Space Complexity:** $O(1)$ because we're using a constant amount of space to store the minimum and maximum x and y coordinates.
> - **Why these complexities occur:** The time complexity is linear because we're doing a constant amount of work for each rectangle. The space complexity is constant because we're not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking all possible combinations, we can use a hashmap to store the coordinates of the rectangles and check if they form a perfect rectangle.
- Detailed breakdown of the approach:
  1. Create a hashmap to store the coordinates of the rectangles.
  2. Iterate over all rectangles and add their coordinates to the hashmap.
  3. Check if the area of the bounding box is equal to the total area of all rectangles.
- Proof of optimality: This approach is optimal because we're doing a constant amount of work for each rectangle and we're not using any unnecessary data structures.

```cpp
bool isRectangleCover(vector<vector<int>>& rectangles) {
    int area = 0;
    int minX = INT_MAX, minY = INT_MAX, maxX = INT_MIN, maxY = INT_MIN;
    unordered_map<string, int> corners;
    for (auto& rectangle : rectangles) {
        int x = rectangle[0], y = rectangle[1], x1 = rectangle[2], y1 = rectangle[3];
        area += (x1 - x) * (y1 - y);
        string s1 = to_string(x) + "," + to_string(y);
        string s2 = to_string(x1) + "," + to_string(y);
        string s3 = to_string(x) + "," + to_string(y1);
        string s4 = to_string(x1) + "," + to_string(y1);
        if (corners.count(s1)) corners[s1]--;
        else corners[s1] = 1;
        if (corners.count(s2)) corners[s2]--;
        else corners[s2] = 1;
        if (corners.count(s3)) corners[s3]--;
        else corners[s3] = 1;
        if (corners.count(s4)) corners[s4]--;
        else corners[s4] = 1;
        minX = min(minX, x);
        minY = min(minY, y);
        maxX = max(maxX, x1);
        maxY = max(maxY, y1);
    }
    if (area != (maxX - minX) * (maxY - minY)) return false;
    if (corners.size() != 4) return false;
    string s1 = to_string(minX) + "," + to_string(minY);
    string s2 = to_string(maxX) + "," + to_string(minY);
    string s3 = to_string(minX) + "," + to_string(maxY);
    string s4 = to_string(maxX) + "," + to_string(maxY);
    if (corners[s1] != 1 || corners[s2] != 1 || corners[s3] != 1 || corners[s4] != 1) return false;
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of rectangles. This is because we're iterating over all rectangles once.
> - **Space Complexity:** $O(n)$ because we're using a hashmap to store the coordinates of the rectangles.
> - **Optimality proof:** This approach is optimal because we're doing a constant amount of work for each rectangle and we're not using any unnecessary data structures.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a hashmap to store coordinates and checking if they form a perfect rectangle.
- Problem-solving patterns identified: Checking all possible combinations and using a hashmap to optimize the solution.
- Optimization techniques learned: Using a hashmap to store coordinates and checking if they form a perfect rectangle.
- Similar problems to practice: Other problems that involve checking if a set of rectangles form a perfect rectangle.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the area of the bounding box is equal to the total area of all rectangles.
- Edge cases to watch for: Empty input, input with a single rectangle, rectangles with zero area.
- Performance pitfalls: Using a brute-force approach to check all possible combinations.
- Testing considerations: Test the solution with different inputs, including edge cases.