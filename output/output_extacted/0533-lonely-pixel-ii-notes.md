## Lonely Pixel II

**Problem Link:** https://leetcode.com/problems/lonely-pixel-ii/description

**Problem Statement:**
- Input format and constraints: Given an `m x n` picture consisting of `1`s (black) and `0`s (white), return the number of black lonely pixels.
- Expected output format: A single integer representing the count of black lonely pixels.
- Key requirements and edge cases to consider: A black lonely pixel is a black pixel that is not adjacent to another black pixel horizontally or vertically.
- Example test cases with explanations:
  - Example 1: Input: `picture = [["W","W","B"],["W","B","W"],["B","W","W"]]`, Output: `3`
  - Example 2: Input: `picture = [["B","B","B"],["B","B","B"],["B","B","B"]]`, Output: `0`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each pixel, check its adjacent pixels (up, down, left, right) to see if any are black. If not, increment the count of black lonely pixels.
- Step-by-step breakdown of the solution:
  1. Initialize a count variable to 0.
  2. Iterate over each pixel in the picture.
  3. For each pixel, check its adjacent pixels.
  4. If the pixel is black and none of its adjacent pixels are black, increment the count.
- Why this approach comes to mind first: It directly implements the definition of a lonely pixel.

```cpp
int findLonelyPixel(vector<vector<char>>& picture) {
    int m = picture.size();
    int n = picture[0].size();
    int count = 0;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (picture[i][j] == 'B') {
                bool isLonely = true;
                // Check up
                if (i > 0 && picture[i-1][j] == 'B') isLonely = false;
                // Check down
                if (i < m - 1 && picture[i+1][j] == 'B') isLonely = false;
                // Check left
                if (j > 0 && picture[i][j-1] == 'B') isLonely = false;
                // Check right
                if (j < n - 1 && picture[i][j+1] == 'B') isLonely = false;
                if (isLonely) count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the dimensions of the picture. This is because we potentially check every pixel and its neighbors.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store our count and loop variables.
> - **Why these complexities occur:** The time complexity is linear with respect to the total number of pixels because we might have to check each pixel once. The space complexity is constant because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal in terms of time complexity because we must at least glance at each pixel once to determine if it's lonely. However, we can slightly optimize the code for better readability and maintainability.
- Detailed breakdown of the approach: The same as the brute force, but with minor improvements for readability.
- Proof of optimality: Since we must check each pixel at least once, the time complexity cannot be better than $O(m \cdot n)$.

```cpp
int findLonelyPixel(vector<vector<char>>& picture) {
    int m = picture.size();
    int n = picture[0].size();
    int count = 0;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (picture[i][j] == 'B' && 
                (i == 0 || picture[i-1][j] != 'B') && 
                (i == m - 1 || picture[i+1][j] != 'B') && 
                (j == 0 || picture[i][j-1] != 'B') && 
                (j == n - 1 || picture[i][j+1] != 'B')) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, for the same reasons as the brute force approach.
> - **Space Complexity:** $O(1)$, also the same as the brute force approach.
> - **Optimality proof:** This approach is optimal because it checks each pixel exactly once, which is necessary to determine if a pixel is lonely.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over a 2D array, conditional checks for neighboring elements.
- Problem-solving patterns identified: Checking each element and its neighbors to determine a property (in this case, being a lonely pixel).
- Optimization techniques learned: While the brute force was already quite efficient, minor improvements for readability can enhance the code's maintainability.
- Similar problems to practice: Other problems involving checking properties of elements in a 2D array based on their neighbors.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check the boundaries of the array (e.g., not checking if `i` or `j` is 0 before accessing `picture[i-1][j]`).
- Edge cases to watch for: When the picture has only one row or one column, or when it's entirely filled with 'B's or 'W's.
- Performance pitfalls: Unnecessary checks or iterations that could increase the time complexity beyond $O(m \cdot n)$.
- Testing considerations: Ensure to test with various picture sizes and configurations to cover all edge cases.