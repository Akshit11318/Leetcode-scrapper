## Array of Objects to Matrix
**Problem Link:** https://leetcode.com/problems/array-of-objects-to-matrix/description

**Problem Statement:**
- Input format: An array of objects, where each object contains two integers, `x` and `y`.
- Constraints: The input array will not be empty.
- Expected output format: A matrix where each row corresponds to an object in the input array, and the first column is `x`, and the second column is `y`.
- Key requirements and edge cases to consider: The input array may contain duplicate objects, and the output matrix should be a 2D array of integers.
- Example test cases:
  - Input: `[{"x": 1, "y": 2}, {"x": 3, "y": 4}]`
  - Output: `[[1, 2], [3, 4]]`
  - Explanation: The output matrix has two rows, each corresponding to an object in the input array.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The problem requires converting an array of objects to a matrix, where each object contains two integers, `x` and `y`. The brute force approach involves iterating over the input array and creating a new matrix with the corresponding `x` and `y` values.
- Step-by-step breakdown of the solution:
  1. Initialize an empty matrix.
  2. Iterate over the input array.
  3. For each object in the input array, create a new row in the matrix with the corresponding `x` and `y` values.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, as it involves a simple iteration over the input array.

```cpp
#include <vector>
using namespace std;

vector<vector<int>> arrayToMatrix(vector<vector<int>>& arr) {
    vector<vector<int>> matrix;
    for (auto& obj : arr) {
        vector<int> row;
        row.push_back(obj[0]);
        row.push_back(obj[1]);
        matrix.push_back(row);
    }
    return matrix;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of objects in the input array. This is because we are iterating over the input array once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of objects in the input array. This is because we are creating a new matrix with the same number of rows as the input array.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over the input array once, and the space complexity occurs because we are creating a new matrix with the same number of rows as the input array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a simple iteration over the input array, and the optimal solution involves using a vector of vectors to create the matrix.
- Detailed breakdown of the approach:
  1. Initialize an empty vector of vectors.
  2. Iterate over the input array.
  3. For each object in the input array, create a new row in the matrix with the corresponding `x` and `y` values.
- Proof of optimality: This solution is optimal because it involves a single iteration over the input array and uses a vector of vectors to create the matrix, which is the most efficient data structure for this problem.

```cpp
#include <vector>
using namespace std;

vector<vector<int>> arrayToMatrix(vector<vector<int>>& arr) {
    vector<vector<int>> matrix;
    for (auto& obj : arr) {
        matrix.push_back({obj[0], obj[1]});
    }
    return matrix;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of objects in the input array. This is because we are iterating over the input array once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of objects in the input array. This is because we are creating a new matrix with the same number of rows as the input array.
> - **Optimality proof:** This solution is optimal because it involves a single iteration over the input array and uses a vector of vectors to create the matrix, which is the most efficient data structure for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, vector of vectors.
- Problem-solving patterns identified: Using a vector of vectors to create a matrix.
- Optimization techniques learned: Using a single iteration over the input array.
- Similar problems to practice: Converting a matrix to an array of objects.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for empty input array.
- Edge cases to watch for: Duplicate objects in the input array.
- Performance pitfalls: Using a non-efficient data structure.
- Testing considerations: Testing with empty input array, duplicate objects, and large input array.