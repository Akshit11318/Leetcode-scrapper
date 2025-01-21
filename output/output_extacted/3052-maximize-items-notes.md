## Maximize Items
**Problem Link:** https://leetcode.com/problems/maximize-items/description

**Problem Statement:**
- Input format and constraints: You are given two integers `bags` and `items`, where `bags` represents the number of bags and `items` represents the number of items. Each item has a weight and a value. You are also given a list of integers `capacity` representing the capacity of each bag.
- Expected output format: The maximum number of items that can be put in the bags.
- Key requirements and edge cases to consider: The total weight of items in each bag cannot exceed the capacity of the bag. Each item can only be used once.
- Example test cases with explanations: 
    - Input: `bags = 2, items = 4, capacity = [1, 2], weights = [1, 2, 1, 2], values = [1, 2, 1, 2]`
    - Output: `4`
    - Explanation: We can put one item of weight 1 and value 1 in the first bag, and one item of weight 1 and value 1 and two items of weight 1 and value 1 in the second bag.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to try all possible combinations of items and bags.
- Step-by-step breakdown of the solution: 
    1. Generate all possible combinations of items.
    2. For each combination, try to put the items in the bags.
    3. If the total weight of items in a bag does not exceed the capacity of the bag, update the maximum number of items.
- Why this approach comes to mind first: This approach is simple and easy to understand, but it has a high time complexity.

```cpp
#include <iostream>
#include <vector>

using namespace std;

int maxItems(int bags, int items, vector<int>& capacity, vector<int>& weights) {
    int max_items = 0;
    for (int i = 0; i < (1 << items); i++) {
        vector<int> bag_weights(bags, 0);
        int item_count = 0;
        for (int j = 0; j < items; j++) {
            if ((i & (1 << j)) != 0) {
                bool placed = false;
                for (int k = 0; k < bags; k++) {
                    if (bag_weights[k] + weights[j] <= capacity[k]) {
                        bag_weights[k] += weights[j];
                        placed = true;
                        break;
                    }
                }
                if (placed) {
                    item_count++;
                }
            }
        }
        max_items = max(max_items, item_count);
    }
    return max_items;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m)$, where $n$ is the number of items and $m$ is the number of bags. This is because we generate all possible combinations of items and for each combination, we try to put the items in the bags.
> - **Space Complexity:** $O(m)$, where $m$ is the number of bags. This is because we need to store the weights of items in each bag.
> - **Why these complexities occur:** The time complexity is high because we generate all possible combinations of items, and for each combination, we try to put the items in the bags. The space complexity is relatively low because we only need to store the weights of items in each bag.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to solve this problem. We sort the items by their weights and then try to put the items in the bags.
- Detailed breakdown of the approach: 
    1. Sort the items by their weights.
    2. Try to put the items in the bags. For each item, we try to put it in the bag with the most remaining capacity.
- Proof of optimality: This approach is optimal because we always try to put the item with the smallest weight in the bag with the most remaining capacity. This ensures that we can put the maximum number of items in the bags.
- Why further optimization is impossible: This approach is already optimal because we always make the best possible choice for each item.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxItems(int bags, int items, vector<int>& capacity, vector<int>& weights) {
    vector<pair<int, int>> sorted_weights;
    for (int i = 0; i < items; i++) {
        sorted_weights.push_back({weights[i], i});
    }
    sort(sorted_weights.begin(), sorted_weights.end());
    vector<int> remaining_capacity = capacity;
    int max_items = 0;
    for (auto& weight : sorted_weights) {
        for (int i = 0; i < bags; i++) {
            if (remaining_capacity[i] >= weight.first) {
                remaining_capacity[i] -= weight.first;
                max_items++;
                break;
            }
        }
    }
    return max_items;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + n \cdot m)$, where $n$ is the number of items and $m$ is the number of bags. This is because we sort the items by their weights and then try to put the items in the bags.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of items and $m$ is the number of bags. This is because we need to store the weights of items and the remaining capacity of each bag.
> - **Optimality proof:** This approach is optimal because we always try to put the item with the smallest weight in the bag with the most remaining capacity. This ensures that we can put the maximum number of items in the bags.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, sorting.
- Problem-solving patterns identified: Trying to put items in bags, sorting items by their weights.
- Optimization techniques learned: Using a greedy approach to solve the problem.
- Similar problems to practice: Other problems that involve trying to put items in bags, such as the 0/1 knapsack problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the total weight of items in a bag exceeds the capacity of the bag.
- Edge cases to watch for: When the number of bags is 0, when the number of items is 0.
- Performance pitfalls: Using a brute force approach to solve the problem.
- Testing considerations: Testing the function with different inputs, such as different numbers of bags and items, different capacities and weights.