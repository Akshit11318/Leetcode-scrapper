## Find the Kth Smallest Sum of a Matrix with Sorted Rows

**Problem Link:** https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/description

**Problem Statement:**
- Input: A `matrix` with `m` rows and `n` columns, and an integer `k`.
- The `matrix` has sorted rows.
- Expected output: The `kth` smallest sum of a submatrix of size `1x1` to `m x n`.
- Key requirements: Find the `kth` smallest sum efficiently.
- Edge cases: Empty matrix, `k` is out of bounds, etc.

**Example Test Cases:**
- Input: `matrix = [[1, 3, 11], [2, 4, 6]]`, `k = 5`
- Output: `7`
- Explanation: The smallest sums are: `[1, 2, 3, 4, 6]`, so the `5th` smallest sum is `7`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible submatrices and calculate their sums.
- Then, sort these sums and find the `kth` smallest sum.
- This approach comes to mind first because it is straightforward and easy to understand.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int kthSmallestSum(std::vector<std::vector<int>>& matrix, int k) {
    int m = matrix.size();
    int n = matrix[0].size();
    std::vector<int> sums;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            for (int x = i; x < m; x++) {
                for (int y = j; y < n; y++) {
                    int sum = 0;
                    for (int a = i; a <= x; a++) {
                        for (int b = j; b <= y; b++) {
                            sum += matrix[a][b];
                        }
                    }
                    sums.push_back(sum);
                }
            }
        }
    }

    std::sort(sums.begin(), sums.end());
    return sums[k - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2 \cdot n^2 \cdot log(m^2 \cdot n^2))$ due to generating all possible submatrices and sorting the sums.
> - **Space Complexity:** $O(m^2 \cdot n^2)$ for storing the sums of all submatrices.
> - **Why these complexities occur:** The brute force approach generates all possible submatrices, which results in a large number of sums to sort.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a min-heap to store the sums of submatrices.
- We start with the sum of the first element of each row and then expand the submatrix by adding the next element of each row.
- We use a min-heap to keep track of the smallest sums and ensure that we always consider the smallest sum when expanding the submatrix.
- This approach is optimal because it avoids generating all possible submatrices and only considers the smallest sums.

```cpp
#include <iostream>
#include <vector>
#include <queue>

struct Node {
    int sum;
    std::vector<int> indices;
};

struct Compare {
    bool operator()(const Node& a, const Node& b) {
        return a.sum > b.sum;
    }
};

int kthSmallestSum(std::vector<std::vector<int>>& matrix, int k) {
    int m = matrix.size();
    int n = matrix[0].size();
    std::priority_queue<Node, std::vector<Node>, Compare> minHeap;

    for (int i = 0; i < m; i++) {
        Node node;
        node.sum = matrix[i][0];
        node.indices = {i, 0};
        minHeap.push(node);
    }

    for (int i = 0; i < k - 1; i++) {
        Node node = minHeap.top();
        minHeap.pop();

        for (int j = 0; j < node.indices.size(); j++) {
            if (node.indices[j] < n - 1) {
                Node newNode;
                newNode.sum = node.sum + matrix[j][node.indices[j] + 1];
                newNode.indices = node.indices;
                newNode.indices[j]++;
                minHeap.push(newNode);
                break;
            }
        }
    }

    return minHeap.top().sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot m \cdot log(m))$ due to using a min-heap to store the smallest sums.
> - **Space Complexity:** $O(m)$ for storing the sums of submatrices in the min-heap.
> - **Optimality proof:** This approach is optimal because it avoids generating all possible submatrices and only considers the smallest sums.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a min-heap to store the smallest sums and expanding the submatrix by adding the next element of each row.
- Problem-solving patterns identified: Using a min-heap to keep track of the smallest sums and avoiding generating all possible submatrices.
- Optimization techniques learned: Using a min-heap to reduce the time complexity and avoiding unnecessary calculations.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the bounds of the matrix and not handling edge cases.
- Edge cases to watch for: Empty matrix, `k` is out of bounds, etc.
- Performance pitfalls: Generating all possible submatrices and not using a min-heap to store the smallest sums.
- Testing considerations: Testing the function with different inputs and edge cases to ensure it works correctly.