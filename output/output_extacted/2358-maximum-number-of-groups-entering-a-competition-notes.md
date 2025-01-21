## Maximum Number of Groups Entering a Competition

**Problem Link:** https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/description

**Problem Statement:**
- Input: `groups` - a list of integers representing the number of people in each group, and `threshold` - an integer representing the maximum number of people allowed to enter the competition.
- Output: The maximum number of groups that can enter the competition.
- Key requirements: The total number of people from all groups should not exceed the threshold.
- Edge cases: If the threshold is less than the number of people in any group, no groups can enter. If the threshold is 0, no groups can enter.

**Example Test Cases:**
- `groups = [10,10,10,7,5,8], threshold = 28` - The maximum number of groups that can enter is 3.
- `groups = [10,10,10,7,5,8], threshold = 20` - The maximum number of groups that can enter is 2.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of groups and check which combination has the maximum number of groups without exceeding the threshold.
- Step-by-step breakdown:
  1. Generate all possible combinations of groups.
  2. For each combination, calculate the total number of people.
  3. If the total number of people does not exceed the threshold, update the maximum number of groups.
- Why this approach comes to mind first: It is a straightforward approach that tries all possibilities.

```cpp
#include <vector>
#include <algorithm>

int maxNumberOfGroups(std::vector<int>& groups, int threshold) {
    std::sort(groups.begin(), groups.end());
    int maxGroups = 0;
    for (int i = 0; i < (1 << groups.size()); i++) {
        int totalPeople = 0;
        int currentGroups = 0;
        for (int j = 0; j < groups.size(); j++) {
            if ((i & (1 << j)) != 0) {
                totalPeople += groups[j];
                currentGroups++;
            }
        }
        if (totalPeople <= threshold && currentGroups > maxGroups) {
            maxGroups = currentGroups;
        }
    }
    return maxGroups;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of groups. This is because we generate all possible combinations of groups and for each combination, we calculate the total number of people.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum number of groups and the total number of people.
> - **Why these complexities occur:** The time complexity is high because we try all possible combinations of groups, and for each combination, we perform a linear scan to calculate the total number of people.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a greedy approach to select the groups with the smallest number of people first.
- Detailed breakdown:
  1. Sort the groups in ascending order of the number of people.
  2. Initialize the total number of people and the maximum number of groups.
  3. Iterate over the sorted groups and add each group to the total number of people if it does not exceed the threshold.
- Proof of optimality: This approach is optimal because it always selects the groups with the smallest number of people first, which maximizes the number of groups that can enter the competition.

```cpp
int maxNumberOfGroups(std::vector<int>& groups, int threshold) {
    std::sort(groups.begin(), groups.end());
    int totalPeople = 0;
    int maxGroups = 0;
    for (int group : groups) {
        if (totalPeople + group <= threshold) {
            totalPeople += group;
            maxGroups++;
        }
    }
    return maxGroups;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of groups. This is because we sort the groups and then iterate over them.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the total number of people and the maximum number of groups.
> - **Optimality proof:** This approach is optimal because it always selects the groups with the smallest number of people first, which maximizes the number of groups that can enter the competition.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, sorting.
- Problem-solving patterns identified: Always try to select the smallest items first to maximize the number of items that can be selected.
- Optimization techniques learned: Sorting the groups in ascending order of the number of people.
- Similar problems to practice: [Maximum Number of Consecutive Values You Can Make](https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/).

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the total number of people exceeds the threshold before adding a group.
- Edge cases to watch for: If the threshold is less than the number of people in any group, no groups can enter. If the threshold is 0, no groups can enter.
- Performance pitfalls: Using a brute force approach that tries all possible combinations of groups.
- Testing considerations: Test the function with different inputs, including edge cases.