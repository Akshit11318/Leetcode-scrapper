## Minimized Maximum of Products Distributed to Any Store

**Problem Link:** https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `n` representing the number of stores and an integer array `quantities` representing the quantities of products in each store.
- Expected output format: The function should return the minimized maximum number of products that can be distributed to any store.
- Key requirements and edge cases to consider: The function should handle cases where the number of stores is 1 or more, and the quantities of products in each store can vary.
- Example test cases with explanations:
  - Example 1: `n = 2`, `quantities = [3, 5]`. The output should be `4` because we can distribute 3 products to the first store and 5 products to the second store, and the maximum number of products in any store is `min(3, 5) = 3` when we distribute `3` to the first store and `4` to the second store.
  - Example 2: `n = 4`, `quantities = [1, 2, 3, 4]`. The output should be `2` because we can distribute 1 product to the first store, 2 products to the second store, 3 products to the third store, and 4 products to the fourth store, and the maximum number of products in any store is `min(1, 2, 3, 4) = 1` when we distribute `1` to the first store, `1` to the second store, `1` to the third store, and `2` to the fourth store.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible distributions of products to the stores and finding the minimum maximum number of products in any store.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `min_max` to store the minimum maximum number of products in any store.
  2. Iterate over all possible distributions of products to the stores.
  3. For each distribution, calculate the maximum number of products in any store.
  4. Update `min_max` if the calculated maximum is less than the current `min_max`.
- Why this approach comes to mind first: The brute force approach is straightforward and easy to understand, but it is not efficient for large inputs.

```cpp
int minimizedMaximum(int n, vector<int>& quantities) {
    int min_max = INT_MAX;
    for (int i = 1; i <= 1000; i++) {
        int max_quantity = 0;
        for (int j = 0; j < n; j++) {
            int quantity = (quantities[j] + i - 1) / i;
            max_quantity = max(max_quantity, quantity);
        }
        min_max = min(min_max, max_quantity);
    }
    return min_max;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times 1000)$, where $n$ is the number of stores.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity is high because we are trying all possible distributions of products to the stores, and the space complexity is low because we are only using a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a binary search approach to find the minimum maximum number of products in any store.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `low` and `high`, to represent the range of possible values for the minimum maximum number of products in any store.
  2. While `low` is less than or equal to `high`, calculate the midpoint `mid`.
  3. Check if it is possible to distribute the products such that the maximum number of products in any store is less than or equal to `mid`.
  4. If it is possible, update `high` to `mid - 1`. Otherwise, update `low` to `mid + 1`.
- Proof of optimality: The binary search approach ensures that we find the minimum maximum number of products in any store in the fewest number of iterations.

```cpp
int minimizedMaximum(int n, vector<int>& quantities) {
    int low = 1;
    int high = *max_element(quantities.begin(), quantities.end());
    while (low < high) {
        int mid = low + (high - low) / 2;
        int total = 0;
        for (int quantity : quantities) {
            total += (quantity + mid - 1) / mid;
        }
        if (total <= n) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log m)$, where $n$ is the number of stores and $m$ is the maximum quantity of products in any store.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** The binary search approach ensures that we find the minimum maximum number of products in any store in the fewest number of iterations, making it the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, optimization techniques.
- Problem-solving patterns identified: Using binary search to find the minimum maximum value.
- Optimization techniques learned: Reducing the search space using binary search.
- Similar problems to practice: Other optimization problems that can be solved using binary search.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not initializing variables correctly.
- Edge cases to watch for: When the number of stores is 1, when the quantities of products in each store are equal.
- Performance pitfalls: Using a brute force approach for large inputs.
- Testing considerations: Testing the function with different inputs, including edge cases.