## Maximum Number of Groups Getting Fresh Donuts
**Problem Link:** https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers `donuts_count` representing the number of fresh donuts in each box and an integer `k` representing the number of groups. The goal is to find the maximum number of groups that can get fresh donuts.
- Expected output format: The function should return the maximum number of groups that can get fresh donuts.
- Key requirements and edge cases to consider: The total number of fresh donuts in each group should be a multiple of the number of groups, and each group should have at least one fresh donut.
- Example test cases with explanations:
  - If `donuts_count = [1,2,3]` and `k = 3`, the function should return `3` because we can give each group one fresh donut.
  - If `donuts_count = [1,2,3]` and `k = 2`, the function should return `2` because we can give one group two fresh donuts and the other group two fresh donuts.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves trying all possible combinations of groups and calculating the total number of fresh donuts in each group.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `max_groups` to store the maximum number of groups that can get fresh donuts.
  2. Iterate over all possible combinations of groups.
  3. For each combination, calculate the total number of fresh donuts in each group.
  4. Check if the total number of fresh donuts in each group is a multiple of the number of groups and if each group has at least one fresh donut.
  5. Update `max_groups` if the current combination satisfies the conditions and has more groups than the current maximum.
- Why this approach comes to mind first: The brute force approach is often the first solution that comes to mind because it involves trying all possible combinations, which guarantees finding the optimal solution if the problem has a small input size.

```cpp
#include <vector>
#include <algorithm>

int max_groups(std::vector<int>& donuts_count, int k) {
    int max_groups = 0;
    for (int i = 1; i <= k; i++) {
        std::vector<int> groups(i, 0);
        std::sort(donuts_count.rbegin(), donuts_count.rend());
        for (int j = 0; j < donuts_count.size(); j++) {
            groups[j % i] += donuts_count[j];
        }
        bool valid = true;
        for (int j = 0; j < i; j++) {
            if (groups[j] % i != 0 || groups[j] == 0) {
                valid = false;
                break;
            }
        }
        if (valid) {
            max_groups = std::max(max_groups, i);
        }
    }
    return max_groups;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$ where $n$ is the number of boxes and $k$ is the number of groups. This is because we are iterating over all possible combinations of groups and calculating the total number of fresh donuts in each group.
> - **Space Complexity:** $O(k)$ where $k$ is the number of groups. This is because we need to store the total number of fresh donuts in each group.
> - **Why these complexities occur:** The time complexity occurs because we are trying all possible combinations of groups, and the space complexity occurs because we need to store the total number of fresh donuts in each group.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves sorting the boxes in descending order of fresh donuts and then trying to distribute the donuts to the groups.
- Detailed breakdown of the approach:
  1. Sort the boxes in descending order of fresh donuts.
  2. Initialize a variable `max_groups` to store the maximum number of groups that can get fresh donuts.
  3. Iterate over all possible numbers of groups from $1$ to $k$.
  4. For each number of groups, try to distribute the donuts to the groups.
  5. If the distribution is valid (i.e., the total number of fresh donuts in each group is a multiple of the number of groups and each group has at least one fresh donut), update `max_groups`.
- Proof of optimality: The optimal solution is optimal because it tries all possible numbers of groups and distributions of donuts, and it stops as soon as it finds a valid distribution.

```cpp
#include <vector>
#include <algorithm>

int max_groups(std::vector<int>& donuts_count, int k) {
    std::sort(donuts_count.rbegin(), donuts_count.rend());
    int max_groups = 0;
    for (int i = 1; i <= k; i++) {
        int j = 0;
        int donuts = 0;
        while (j < donuts_count.size() && donuts < i) {
            donuts += donuts_count[j];
            j++;
        }
        if (donuts >= i && donuts % i == 0) {
            max_groups = i;
        } else {
            break;
        }
    }
    return max_groups;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$ where $n$ is the number of boxes and $k$ is the number of groups. This is because we are sorting the boxes and then trying all possible numbers of groups.
> - **Space Complexity:** $O(1)$ where $k$ is the number of groups. This is because we only need a constant amount of space to store the maximum number of groups.
> - **Optimality proof:** The optimal solution is optimal because it tries all possible numbers of groups and distributions of donuts, and it stops as soon as it finds a valid distribution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, iteration, and conditional statements.
- Problem-solving patterns identified: Trying all possible combinations and stopping as soon as a valid solution is found.
- Optimization techniques learned: Sorting the input and trying all possible numbers of groups.
- Similar problems to practice: Other problems that involve trying all possible combinations and stopping as soon as a valid solution is found.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the distribution is valid before updating the maximum number of groups.
- Edge cases to watch for: The case where the number of groups is $1$ and the case where the number of groups is equal to the number of boxes.
- Performance pitfalls: Trying all possible combinations of groups and distributions of donuts without stopping as soon as a valid solution is found.
- Testing considerations: Testing the function with different inputs and edge cases to ensure that it works correctly.