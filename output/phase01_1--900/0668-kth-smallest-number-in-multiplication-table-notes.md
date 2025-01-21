## Kth Smallest Number in Multiplication Table
**Problem Link:** https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description

**Problem Statement:**
- Input format: Given integers `m` and `n`, and an integer `k`, find the `k`-th smallest number in the multiplication table of size `m x n`.
- Expected output format: The `k`-th smallest number.
- Key requirements and edge cases to consider:
  - The multiplication table is a matrix where each cell `[i][j]` contains the product of `i` and `j`.
  - `1 <= m, n <= 3 * 10^4`, `1 <= k <= m * n`.
- Example test cases with explanations:
  - For `m = 3`, `n = 3`, `k = 5`, the multiplication table is:
    ```
    1  2  3
    2  4  6
    3  6  9
    ```
    The `5`-th smallest number is `5`, which does not exist in the table, so we should return the `5`-th smallest number that does exist, which is `5` is not in the table but `3` is the 5th smallest number.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create the multiplication table and sort all the numbers to find the `k`-th smallest.
- Step-by-step breakdown of the solution:
  1. Create a vector to store all the products.
  2. Iterate through each cell in the multiplication table, calculating the product and adding it to the vector.
  3. Sort the vector.
  4. Return the `k`-th smallest number.
- Why this approach comes to mind first: It directly solves the problem by generating all possible products and sorting them.

```cpp
class Solution {
public:
    int findKthNumber(int m, int n, int k) {
        vector<int> products;
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                products.push_back(i * j);
            }
        }
        sort(products.begin(), products.end());
        return products[k - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n \cdot \log(m \cdot n))$, where $m \cdot n$ is the number of elements in the multiplication table, and $\log(m \cdot n)$ is the time complexity of sorting.
> - **Space Complexity:** $O(m \cdot n)$, as we need to store all the products in the vector.
> - **Why these complexities occur:** The brute force approach requires generating all possible products, storing them, and sorting them, which leads to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting all products, we can use a binary search approach to find the `k`-th smallest number.
- Detailed breakdown of the approach:
  1. Define the search range `[1, m * n]`.
  2. For each mid value in the search range, count how many numbers in the multiplication table are less than or equal to mid.
  3. If the count is greater than or equal to `k`, update the upper bound of the search range to mid.
  4. If the count is less than `k`, update the lower bound of the search range to mid + 1.
  5. Repeat steps 2-4 until the search range contains only one number, which is the `k`-th smallest number.
- Proof of optimality: This approach has a time complexity of $O(m \cdot \log(m \cdot n))$, which is optimal because we need to consider all rows in the worst case.

```cpp
class Solution {
public:
    int findKthNumber(int m, int n, int k) {
        int left = 1, right = m * n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            int count = 0;
            int j = n;
            for (int i = 1; i <= m; ++i) {
                while (j >= 1 && i * j > mid) {
                    --j;
                }
                count += j;
            }
            if (count < k) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot \log(m \cdot n))$, where $m$ is the number of rows in the multiplication table, and $\log(m \cdot n)$ is the number of iterations in the binary search.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the search range and the count.
> - **Optimality proof:** This approach is optimal because we need to consider all rows in the worst case, and the binary search approach reduces the number of iterations to $\log(m \cdot n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, counting numbers in a range.
- Problem-solving patterns identified: Using binary search to find the `k`-th smallest number in an unsorted array.
- Optimization techniques learned: Reducing the search space using binary search.
- Similar problems to practice: Finding the `k`-th smallest number in a sorted array, finding the median of an unsorted array.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the search range correctly, not counting the numbers in the range correctly.
- Edge cases to watch for: When `k` is 1 or `m * n`, when `m` or `n` is 1.
- Performance pitfalls: Using a brute force approach instead of binary search.
- Testing considerations: Testing with different values of `m`, `n`, and `k`, testing with edge cases.