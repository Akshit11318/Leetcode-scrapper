## Diagonal Traverse
**Problem Link:** https://leetcode.com/problems/diagonal-traverse/description

**Problem Statement:**
- Input: A 2D array of integers `nums` with dimensions `m x n`.
- Constraints: `1 <= m <= 10^5`, `1 <= n <= 10^5`, `1 <= m * n <= 10^5`.
- Expected Output: A 1D array of integers representing the diagonal traversal of the input array.
- Key Requirements: Traverse the array diagonally from top-left to bottom-right, starting from the first row and moving down, then moving right.
- Edge Cases:
  - When `m = 1` or `n = 1`, the array is essentially 1D, so the output is the same as the input.
  - When `m = n`, the array is a square matrix.
- Example Test Cases:
  - Input: `[[1,2,3],[4,5,6],[7,8,9]]`
    - Output: `[1,2,4,7,5,3,6,8,9]`
  - Input: `[[1,2,3]]`
    - Output: `[1,2,3]`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate through the array and add each element to the result array based on its diagonal position.
- We can calculate the diagonal position of each element using the formula `diagonal = row + column`.
- We can use a hashmap or a 2D array to store the elements of each diagonal.

```cpp
#include <vector>
#include <unordered_map>

vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
    unordered_map<int, vector<int>> diagonals;
    int m = nums.size();
    int n = nums[0].size();
    
    // Iterate through the array and add each element to the result array based on its diagonal position.
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int diagonal = i + j;
            diagonals[diagonal].push_back(nums[i][j]);
        }
    }
    
    vector<int> result;
    // Iterate through the diagonals and add the elements to the result array.
    for (auto& pair : diagonals) {
        // Reverse the elements of the diagonal if the diagonal number is odd.
        if (pair.first % 2 == 1) {
            reverse(pair.second.begin(), pair.second.end());
        }
        result.insert(result.end(), pair.second.begin(), pair.second.end());
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the input array. This is because we iterate through each element in the array once.
> - **Space Complexity:** $O(m \cdot n)$, as in the worst case, we may need to store all elements in the hashmap.
> - **Why these complexities occur:** The time complexity occurs because we iterate through each element in the array once, and the space complexity occurs because we need to store all elements in the hashmap in the worst case.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to use a single pass through the array and store the elements of each diagonal in a vector.
- We can use a vector of vectors to store the elements of each diagonal.
- We can calculate the diagonal position of each element using the formula `diagonal = row + column`.
- We can add the elements to the result array based on the diagonal position.

```cpp
#include <vector>

vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
    int m = nums.size();
    int n = nums[0].size();
    vector<vector<int>> diagonals(m + n - 1);
    
    // Iterate through the array and add each element to the result array based on its diagonal position.
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int diagonal = i + j;
            diagonals[diagonal].push_back(nums[i][j]);
        }
    }
    
    vector<int> result;
    // Iterate through the diagonals and add the elements to the result array.
    for (int i = 0; i < m + n - 1; i++) {
        // Reverse the elements of the diagonal if the diagonal number is odd.
        if (i % 2 == 1) {
            reverse(diagonals[i].begin(), diagonals[i].end());
        }
        result.insert(result.end(), diagonals[i].begin(), diagonals[i].end());
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the input array. This is because we iterate through each element in the array once.
> - **Space Complexity:** $O(m \cdot n)$, as in the worst case, we may need to store all elements in the vector of vectors.
> - **Optimality proof:** This is the optimal solution because we only iterate through the array once and store the elements of each diagonal in a vector. We do not use any extra space that scales with the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: diagonal traversal, hashmap or vector of vectors to store elements of each diagonal.
- Problem-solving patterns identified: calculating the diagonal position of each element, reversing the elements of odd-numbered diagonals.
- Optimization techniques learned: using a single pass through the array, storing elements of each diagonal in a vector.

**Mistakes to Avoid:**
- Common implementation errors: not reversing the elements of odd-numbered diagonals, not handling edge cases correctly.
- Edge cases to watch for: when `m = 1` or `n = 1`, when `m = n`.
- Performance pitfalls: using extra space that scales with the input size, iterating through the array multiple times.
- Testing considerations: test the solution with different input sizes, test the solution with edge cases.