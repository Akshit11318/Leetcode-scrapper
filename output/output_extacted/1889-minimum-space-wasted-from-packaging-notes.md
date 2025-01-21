## Minimum Space Wasted From Packaging
**Problem Link:** https://leetcode.com/problems/minimum-space-wasted-from-packaging/description

**Problem Statement:**
- Input format and constraints: The problem takes in an array `packaging` representing the packaging sizes available and an array `orders` representing the orders to be fulfilled. Each order is represented by an array where the first element is the number of items ordered and the second element is the item size.
- Expected output format: The function should return the minimum space wasted when packaging all orders.
- Key requirements and edge cases to consider: The function should handle cases where there are no orders or packaging sizes, and it should also handle cases where the item size is larger than any packaging size.
- Example test cases with explanations:
  - Example 1: `packaging = [2,3,5], orders = [[4,5],[4,7],[4,9]]`, output: `23`.
  - Example 2: `packaging = [3,5,8,10,11,12], orders = [[12,5],[11,9],[14,10]]`, output: `26`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves trying all possible packaging sizes for each order and calculating the minimum space wasted.
- Step-by-step breakdown of the solution:
  1. Iterate over each order.
  2. For each order, try all possible packaging sizes.
  3. Calculate the minimum space wasted for each packaging size.
  4. Return the minimum space wasted across all orders.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient for large inputs.

```cpp
int minSpaceWastedKResized(int packaging[], int packagingSize, int orders[], int ordersSize) {
    int minWasted = 0;
    for (int i = 0; i < ordersSize; i++) {
        int minWastedForOrder = INT_MAX;
        for (int j = 0; j < packagingSize; j++) {
            int wasted = 0;
            int items = orders[i][0];
            int itemSize = orders[i][1];
            while (items > 0) {
                int packs = (items + packaging[j] - 1) / packaging[j];
                wasted += packs * packaging[j] - items * itemSize;
                items = 0;
            }
            minWastedForOrder = min(minWastedForOrder, wasted);
        }
        minWasted += minWastedForOrder;
    }
    return minWasted;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of orders and $m$ is the number of packaging sizes. This is because we are iterating over each order and for each order, we are iterating over each packaging size.
> - **Space Complexity:** $O(1)$ because we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The time complexity occurs because of the nested loops, and the space complexity occurs because we are only using a constant amount of space to store the minimum wasted space.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a binary search approach to find the minimum packaging size that can fulfill each order.
- Detailed breakdown of the approach:
  1. Sort the packaging sizes in ascending order.
  2. Iterate over each order.
  3. For each order, use binary search to find the smallest packaging size that is greater than or equal to the item size.
  4. Calculate the minimum space wasted for the found packaging size.
  5. Return the minimum space wasted across all orders.
- Proof of optimality: This approach is optimal because it uses a binary search approach to find the smallest packaging size, which reduces the time complexity to $O(n \log m)$.

```cpp
int minSpaceWastedKResized(int packaging[], int packagingSize, int orders[], int ordersSize) {
    sort(packaging, packaging + packagingSize);
    int minWasted = 0;
    for (int i = 0; i < ordersSize; i++) {
        int itemSize = orders[i][1];
        int items = orders[i][0];
        int left = 0, right = packagingSize - 1;
        int minPackagingSize = INT_MAX;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (packaging[mid] >= itemSize) {
                minPackagingSize = packaging[mid];
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        if (minPackagingSize != INT_MAX) {
            int packs = (items + minPackagingSize - 1) / minPackagingSize;
            minWasted += packs * minPackagingSize - items * itemSize;
        } else {
            minWasted += items * itemSize;
        }
    }
    return minWasted;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log m)$ where $n$ is the number of orders and $m$ is the number of packaging sizes. This is because we are iterating over each order and for each order, we are using binary search to find the smallest packaging size.
> - **Space Complexity:** $O(1)$ because we are not using any extra space that scales with the input size.
> - **Optimality proof:** This approach is optimal because it uses a binary search approach to find the smallest packaging size, which reduces the time complexity to $O(n \log m)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, sorting.
- Problem-solving patterns identified: Using a binary search approach to find the smallest packaging size.
- Optimization techniques learned: Reducing the time complexity by using a binary search approach.
- Similar problems to practice: Problems that involve finding the minimum or maximum value in an array using a binary search approach.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as when the item size is larger than any packaging size.
- Edge cases to watch for: When the item size is larger than any packaging size, when there are no orders or packaging sizes.
- Performance pitfalls: Using a brute force approach, which can result in a high time complexity.
- Testing considerations: Testing the function with different inputs, such as different packaging sizes and orders, to ensure that it works correctly in all cases.