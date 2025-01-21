## Smallest Rectangle Enclosing Black Pixels
**Problem Link:** https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/description

**Problem Statement:**
- Input format and constraints: The problem provides a binary image represented as a 2D `vector<vector<char>>` named `image`. Each pixel in the image is either `'0'` (white) or `'1'` (black). The task is to find the smallest rectangle (defined by its top-left and bottom-right corners) that encloses all black pixels.
- Expected output format: The function should return a `vector<int>` containing four integers representing the coordinates of the top-left and bottom-right corners of the smallest enclosing rectangle in the format `[min_x, min_y, max_x, max_y]`.
- Key requirements and edge cases to consider: The input image may contain no black pixels, in which case the function should return an empty vector `[]`. If there are black pixels, the rectangle must enclose all of them.
- Example test cases with explanations:
  - For an image with no black pixels, the output should be `[]`.
  - For an image with a single black pixel, the output should enclose just that pixel.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Start by finding all the black pixels in the image. Then, determine the minimum and maximum x and y coordinates of these black pixels, which will define the smallest enclosing rectangle.
- Step-by-step breakdown of the solution:
  1. Iterate through each pixel in the image to find all black pixels.
  2. For each black pixel found, update the minimum and maximum x and y coordinates if necessary.
  3. Once all pixels have been checked, use the minimum and maximum x and y coordinates to define the rectangle.
- Why this approach comes to mind first: It's a straightforward method that checks every pixel, ensuring no black pixel is missed.

```cpp
vector<int> minAreaRect(vector<vector<char>>& image) {
    int minX = INT_MAX, minY = INT_MAX, maxX = INT_MIN, maxY = INT_MIN;
    for (int i = 0; i < image.size(); ++i) {
        for (int j = 0; j < image[i].size(); ++j) {
            if (image[i][j] == '1') {
                minX = min(minX, i);
                minY = min(minY, j);
                maxX = max(maxX, i);
                maxY = max(maxY, j);
            }
        }
    }
    if (minX == INT_MAX) return {}; // No black pixels found
    return {minX, minY, maxX, maxY};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the image. This is because we potentially check every pixel once.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the minimum and maximum coordinates.
> - **Why these complexities occur:** The time complexity is linear with respect to the total number of pixels because we check each pixel once. The space complexity is constant because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal for finding the smallest rectangle enclosing all black pixels because it must check each pixel at least once to ensure all black pixels are found.
- Detailed breakdown of the approach: The optimal approach remains the same as the brute force approach because it already achieves the best possible time complexity for this problem.
- Proof of optimality: Any algorithm must at least read the input, which for an image of size $m \times n$ requires $O(m \cdot n)$ time. Thus, the brute force approach is optimal.
- Why further optimization is impossible: Since we must check each pixel at least once, we cannot improve upon the $O(m \cdot n)$ time complexity.

```cpp
// The code for the optimal approach is the same as the brute force approach
vector<int> minAreaRect(vector<vector<char>>& image) {
    int minX = INT_MAX, minY = INT_MAX, maxX = INT_MIN, maxY = INT_MIN;
    for (int i = 0; i < image.size(); ++i) {
        for (int j = 0; j < image[i].size(); ++j) {
            if (image[i][j] == '1') {
                minX = min(minX, i);
                minY = min(minY, j);
                maxX = max(maxX, i);
                maxY = max(maxY, j);
            }
        }
    }
    if (minX == INT_MAX) return {}; // No black pixels found
    return {minX, minY, maxX, maxY};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the image.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** The algorithm checks each pixel once, which is necessary to find all black pixels, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and basic optimization.
- Problem-solving patterns identified: Checking each element in a dataset to find specific conditions.
- Optimization techniques learned: Understanding that sometimes the brute force approach is optimal due to the nature of the problem.
- Similar problems to practice: Other problems involving finding minimum or maximum areas or perimeters in grids or images.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect loop bounds, missing checks for edge cases (like an empty image).
- Edge cases to watch for: Images with no black pixels, images with a single black pixel, and very large images.
- Performance pitfalls: Unnecessary iterations or checks that could increase the time complexity.
- Testing considerations: Ensure to test with various image sizes, including edge cases like empty images or images with a single black pixel.