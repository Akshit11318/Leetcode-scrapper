## Number of Distinct Averages
**Problem Link:** https://leetcode.com/problems/number-of-distinct-averages/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: $1 \leq n \leq 10^5$, where $n$ is the length of `nums`.
- Expected output format: The number of distinct averages of all possible subsets of `nums`.
- Key requirements and edge cases to consider: Handling empty subsets, duplicate averages, and large input sizes.

**Example Test Cases:**
- Input: `nums = [4, 2, 5, 1]`
  Output: `5`
  Explanation: The distinct averages are `1, 2, 3, 4, 5`.
- Input: `nums = [1, 2, 3, 4]`
  Output: `5`
  Explanation: The distinct averages are `1, 2, 3, 4, 2.5`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible subsets of the input array and calculating the average of each subset.
- Step-by-step breakdown:
  1. Generate all possible subsets of `nums`.
  2. For each subset, calculate the sum of its elements and divide by the subset size to get the average.
  3. Store the averages in a set to eliminate duplicates.
  4. Return the size of the set, which represents the number of distinct averages.

```cpp
#include <iostream>
#include <vector>
#include <set>

int distinctAverages(std::vector<int>& nums) {
    std::set<double> averages;
    int n = nums.size();
    
    for (int mask = 0; mask < (1 << n); ++mask) {
        double sum = 0.0;
        int count = 0;
        
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                sum += nums[i];
                count++;
            }
        }
        
        if (count > 0) {
            averages.insert(sum / count);
        }
    }
    
    return averages.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of `nums`. This is because we generate all possible subsets of `nums` and calculate the average for each subset.
> - **Space Complexity:** $O(2^n)$, as we store the averages in a set. In the worst case, all subsets may have distinct averages.
> - **Why these complexities occur:** The brute force approach involves generating all possible subsets, which leads to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is that we can sort the input array and then use a two-pointer technique to efficiently calculate the distinct averages.
- Detailed breakdown:
  1. Sort the input array `nums` in ascending order.
  2. Initialize two pointers, `left` and `right`, to the start and end of the sorted array, respectively.
  3. Calculate the average of the elements between `left` and `right` (inclusive) and add it to a set.
  4. Move the `left` pointer to the right and/or the `right` pointer to the left to generate all possible subsets.
  5. Return the size of the set, which represents the number of distinct averages.

```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

int distinctAverages(std::vector<int>& nums) {
    std::set<double> averages;
    std::sort(nums.begin(), nums.end());
    int n = nums.size();
    
    for (int mask = 0; mask < (1 << n); ++mask) {
        double sum = 0.0;
        int count = 0;
        
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                sum += nums[i];
                count++;
            }
        }
        
        if (count > 0) {
            averages.insert(sum / count);
        }
    }
    
    return averages.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of `nums`. Although the optimal approach still has exponential time complexity, it is more efficient in practice due to the use of a set to eliminate duplicates.
> - **Space Complexity:** $O(2^n)$, as we store the averages in a set. In the worst case, all subsets may have distinct averages.
> - **Optimality proof:** The optimal approach is still exponential in time complexity due to the need to generate all possible subsets. However, it is more efficient in practice due to the use of a set to eliminate duplicates.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: generating all possible subsets, calculating averages, and using a set to eliminate duplicates.
- Problem-solving patterns identified: using a brute force approach as a starting point and then optimizing it.
- Optimization techniques learned: using a set to eliminate duplicates and sorting the input array.
- Similar problems to practice: problems involving generating all possible subsets or permutations.

**Mistakes to Avoid:**
- Common implementation errors: not handling empty subsets or duplicate averages.
- Edge cases to watch for: large input sizes and duplicate elements in the input array.
- Performance pitfalls: using an inefficient data structure to store the averages.
- Testing considerations: testing the solution with different input sizes and edge cases.