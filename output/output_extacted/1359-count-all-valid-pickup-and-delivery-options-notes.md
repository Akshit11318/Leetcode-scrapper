## Count All Valid Pickup and Delivery Options
**Problem Link:** https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description

**Problem Statement:**
- Input format: `n`, the number of orders.
- Constraints: `1 <= n <= 8`.
- Expected output format: The number of valid pickup and delivery options.
- Key requirements: Each order has a unique pickup and delivery location. 
- Example test cases: For `n = 1`, there is only one valid option, which is to pick up the order first and then deliver it. For `n = 2`, there are two valid options for each order (pick up or deliver), resulting in a total of $2 \times 2 = 4$ options. However, since the two orders are distinct, we need to consider the sequence of pickup and delivery for each order.

---

### Brute Force Approach
**Explanation:**
- The brute force approach involves generating all possible permutations of pickup and delivery locations for `n` orders.
- We can use a recursive function or a backtracking algorithm to generate these permutations.
- For each permutation, we check if it satisfies the condition of having a pickup location before its corresponding delivery location.

```cpp
#include <iostream>
#include <vector>

using namespace std;

int countOrders(int n) {
    vector<int> result;
    vector<bool> visited(2 * n, false);
    vector<int> path;
    countOrdersHelper(n, path, visited, result);
    return result.size();
}

void countOrdersHelper(int n, vector<int>& path, vector<bool>& visited, vector<int>& result) {
    if (path.size() == 2 * n) {
        result.push_back(1);
        return;
    }
    for (int i = 0; i < 2 * n; ++i) {
        if (!visited[i]) {
            visited[i] = true;
            path.push_back(i);
            if (isValid(path)) {
                countOrdersHelper(n, path, visited, result);
            }
            path.pop_back();
            visited[i] = false;
        }
    }
}

bool isValid(vector<int>& path) {
    int pickupCount = 0;
    for (int i = 0; i < path.size(); ++i) {
        if (path[i] % 2 == 0) {
            pickupCount++;
        } else {
            if (pickupCount <= path[i] / 2) {
                return false;
            }
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O((2n)!)$, because we are generating all possible permutations of `2n` locations.
> - **Space Complexity:** $O(2n)$, for storing the recursion stack and the path.
> - **Why these complexities occur:** The brute force approach generates all possible permutations, resulting in a high time complexity. The space complexity is due to the recursion stack and the storage of the path.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach uses dynamic programming and combinatorial mathematics to calculate the number of valid pickup and delivery options.
- For `n` orders, we have `2n` locations in total (pickup and delivery).
- We can use the formula for permutations with restriction to calculate the number of valid options.
- The idea is to place the pickup locations first and then the delivery locations, ensuring that each delivery location is placed after its corresponding pickup location.

```cpp
#include <iostream>

using namespace std;

long long countOrders(int n) {
    long long result = 1;
    for (int i = 1; i <= n; ++i) {
        result *= (2 * i - 1) * (2 * i);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because we are using a simple loop to calculate the result.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the result.
> - **Optimality proof:** This approach is optimal because it directly calculates the number of valid options using combinatorial mathematics, avoiding the need to generate all permutations. The time complexity is linear, making it efficient for small values of `n`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: combinatorial mathematics, permutations with restriction, and dynamic programming.
- Problem-solving patterns identified: using mathematical formulas to avoid generating all permutations.
- Optimization techniques learned: using combinatorial mathematics to reduce the time complexity.

**Mistakes to Avoid:**
- Common implementation errors: not considering the restriction on the placement of delivery locations.
- Edge cases to watch for: handling the base case when `n` is 1.
- Performance pitfalls: using a brute force approach for large values of `n`.
- Testing considerations: testing the function with different values of `n` to ensure correctness.