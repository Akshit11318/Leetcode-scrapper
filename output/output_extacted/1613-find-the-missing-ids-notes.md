## Find the Missing IDs

**Problem Link:** https://leetcode.com/problems/find-the-missing-ids/description

**Problem Statement:**
- Input format and constraints: The problem involves finding missing IDs in a list of integers, where each integer represents an ID. The input is a list of integers, and the constraint is that the IDs are non-negative integers.
- Expected output format: The expected output is a list of missing IDs in the range of the given IDs.
- Key requirements and edge cases to consider: The key requirement is to find all missing IDs in the range of the given IDs. Edge cases include an empty input list, a list with a single element, and a list with duplicate IDs.
- Example test cases with explanations:
  - Example 1: Input: `[4, 3, 2, 7, 8, 2, 3, 1]`, Output: `[5, 6]`. Explanation: The missing IDs in the range of the given IDs are 5 and 6.
  - Example 2: Input: `[]`, Output: `[]`. Explanation: The input list is empty, so there are no missing IDs.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought process is to sort the input list and then iterate over the sorted list to find missing IDs.
- Step-by-step breakdown of the solution:
  1. Sort the input list in ascending order.
  2. Initialize an empty list to store the missing IDs.
  3. Iterate over the sorted list, and for each ID, check if the next ID is missing.
  4. If the next ID is missing, add it to the list of missing IDs.
- Why this approach comes to mind first: This approach comes to mind first because it is a straightforward and intuitive solution to the problem.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> findMissingIds(std::vector<int>& nums) {
    std::sort(nums.begin(), nums.end());
    std::vector<int> missingIds;
    for (int i = 0; i < nums.size() - 1; i++) {
        int diff = nums[i + 1] - nums[i];
        if (diff > 1) {
            for (int j = 1; j < diff; j++) {
                missingIds.push_back(nums[i] + j);
            }
        }
    }
    return missingIds;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of IDs in the input list. The subsequent for loop has a time complexity of $O(n)$, but it is dominated by the sorting operation.
> - **Space Complexity:** $O(n)$ for the sorting operation and the output list of missing IDs.
> - **Why these complexities occur:** The time complexity occurs because the sorting operation dominates the solution. The space complexity occurs because we need to store the sorted list and the output list of missing IDs.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a `std::set` to store the IDs and then iterate over the range of IDs to find missing IDs.
- Detailed breakdown of the approach:
  1. Create a `std::set` to store the IDs.
  2. Iterate over the input list and add each ID to the `std::set`.
  3. Initialize an empty list to store the missing IDs.
  4. Iterate over the range of IDs, and for each ID, check if it is in the `std::set`.
  5. If the ID is not in the `std::set`, add it to the list of missing IDs.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

```cpp
#include <iostream>
#include <vector>
#include <set>

std::vector<int> findMissingIds(std::vector<int>& nums) {
    std::set<int> idSet;
    for (int num : nums) {
        idSet.insert(num);
    }
    std::vector<int> missingIds;
    int minId = *idSet.begin();
    int maxId = *idSet.rbegin();
    for (int i = minId; i <= maxId; i++) {
        if (idSet.find(i) == idSet.end()) {
            missingIds.push_back(i);
        }
    }
    return missingIds;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of IDs in the input list. The `std::set` operations (insert and find) have an average time complexity of $O(1)$.
> - **Space Complexity:** $O(n)$ for the `std::set` and the output list of missing IDs.
> - **Optimality proof:** The time complexity is optimal because we only need to iterate over the input list once to add IDs to the `std::set`, and then iterate over the range of IDs once to find missing IDs.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of sorting and `std::set` operations to solve the problem efficiently.
- Problem-solving patterns identified: The problem requires identifying the range of IDs and then finding missing IDs within that range.
- Optimization techniques learned: The optimal solution uses a `std::set` to store IDs, which reduces the time complexity from $O(n \log n)$ to $O(n)$.
- Similar problems to practice: Similar problems include finding missing numbers in a list, finding duplicate IDs, and finding the maximum or minimum ID in a list.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to use a sorting-based approach, which has a higher time complexity than the optimal solution.
- Edge cases to watch for: Edge cases include an empty input list, a list with a single element, and a list with duplicate IDs.
- Performance pitfalls: A performance pitfall is to use a brute force approach, which has a higher time complexity than the optimal solution.
- Testing considerations: Testing considerations include testing the solution with different input lists, including edge cases, to ensure that it produces the correct output.