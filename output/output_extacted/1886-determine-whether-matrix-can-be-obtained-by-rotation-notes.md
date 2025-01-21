## Determine Whether Matrix Can Be Obtained By Rotation

**Problem Link:** https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description

**Problem Statement:**
- Input: Two `n x n` matrices, `mat` and `target`.
- Constraints: `n == mat.length == mat[i].length == target.length == target[i].length`, `1 <= n <= 10`, `1 <= mat[i][j] <= 10^9`, `1 <= target[i][j] <= 10^9`.
- Expected output: `true` if `target` can be obtained by rotating `mat` by `90`, `180`, `270`, or `360` degrees; `false` otherwise.
- Key requirements: Compare the matrices after each possible rotation to determine if `target` can be obtained.

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible rotations of `mat` to see if any match `target`.
- Step-by-step breakdown:
  1. Define a function to rotate a matrix by `90` degrees.
  2. Check if `target` matches `mat` after `0`, `1`, `2`, or `3` rotations.
  3. If any rotation matches, return `true`; otherwise, return `false`.

```cpp
#include <vector>
using namespace std;

bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
    int n = mat.size();
    
    // Function to rotate matrix by 90 degrees
    void rotate(vector<vector<int>>& matrix) {
        vector<vector<int>> temp(n, vector<int>(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                temp[j][n - 1 - i] = matrix[i][j];
            }
        }
        matrix = temp;
    }
    
    // Check for all rotations
    for (int i = 0; i < 4; i++) {
        if (mat == target) return true;
        rotate(mat);
    }
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the size of the matrix and $k$ is the number of rotations checked (in this case, $k = 4$). The rotation operation itself is $O(n^2)$, and we perform it $k$ times.
> - **Space Complexity:** $O(n^2)$ for storing the temporary rotated matrix.
> - **Why these complexities occur:** The time complexity is due to the rotation operation and the comparison of matrices after each rotation. The space complexity is due to the storage of the temporary rotated matrix.

### Optimal Approach (Required)

**Explanation:**
- The key insight is recognizing that we can achieve the rotations by simply checking the original matrix and its rotations without modifying it.
- Detailed breakdown:
  1. Check if `target` matches `mat` directly.
  2. Perform a single rotation of `mat` and compare it with `target`.
  3. Repeat the rotation and comparison two more times for a total of four checks (including the original position).

```cpp
bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
    int n = mat.size();
    
    // Function to rotate matrix by 90 degrees
    void rotate(vector<vector<int>>& matrix) {
        vector<vector<int>> temp(n, vector<int>(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                temp[j][n - 1 - i] = matrix[i][j];
            }
        }
        matrix = temp;
    }
    
    // Check for all rotations without modifying the original matrix
    vector<vector<int>> matCopy = mat;
    for (int i = 0; i < 4; i++) {
        if (matCopy == target) return true;
        rotate(matCopy);
    }
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the size of the matrix and $k$ is the number of rotations checked (in this case, $k = 4$). This is the same as the brute force approach because the operations are essentially the same but with a clearer separation of concerns.
> - **Space Complexity:** $O(n^2)$ for storing the copy of the matrix to be rotated.
> - **Optimality proof:** This approach is optimal because it checks all possible rotations exactly once and does not perform any redundant operations. The time and space complexities are minimal given the problem constraints.

### Final Notes

**Learning Points:**
- Recognizing the importance of checking all possible rotations of a matrix in a problem.
- Understanding how to implement matrix rotation efficiently.
- Realizing the need to preserve the original data when performing transformations for comparison.

**Mistakes to Avoid:**
- Failing to consider all possible rotations.
- Modifying the original data unnecessarily.
- Not checking for equality after each rotation.
- Not considering the space complexity of temporary matrices.