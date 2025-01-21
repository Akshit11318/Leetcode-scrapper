## Lonely Pixel I
**Problem Link:** https://leetcode.com/problems/lonely-pixel-i/description

**Problem Statement:**
- Input format and constraints: The input is a 2D array `picture` of size `m x n`, where each pixel is either `B` (black) or `W` (white). The goal is to find the number of lonely pixels, which are black pixels that are not adjacent to any other black pixels.
- Expected output format: The output should be the count of lonely pixels.
- Key requirements and edge cases to consider: 
    - A pixel is considered lonely if it is black and none of its adjacent pixels (up, down, left, right) are black.
    - The input picture is guaranteed to be non-empty.
- Example test cases with explanations:
    - `picture = [["W","W","B"],["W","B","W"],["B","W","W"]]` should return `3`.
    - `picture = [["B","B","B"],["B","B","B"],["B","B","B"]]` should return `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest approach is to iterate through each pixel in the picture and check if it is a lonely pixel by examining its adjacent pixels.
- Step-by-step breakdown of the solution:
    1. Iterate through each pixel in the picture.
    2. For each pixel, check if it is black.
    3. If the pixel is black, check its adjacent pixels (up, down, left, right).
    4. If none of the adjacent pixels are black, increment the count of lonely pixels.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
int findLonelyPixel(vector<vector<char>>& picture) {
    int m = picture.size();
    int n = picture[0].size();
    int count = 0;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (picture[i][j] == 'B') {
                bool isLonely = true;
                // Check adjacent pixels
                if (i > 0 && picture[i-1][j] == 'B') isLonely = false;
                if (i < m-1 && picture[i+1][j] == 'B') isLonely = false;
                if (j > 0 && picture[i][j-1] == 'B') isLonely = false;
                if (j < n-1 && picture[i][j+1] == 'B') isLonely = false;
                if (isLonely) count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \times n)$, where $m$ is the number of rows and $n$ is the number of columns in the picture. This is because we are iterating through each pixel once.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the count of lonely pixels.
> - **Why these complexities occur:** The time complexity is linear with respect to the size of the input because we are checking each pixel exactly once. The space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal because we must check each pixel at least once to determine if it is lonely.
- Detailed breakdown of the approach: The optimal approach remains the same as the brute force approach because it is already efficient and necessary.
- Proof of optimality: Any algorithm must check each pixel at least once to determine if it is lonely, so the optimal time complexity is $O(m \times n)$.
- Why further optimization is impossible: We cannot improve upon the time complexity because checking each pixel is a necessary step.

```cpp
int findLonelyPixel(vector<vector<char>>& picture) {
    int m = picture.size();
    int n = picture[0].size();
    int count = 0;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (picture[i][j] == 'B') {
                bool isLonely = true;
                // Check adjacent pixels
                if (i > 0 && picture[i-1][j] == 'B') isLonely = false;
                if (i < m-1 && picture[i+1][j] == 'B') isLonely = false;
                if (j > 0 && picture[i][j-1] == 'B') isLonely = false;
                if (j < n-1 && picture[i][j+1] == 'B') isLonely = false;
                if (isLonely) count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \times n)$, where $m$ is the number of rows and $n$ is the number of columns in the picture.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the count of lonely pixels.
> - **Optimality proof:** The time complexity is optimal because we must check each pixel at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks.
- Problem-solving patterns identified: Checking each element in a 2D array.
- Optimization techniques learned: None, as the brute force approach is already optimal.
- Similar problems to practice: Other problems involving iteration and conditional checks.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors when checking adjacent pixels.
- Edge cases to watch for: Pixels on the edges of the picture have fewer adjacent pixels to check.
- Performance pitfalls: None, as the optimal approach is already efficient.
- Testing considerations: Test the function with different inputs, including edge cases like a picture with no black pixels or a picture with only black pixels.