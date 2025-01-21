## Most Beautiful Item for Each Query
**Problem Link:** https://leetcode.com/problems/most-beautiful-item-for-each-query/description

**Problem Statement:**
- Input format: You are given a 2D array `items` where `items[i] = [beauty_i, price_i]`, and a 2D array `queries` where `queries[j] = [query_j, limit_j]`.
- Constraints: `1 <= items.length <= 10^5`, `1 <= queries.length <= 10^5`, `1 <= price_i, beauty_i, query_j, limit_j <= 10^5`.
- Expected output format: For each query, find the most beautiful item whose price is less than or equal to the limit. If no such item exists, return `-1`.
- Key requirements and edge cases to consider: Handling queries where no items meet the criteria, ensuring efficient search for the most beautiful item within the limit.

**Example Test Cases:**
- Example 1: `items = [[1,2],[3,2],[2,4],[5,6],[3,5]]`, `queries = [[1,2],[2,3],[2,2],[4,3],[5,6]]`. The output should be `[2, -1, -1, -1, 5]`.
- Example 2: `items = [[1,2],[3,2],[2,4],[5,6],[3,5]]`, `queries = [[3,2],[1,2],[2,3],[4,3],[5,6]]`. The output should be `[2, 2, 3, -1, 5]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves iterating through each query and checking all items to find the most beautiful one that fits the price limit.
- For each query, we iterate through all items, compare their prices with the query limit, and keep track of the item with the highest beauty value that meets the price condition.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

vector<int> maximumBeauty(vector<vector<int>>& items, vector<vector<int>>& queries) {
    vector<int> result;
    for (auto& query : queries) {
        int maxBeauty = -1;
        for (auto& item : items) {
            if (item[1] <= query[1] && item[0] > maxBeauty) {
                maxBeauty = item[0];
            }
        }
        result.push_back(maxBeauty);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of queries and $m$ is the number of items. This is because for each query, we potentially check all items.
> - **Space Complexity:** $O(n)$, for storing the results of the queries.
> - **Why these complexities occur:** The brute force approach involves nested loops, one for iterating through queries and another for iterating through items for each query, leading to the $O(n \cdot m)$ time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight here is to first sort the items based on their prices. This allows us to use a more efficient algorithm to find the most beautiful item for each query.
- We can then use a binary search approach to find the most beautiful item that fits within the price limit for each query.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

vector<int> maximumBeauty(vector<vector<int>>& items, vector<vector<int>>& queries) {
    // Sort items by price
    sort(items.begin(), items.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });

    vector<int> result;
    for (auto& query : queries) {
        int maxBeauty = -1;
        // Binary search to find the first item that exceeds the price limit
        int left = 0, right = items.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (items[mid][1] <= query[1]) {
                maxBeauty = max(maxBeauty, items[mid][0]);
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        result.push_back(maxBeauty);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log m + m \log m)$, where $n$ is the number of queries and $m$ is the number of items. The $m \log m$ comes from sorting the items, and $n \log m$ comes from the binary search for each query.
> - **Space Complexity:** $O(n)$, for storing the results of the queries.
> - **Optimality proof:** This approach is optimal because it reduces the search space significantly by sorting the items and using binary search, which is the most efficient way to find an item in a sorted list.

---

### Final Notes

**Learning Points:**
- The importance of sorting and binary search in reducing complexity.
- How to approach problems that involve finding maximum or minimum values within certain constraints.
- The trade-off between time and space complexity in algorithm design.

**Mistakes to Avoid:**
- Not considering the constraints and edge cases thoroughly.
- Not optimizing the search process, leading to inefficient algorithms.
- Not validating the input and handling potential errors.