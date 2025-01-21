## Choose Numbers from Two Arrays in Range

**Problem Link:** https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/description

**Problem Statement:**
- Input format: Two arrays `l` and `r` of the same length `n`, where `l[i]` and `r[i]` represent a range of values.
- Constraints: `1 <= n <= 10^5`, `1 <= l[i] <= r[i] <= 10^9`.
- Expected output format: The maximum number of ranges that can be chosen such that no two chosen ranges overlap.
- Key requirements and edge cases to consider: Handling overlapping ranges, ensuring non-overlapping selection, and optimizing for maximum selection.
- Example test cases with explanations:
  - Example 1: `l = [1, 3, 1, 5], r = [5, 4, 4, 6]`. The maximum number of non-overlapping ranges is 3.
  - Example 2: `l = [1, 2, 3], r = [3, 4, 5]`. The maximum number of non-overlapping ranges is 3.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of ranges and check for non-overlap.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of ranges.
  2. For each combination, check if any two ranges overlap.
  3. If no overlap is found, update the maximum count of non-overlapping ranges.
- Why this approach comes to mind first: It's a straightforward, though inefficient, way to ensure all possibilities are considered.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxNonOverlappingRanges(std::vector<int>& l, std::vector<int>& r) {
    int n = l.size();
    int maxCount = 0;
    
    // Generate all possible combinations
    for (int mask = 0; mask < (1 << n); ++mask) {
        bool isNonOverlapping = true;
        int count = 0;
        
        // Check each bit in the mask
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) != 0) {
                count++;
                
                // Check for overlap with previously selected ranges
                for (int j = 0; j < i; ++j) {
                    if ((mask & (1 << j)) != 0 && r[j] >= l[i]) {
                        isNonOverlapping = false;
                        break;
                    }
                }
            }
            
            if (!isNonOverlapping) break;
        }
        
        // Update maxCount if current combination is non-overlapping
        if (isNonOverlapping) maxCount = std::max(maxCount, count);
    }
    
    return maxCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n^2)$, where $n$ is the number of ranges. This is because we generate all possible combinations ($2^n$) and for each combination, we check for overlap ($n^2$).
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the mask, count, and maxCount variables.
> - **Why these complexities occur:** The brute force approach involves generating all possible combinations and checking each one for non-overlap, leading to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Sort the ranges by their end points and select the range with the smallest end point that does not overlap with the previously selected range.
- Detailed breakdown of the approach:
  1. Sort the ranges by their end points.
  2. Initialize the count of non-overlapping ranges to 1 (since we can always select the first range).
  3. Initialize the end point of the last selected range to the end point of the first range.
  4. Iterate through the sorted ranges. For each range, if its start point is greater than the end point of the last selected range, increment the count and update the end point of the last selected range.
- Proof of optimality: This approach ensures that we select the maximum number of non-overlapping ranges, as we always choose the range with the smallest end point that does not overlap with the previously selected range.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxNonOverlappingRanges(std::vector<int>& l, std::vector<int>& r) {
    int n = l.size();
    std::vector<std::pair<int, int>> ranges;
    
    // Create a vector of pairs to store the ranges
    for (int i = 0; i < n; ++i) {
        ranges.push_back({l[i], r[i]});
    }
    
    // Sort the ranges by their end points
    std::sort(ranges.begin(), ranges.end(), [](const auto& a, const auto& b) {
        return a.second < b.second;
    });
    
    int count = 1;
    int lastEnd = ranges[0].second;
    
    // Iterate through the sorted ranges
    for (int i = 1; i < n; ++i) {
        if (ranges[i].first > lastEnd) {
            count++;
            lastEnd = ranges[i].second;
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of ranges. This is because we sort the ranges by their end points.
> - **Space Complexity:** $O(n)$, as we create a vector to store the ranges.
> - **Optimality proof:** This approach ensures that we select the maximum number of non-overlapping ranges, as we always choose the range with the smallest end point that does not overlap with the previously selected range.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, sorting.
- Problem-solving patterns identified: Finding non-overlapping ranges, selecting the range with the smallest end point.
- Optimization techniques learned: Sorting the ranges by their end points.
- Similar problems to practice: Scheduling tasks, assigning resources.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the ranges correctly, not updating the end point of the last selected range.
- Edge cases to watch for: Empty input, ranges with equal start and end points.
- Performance pitfalls: Using a brute force approach, not optimizing the sorting step.
- Testing considerations: Test with different input sizes, test with overlapping and non-overlapping ranges.