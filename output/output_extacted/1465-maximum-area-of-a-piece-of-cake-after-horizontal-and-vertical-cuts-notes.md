## Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

**Problem Link:** https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/description

**Problem Statement:**
- Input format and constraints: The problem involves a rectangular piece of cake with `h` as the height and `w` as the width. There are `horizontalCuts` and `verticalCuts` given as arrays, representing the positions of the cuts. The task is to find the maximum area of a piece of cake after making all the cuts.
- Expected output format: The maximum area of a piece of cake after making all the cuts.
- Key requirements and edge cases to consider: The cuts are made in ascending order, and the cake is cut into rectangles. The maximum area of a piece of cake is obtained by finding the maximum length and width of a rectangle.
- Example test cases with explanations: For example, given `h = 5`, `w = 4`, `horizontalCuts = [1, 2, 4]`, and `verticalCuts = [3]`, the maximum area of a piece of cake is `(3-1)*(4-3) = 3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves calculating the area of each piece of cake after making all the cuts. This can be done by iterating over all possible rectangles formed by the cuts and calculating their areas.
- Step-by-step breakdown of the solution: 
  1. First, sort the `horizontalCuts` and `verticalCuts` arrays in ascending order.
  2. Then, iterate over all possible rectangles formed by the cuts.
  3. For each rectangle, calculate its area by finding the length and width.
  4. Keep track of the maximum area found so far.
- Why this approach comes to mind first: This approach is straightforward and involves calculating the area of each possible rectangle.

```cpp
int maxArea(int h, int w, vector<int>& horizontalCuts, vector<int>& verticalCuts) {
    sort(horizontalCuts.begin(), horizontalCuts.end());
    sort(verticalCuts.begin(), verticalCuts.end());
    
    int maxArea = 0;
    
    // Calculate the area of each possible rectangle
    for (int i = 0; i <= horizontalCuts.size(); i++) {
        for (int j = 0; j <= verticalCuts.size(); j++) {
            int length = 0, width = 0;
            if (i == 0) {
                length = horizontalCuts[i];
            } else if (i == horizontalCuts.size()) {
                length = h - horizontalCuts[i-1];
            } else {
                length = horizontalCuts[i] - horizontalCuts[i-1];
            }
            
            if (j == 0) {
                width = verticalCuts[j];
            } else if (j == verticalCuts.size()) {
                width = w - verticalCuts[j-1];
            } else {
                width = verticalCuts[j] - verticalCuts[j-1];
            }
            
            maxArea = max(maxArea, length * width);
        }
    }
    
    return maxArea;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ and $m$ are the number of `horizontalCuts` and `verticalCuts` respectively. This is because we are iterating over all possible rectangles formed by the cuts.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over all possible rectangles, and the space complexity occurs because we are not using any extra space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to find the maximum length and width of a rectangle by finding the maximum difference between two consecutive cuts in the `horizontalCuts` and `verticalCuts` arrays.
- Detailed breakdown of the approach: 
  1. First, add `0` and `h` to the `horizontalCuts` array, and `0` and `w` to the `verticalCuts` array.
  2. Then, sort the `horizontalCuts` and `verticalCuts` arrays in ascending order.
  3. Initialize `maxLength` and `maxWidth` to `0`.
  4. Iterate over the `horizontalCuts` array to find the maximum length of a rectangle.
  5. Iterate over the `verticalCuts` array to find the maximum width of a rectangle.
  6. Return the product of `maxLength` and `maxWidth` as the maximum area of a piece of cake.
- Proof of optimality: This approach is optimal because it finds the maximum length and width of a rectangle in linear time complexity.
- Why further optimization is impossible: Further optimization is impossible because we need to iterate over the `horizontalCuts` and `verticalCuts` arrays to find the maximum length and width of a rectangle.

```cpp
int maxArea(int h, int w, vector<int>& horizontalCuts, vector<int>& verticalCuts) {
    horizontalCuts.push_back(0);
    horizontalCuts.push_back(h);
    verticalCuts.push_back(0);
    verticalCuts.push_back(w);
    
    sort(horizontalCuts.begin(), horizontalCuts.end());
    sort(verticalCuts.begin(), verticalCuts.end());
    
    int maxLength = 0, maxWidth = 0;
    
    // Find the maximum length and width of a rectangle
    for (int i = 1; i < horizontalCuts.size(); i++) {
        maxLength = max(maxLength, horizontalCuts[i] - horizontalCuts[i-1]);
    }
    
    for (int i = 1; i < verticalCuts.size(); i++) {
        maxWidth = max(maxWidth, verticalCuts[i] - verticalCuts[i-1]);
    }
    
    return maxLength * maxWidth;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + m \log m)$, where $n$ and $m$ are the number of `horizontalCuts` and `verticalCuts` respectively. This is because we are sorting the `horizontalCuts` and `verticalCuts` arrays.
> - **Space Complexity:** $O(n + m)$, as we are adding `0` and `h` to the `horizontalCuts` array, and `0` and `w` to the `verticalCuts` array.
> - **Optimality proof:** This approach is optimal because it finds the maximum length and width of a rectangle in linear time complexity after sorting the arrays.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, iteration, and finding the maximum length and width of a rectangle.
- Problem-solving patterns identified: Finding the maximum area of a rectangle by finding the maximum length and width.
- Optimization techniques learned: Sorting the arrays to find the maximum length and width in linear time complexity.
- Similar problems to practice: Finding the maximum area of a rectangle in a grid, finding the maximum length of a rectangle in a grid.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the arrays, not initializing `maxLength` and `maxWidth` to `0`.
- Edge cases to watch for: When the `horizontalCuts` or `verticalCuts` array is empty.
- Performance pitfalls: Not using the optimal approach, using a brute force approach.
- Testing considerations: Test the function with different inputs, including edge cases.