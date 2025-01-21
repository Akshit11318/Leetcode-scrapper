## Convert 1D Array into 2D Array

**Problem Link:** https://leetcode.com/problems/convert-1d-array-into-2d-array/description

**Problem Statement:**
- Input: A 1D array `original` and two integers `m` and `n`, representing the number of rows and columns in the desired 2D array.
- Constraints: The length of `original` must be equal to `m * n`.
- Expected Output: A 2D array with `m` rows and `n` columns, where the elements are filled in row-major order from the `original` array.
- Key Requirements:
  - The input array `original` must have exactly `m * n` elements.
  - The output must be a 2D array with the specified number of rows and columns.
- Example Test Cases:
  - Input: `original = [1,2,3,4]`, `m = 2`, `n = 2`
    - Output: `[[1,2],[3,4]]`
  - Input: `original = [1,2,3,4,5,6]`, `m = 2`, `n = 3`
    - Output: `[[1,2,3],[4,5,6]]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over the `original` array and manually construct the 2D array by indexing into the `original` array.
- We will use two nested loops to fill in the elements of the 2D array.

```cpp
vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
    if (original.size() != m * n) {
        return {}; // Return an empty vector if the lengths do not match
    }
    
    vector<vector<int>> result(m, vector<int>(n));
    int index = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            result[i][j] = original[index++];
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the desired 2D array, respectively. This is because we iterate over each element of the `original` array once.
> - **Space Complexity:** $O(m \cdot n)$, as we need to store the resulting 2D array. This is also the minimum required space to represent the output.
> - **Why these complexities occur:** The time complexity is due to the nested loops used to fill in the elements of the 2D array, while the space complexity is due to the storage required for the output array.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is essentially the same as the brute force approach, as we must iterate over each element of the `original` array exactly once to construct the 2D array.
- However, we can simplify the code by using a single loop and calculating the row and column indices based on the current index.

```cpp
vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
    if (original.size() != m * n) {
        return {}; // Return an empty vector if the lengths do not match
    }
    
    vector<vector<int>> result(m, vector<int>(n));
    for (int i = 0; i < m * n; i++) {
        result[i / n][i % n] = original[i];
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the number of rows and columns in the desired 2D array, respectively. This is because we iterate over each element of the `original` array once.
> - **Space Complexity:** $O(m \cdot n)$, as we need to store the resulting 2D array. This is also the minimum required space to represent the output.
> - **Optimality proof:** This approach is optimal because we must iterate over each element of the `original` array at least once to construct the 2D array. The use of a single loop and calculation of row and column indices based on the current index does not change the overall time complexity.

---

### Final Notes

**Learning Points:**
- The importance of checking the lengths of the input arrays to ensure they match the expected dimensions.
- The use of nested loops or a single loop with calculated indices to fill in the elements of a 2D array.
- The concept of row-major ordering and how it applies to filling in elements of a 2D array.

**Mistakes to Avoid:**
- Not checking the lengths of the input arrays before attempting to construct the 2D array.
- Using incorrect indexing or looping structures, which can lead to incorrect results or runtime errors.
- Not considering the space complexity requirements of the problem, which can lead to inefficient solutions.