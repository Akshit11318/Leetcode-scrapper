## Rank Transform of a Matrix

**Problem Link:** https://leetcode.com/problems/rank-transform-of-a-matrix/description

**Problem Statement:**
- Input: A `matrix` of integers, where each element is unique.
- Output: A new matrix where each element is replaced by its `rank` in the sorted list of all elements in the matrix. The `rank` of an element is its 1-based index in the sorted list.
- Key requirements and edge cases to consider:
  - The input matrix can be empty.
  - The input matrix can have a single row or column.
  - The elements in the matrix are unique.
- Example test cases with explanations:
  - For example, given a matrix `[[1, 2], [3, 4]]`, the output should be `[[1, 2], [3, 4]]` because the sorted list of elements is `[1, 2, 3, 4]`.
  - For example, given a matrix `[[7, 7], [7, 7]]`, the output should be `[[1, 1], [1, 1]]` because all elements are the same.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Sort all elements in the matrix and then replace each element with its 1-based index in the sorted list.
- Step-by-step breakdown of the solution:
  1. Flatten the matrix into a vector.
  2. Sort the vector.
  3. Create a map to store the rank of each element.
  4. Replace each element in the matrix with its rank.

```cpp
#include <vector>
#include <algorithm>
#include <unordered_map>

std::vector<std::vector<int>> matrixRankTransform(std::vector<std::vector<int>>& matrix) {
    int m = matrix.size();
    int n = matrix[0].size();
    std::vector<int> flat;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            flat.push_back(matrix[i][j]);
        }
    }
    std::sort(flat.begin(), flat.end());
    std::unordered_map<int, int> rankMap;
    for (int i = 0; i < flat.size(); ++i) {
        rankMap[flat[i]] = i + 1;
    }
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            matrix[i][j] = rankMap[matrix[i][j]];
        }
    }
    return matrix;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(mn \log (mn))$ due to sorting the vector of $mn$ elements.
> - **Space Complexity:** $O(mn)$ for storing the flattened vector and the rank map.
> - **Why these complexities occur:** The sorting step dominates the time complexity, while the space complexity comes from the need to store all elements in the matrix for sorting and ranking.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved in linear time by using a single pass through the matrix to populate a map with the elements as keys and their ranks as values, and then another pass to replace each element with its rank. However, this approach still requires sorting, which is not linear. A truly optimal approach involves recognizing that the problem can be solved by sorting the unique elements and then replacing each element with its 1-based index in the sorted list of unique elements.
- Detailed breakdown of the approach:
  1. Flatten the matrix into a vector.
  2. Use a set to get unique elements and sort them.
  3. Create a map to store the rank of each unique element.
  4. Replace each element in the matrix with its rank.
- Proof of optimality: This approach is optimal because it minimizes the number of operations required to solve the problem. Sorting the unique elements is necessary to determine their ranks, and using a map to store the ranks allows for efficient replacement of elements in the matrix.

```cpp
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <set>

std::vector<std::vector<int>> matrixRankTransform(std::vector<std::vector<int>>& matrix) {
    int m = matrix.size();
    int n = matrix[0].size();
    std::set<int> unique;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            unique.insert(matrix[i][j]);
        }
    }
    std::vector<int> sortedUnique(unique.begin(), unique.end());
    std::sort(sortedUnique.begin(), sortedUnique.end());
    std::unordered_map<int, int> rankMap;
    for (int i = 0; i < sortedUnique.size(); ++i) {
        rankMap[sortedUnique[i]] = i + 1;
    }
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            matrix[i][j] = rankMap[matrix[i][j]];
        }
    }
    return matrix;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(mn + k \log k)$, where $k$ is the number of unique elements. This is because we first collect all unique elements ($O(mn)$), then sort them ($O(k \log k)$), and finally replace each element with its rank ($O(mn)$).
> - **Space Complexity:** $O(mn + k)$ for storing the unique elements, the sorted list of unique elements, and the rank map.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to solve the problem. Sorting the unique elements is necessary to determine their ranks, and using a map to store the ranks allows for efficient replacement of elements in the matrix.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, using sets for uniqueness, and maps for efficient lookup.
- Problem-solving patterns identified: The importance of identifying unique elements and sorting them to solve ranking problems.
- Optimization techniques learned: Minimizing the number of operations by sorting only unique elements and using a map for efficient replacement.
- Similar problems to practice: Other ranking problems, such as ranking elements in an array or finding the rank of a specific element.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as an empty matrix or a matrix with a single row or column.
- Edge cases to watch for: Matrices with duplicate elements (though the problem statement specifies unique elements).
- Performance pitfalls: Sorting the entire matrix instead of just the unique elements.
- Testing considerations: Thoroughly testing the solution with different matrix sizes, including edge cases.