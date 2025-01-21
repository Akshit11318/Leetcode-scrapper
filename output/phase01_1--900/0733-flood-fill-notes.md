## Flood Fill
**Problem Link:** https://leetcode.com/problems/flood-fill/description

**Problem Statement:**
- Input: A 2D array `image` representing an image, a point `(sr, sc)` representing the starting row and column, and a new color `newColor`.
- Constraints: `1 <= image.length <= 200`, `1 <= image[i].length <= 200`, `0 <= sr < image.length`, `0 <= sc < image[0].length`, and `1 <= newColor <= 10^9`.
- Expected Output: The modified `image` after applying the flood fill operation.
- Key Requirements: Fill all connected components of the same color as the starting point with the new color.
- Edge Cases: The starting point may not be within the bounds of the image, or the new color may be the same as the original color.

**Example Test Cases:**
- `image = [[1,1,1],[1,1,0],[1,0,1]]`, `sr = 1`, `sc = 1`, `newColor = 2`. Expected output: `[[2,2,2],[2,2,0],[2,0,1]]`.
- `image = [[0,0,0],[0,1,1]]`, `sr = 1`, `sc = 1`, `newColor = 1`. Expected output: `[[0,0,0],[0,1,1]]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate through each pixel in the image and check if it's connected to the starting point.
- The brute force approach involves checking all eight directions (up, down, left, right, and diagonals) for each pixel.
- This approach comes to mind first because it's straightforward and easy to implement.

```cpp
#include <vector>
using namespace std;

vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
    int originalColor = image[sr][sc];
    if (originalColor == newColor) return image;

    // Define the eight directions
    vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1}};

    // Function to check if a pixel is within bounds
    auto isValid = [&](int r, int c) {
        return r >= 0 && r < image.size() && c >= 0 && c < image[0].size();
    };

    // Function to perform DFS
    auto dfs = [&](int r, int c) {
        if (!isValid(r, c) || image[r][c] != originalColor) return;
        image[r][c] = newColor;
        for (auto& dir : directions) {
            dfs(r + dir.first, c + dir.second);
        }
    };

    dfs(sr, sc);
    return image;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the image, respectively. This is because in the worst-case scenario, we might need to visit every pixel.
> - **Space Complexity:** $O(m \cdot n)$, due to the recursive call stack in the worst case.
> - **Why these complexities occur:** The time complexity is due to the potential need to visit every pixel, and the space complexity is due to the recursive call stack.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach is essentially the same as the brute force approach, as we still need to visit all connected pixels.
- However, we can optimize the code slightly by using a more efficient data structure, such as a queue, to perform the DFS.
- This approach is optimal because we must visit all connected pixels to perform the flood fill operation.

```cpp
#include <vector>
#include <queue>
using namespace std;

vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
    int originalColor = image[sr][sc];
    if (originalColor == newColor) return image;

    // Define the four directions (up, down, left, right)
    vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    // Function to check if a pixel is within bounds
    auto isValid = [&](int r, int c) {
        return r >= 0 && r < image.size() && c >= 0 && c < image[0].size();
    };

    // Function to perform BFS
    queue<pair<int, int>> q;
    q.push({sr, sc});
    image[sr][sc] = newColor;
    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();
        for (auto& dir : directions) {
            int nr = r + dir.first, nc = c + dir.second;
            if (isValid(nr, nc) && image[nr][nc] == originalColor) {
                image[nr][nc] = newColor;
                q.push({nr, nc});
            }
        }
    }

    return image;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the image, respectively.
> - **Space Complexity:** $O(m \cdot n)$, due to the queue in the worst case.
> - **Optimality proof:** This approach is optimal because we must visit all connected pixels to perform the flood fill operation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS, BFS, and flood fill.
- Problem-solving patterns identified: using a queue or recursive function calls to perform a search.
- Optimization techniques learned: using a more efficient data structure, such as a queue, to perform the search.

**Mistakes to Avoid:**
- Common implementation errors: not checking for invalid input or not handling edge cases.
- Edge cases to watch for: when the starting point is outside the bounds of the image or when the new color is the same as the original color.
- Performance pitfalls: using an inefficient data structure or algorithm, such as a recursive function call without memoization.
- Testing considerations: testing the function with different input sizes and edge cases to ensure correctness and efficiency.