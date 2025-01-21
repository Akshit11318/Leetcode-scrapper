## Find Smallest Common Element in All Rows
**Problem Link:** https://leetcode.com/problems/find-smallest-common-element-in-all-rows/description

**Problem Statement:**
- Input format: A 2D integer array `mat` where each row is sorted in ascending order.
- Constraints: `1 <= mat.length <= 100`, `1 <= mat[i].length <= 100`, `1 <= mat[i][j] <= 100`.
- Expected output format: The smallest common element in all rows. If no common element is found, return `-1`.
- Key requirements and edge cases to consider: 
  - All rows must have at least one common element.
  - If no common element exists, return `-1`.
- Example test cases with explanations:
  - `mat = [[1,2,3],[2,3,4],[2,3,5]]`, output: `2` because `2` is the smallest common element in all rows.
  - `mat = [[1,2,3],[4,5,6]]`, output: `-1` because no common element exists in all rows.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate through each element in the first row and check if it exists in all other rows.
- Step-by-step breakdown of the solution:
  1. Start with the first element of the first row.
  2. Iterate through each row (except the first) and check if the current element exists in that row using a linear search.
  3. If the element is found in all rows, return it as the smallest common element.
  4. If not, move to the next element in the first row and repeat the process.
- Why this approach comes to mind first: It's a straightforward, intuitive approach that checks every possible common element.

```cpp
class Solution {
public:
    int smallestCommonElement(vector<vector<int>>& mat) {
        for (int num : mat[0]) {
            bool common = true;
            for (int i = 1; i < mat.size(); i++) {
                bool found = false;
                for (int j = 0; j < mat[i].size(); j++) {
                    if (mat[i][j] == num) {
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    common = false;
                    break;
                }
            }
            if (common) {
                return num;
            }
        }
        return -1; // No common element found
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m^2)$ where $n$ is the number of columns in the first row and $m$ is the number of rows. This is because for each element in the first row, we potentially iterate through each row (except the first) and for each of those rows, we perform a linear search.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the current element and the boolean flags.
> - **Why these complexities occur:** The time complexity is high due to the nested loops and linear search within the inner loop. The space complexity is constant because we don't use any data structures that scale with input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Since each row is sorted, we can use binary search to find if an element exists in a row, significantly reducing the time complexity.
- Detailed breakdown of the approach:
  1. Iterate through each element in the first row.
  2. For each element, use binary search to check if it exists in all other rows.
  3. If an element is found in all rows, return it as the smallest common element.
- Proof of optimality: This approach is optimal because it minimizes the number of comparisons needed to find a common element by leveraging the sorted nature of the rows and using binary search.

```cpp
class Solution {
public:
    int smallestCommonElement(vector<vector<int>>& mat) {
        for (int num : mat[0]) {
            bool common = true;
            for (int i = 1; i < mat.size(); i++) {
                if (binarySearch(mat[i], num) == -1) {
                    common = false;
                    break;
                }
            }
            if (common) {
                return num;
            }
        }
        return -1; // No common element found
    }
    
    int binarySearch(vector<int>& row, int target) {
        int left = 0, right = row.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (row[mid] == target) {
                return mid;
            } else if (row[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1; // Target not found
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \log k)$ where $n$ is the number of columns in the first row, $m$ is the number of rows, and $k$ is the average number of columns in the other rows. This is because for each element in the first row, we perform a binary search in each of the other rows.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the indices and the boolean flag.
> - **Optimality proof:** This is the optimal approach because it leverages the sorted nature of the rows to minimize the number of comparisons needed to find a common element, resulting in a significant reduction in time complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, iteration through sorted arrays.
- Problem-solving patterns identified: Leveraging the structure of the input (sorted rows) to optimize the solution.
- Optimization techniques learned: Using binary search instead of linear search to find elements in sorted arrays.
- Similar problems to practice: Other problems involving finding common elements in sorted arrays or matrices.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing binary search or not handling edge cases properly.
- Edge cases to watch for: Empty rows, rows with no common elements, or rows with duplicate elements.
- Performance pitfalls: Using linear search instead of binary search, which can significantly increase the time complexity.
- Testing considerations: Thoroughly testing the solution with various input scenarios, including edge cases.