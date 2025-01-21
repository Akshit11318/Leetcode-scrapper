## Diagonal Traverse II
**Problem Link:** https://leetcode.com/problems/diagonal-traverse-ii/description

**Problem Statement:**
- Input format: A list of lists of integers, where each inner list represents a row in a 2D array.
- Constraints: The input array will have a maximum of 10 rows and 10 columns, and the integers in the array will be between 0 and 100.
- Expected output format: A list of integers representing the diagonal elements of the array, traversed in a specific order.
- Key requirements and edge cases to consider: The input array may not be a square matrix (i.e., the number of rows and columns may not be equal), and there may be empty rows or columns in the array.
- Example test cases with explanations:
  - Example 1:
    - Input: `[[1,2,3],[4,5,6],[7,8,9]]`
    - Output: `[1,4,2,7,5,3,8,6,9]`
    - Explanation: The diagonal elements of the array are traversed in a zigzag pattern, starting from the top-left corner and moving down and to the right.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can iterate over the array and calculate the diagonal elements manually.
- Step-by-step breakdown of the solution:
  1. Create a result list to store the diagonal elements.
  2. Iterate over the array, starting from the top-left corner.
  3. For each element, calculate its diagonal position using the formula `row + column`.
  4. Add the element to the result list at the calculated position.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be the most efficient solution.

```cpp
vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
    vector<int> result;
    for (int row = 0; row < nums.size(); row++) {
        for (int col = 0; col < nums[row].size(); col++) {
            int diagonal = row + col;
            while (diagonal >= result.size()) {
                result.push_back(0);
            }
            result[diagonal] = nums[row][col];
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the input array, because we are iterating over each element in the array once.
> - **Space Complexity:** $O(m \cdot n)$, because in the worst case, we may need to store all elements of the array in the result list.
> - **Why these complexities occur:** The brute force approach requires iterating over each element in the array, which leads to a time complexity of $O(m \cdot n)$. The space complexity is also $O(m \cdot n)$ because we need to store the result list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a hash map to store the diagonal elements, where the key is the diagonal position and the value is a list of elements at that position.
- Detailed breakdown of the approach:
  1. Create a hash map to store the diagonal elements.
  2. Iterate over the array, starting from the top-left corner.
  3. For each element, calculate its diagonal position using the formula `row + column`.
  4. Add the element to the list of elements at the calculated position in the hash map.
  5. Iterate over the hash map and add the elements to the result list in the correct order.
- Proof of optimality: This approach is optimal because it only requires iterating over the array once and uses a hash map to store the diagonal elements efficiently.

```cpp
vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
    unordered_map<int, vector<int>> diagonals;
    for (int row = 0; row < nums.size(); row++) {
        for (int col = 0; col < nums[row].size(); col++) {
            int diagonal = row + col;
            diagonals[diagonal].push_back(nums[row][col]);
        }
    }
    vector<int> result;
    for (const auto& pair : diagonals) {
        if (pair.first % 2 == 0) {
            reverse(pair.second.begin(), pair.second.end());
        }
        result.insert(result.end(), pair.second.begin(), pair.second.end());
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns in the input array, because we are iterating over each element in the array once and using a hash map to store the diagonal elements efficiently.
> - **Space Complexity:** $O(m \cdot n)$, because in the worst case, we may need to store all elements of the array in the hash map.
> - **Optimality proof:** This approach is optimal because it only requires iterating over the array once and uses a hash map to store the diagonal elements efficiently, resulting in a time complexity of $O(m \cdot n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, iteration over 2D arrays, and diagonal traversal.
- Problem-solving patterns identified: Using a hash map to store diagonal elements and iterating over the array once to achieve optimal time complexity.
- Optimization techniques learned: Using a hash map to store diagonal elements efficiently and iterating over the array only once.
- Similar problems to practice: Other problems involving diagonal traversal or hash maps, such as finding the diagonal sum of a matrix or counting the number of elements in a diagonal.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for empty rows or columns, not handling edge cases correctly, and not using a hash map to store diagonal elements efficiently.
- Edge cases to watch for: Empty rows or columns, non-square matrices, and matrices with a large number of rows or columns.
- Performance pitfalls: Using a brute force approach or not using a hash map to store diagonal elements efficiently, resulting in a high time complexity.
- Testing considerations: Testing the solution with different input sizes, shapes, and edge cases to ensure correctness and efficiency.