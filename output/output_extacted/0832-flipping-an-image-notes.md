## Flipping an Image

**Problem Link:** https://leetcode.com/problems/flipping-an-image/description

**Problem Statement:**
- Input format and constraints: The input is a 2D array `image` where each element is either 0 or 1. The array has `m` rows and `n` columns.
- Expected output format: The function should return the flipped image.
- Key requirements and edge cases to consider: The image should be flipped both horizontally and the values should be inverted (i.e., 0 becomes 1 and 1 becomes 0).
- Example test cases with explanations:
    - `image = [[1,1,0],[1,0,1],[0,0,0]]` should return `[[1,0,0],[0,1,0],[1,1,1]]`.
    - `image = [[1,1,0,0],[1,0,0,1],[0,1,0,1],[1,0,1,0]]` should return `[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To flip the image, we need to iterate over each row and reverse the row. Then, we need to invert the values.
- Step-by-step breakdown of the solution:
    1. Iterate over each row in the image.
    2. Reverse the row.
    3. Invert the values in the row.
- Why this approach comes to mind first: This approach is straightforward and directly implements the requirements.

```cpp
class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
        int m = image.size();
        int n = image[0].size();
        
        // Iterate over each row
        for (int i = 0; i < m; i++) {
            // Reverse the row
            int left = 0;
            int right = n - 1;
            while (left < right) {
                swap(image[i][left], image[i][right]);
                left++;
                right--;
            }
            
            // Invert the values in the row
            for (int j = 0; j < n; j++) {
                image[i][j] = 1 - image[i][j];
            }
        }
        
        return image;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns. This is because we iterate over each element in the image once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the indices.
> - **Why these complexities occur:** The time complexity is $O(m \cdot n)$ because we need to visit each element in the image once to flip and invert it. The space complexity is $O(1)$ because we only use a constant amount of space to store the indices.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can combine the two steps of flipping and inverting into one step. Instead of first flipping the row and then inverting the values, we can do both operations at the same time.
- Detailed breakdown of the approach: We iterate over each row and for each element, we check if it is at the left or right half of the row. If it is at the left half, we invert the corresponding element at the right half. If it is at the right half, we invert the corresponding element at the left half.
- Proof of optimality: This approach has the same time complexity as the brute force approach, but it is more efficient in practice because it only requires one pass over the data.
- Why further optimization is impossible: The time complexity of $O(m \cdot n)$ is optimal because we need to visit each element in the image at least once to flip and invert it.

```cpp
class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
        int m = image.size();
        int n = image[0].size();
        
        // Iterate over each row
        for (int i = 0; i < m; i++) {
            // Flip and invert the row
            for (int j = 0; j < (n + 1) / 2; j++) {
                int left = image[i][j];
                int right = image[i][n - 1 - j];
                image[i][j] = 1 - right;
                image[i][n - 1 - j] = 1 - left;
            }
        }
        
        return image;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns. This is because we iterate over each element in the image once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the indices.
> - **Optimality proof:** The time complexity is optimal because we need to visit each element in the image at least once to flip and invert it. The space complexity is optimal because we only use a constant amount of space to store the indices.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Flipping and inverting an image.
- Problem-solving patterns identified: Combining multiple operations into one step to improve efficiency.
- Optimization techniques learned: Reducing the number of passes over the data.
- Similar problems to practice: Flipping an image horizontally or vertically, inverting an image.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty image.
- Edge cases to watch for: An image with an odd number of columns, an image with only one row or column.
- Performance pitfalls: Using unnecessary extra space or making unnecessary extra passes over the data.
- Testing considerations: Testing the function with different sizes of images, testing the function with images that have different numbers of rows and columns.