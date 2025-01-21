## Set Intersection Size At Least Two
**Problem Link:** https://leetcode.com/problems/set-intersection-size-at-least-two/description

**Problem Statement:**
- Input format: An array of integers `intervals` representing sets of integers.
- Constraints: `1 <= intervals.length <= 10^5`, `1 <= intervals[i].length <= 30`, `1 <= intervals[i][j] <= 10^9`.
- Expected output format: The number of pairs of sets with an intersection size of at least 2.
- Key requirements and edge cases to consider:
  - Empty intervals list.
  - Intervals with single elements.
  - Intervals with elements that do not intersect with any other intervals.
- Example test cases with explanations:
  - `intervals = [[1,2],[1,2],[1,2]]`, output: `3`.
  - `intervals = [[1,3],[1,3],[2,4],[2,4]]`, output: `4`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each pair of intervals to find intersections.
- Step-by-step breakdown of the solution:
  1. Iterate through each pair of intervals.
  2. For each pair, find the intersection by checking common elements.
  3. If the intersection size is at least 2, increment the count of pairs.
- Why this approach comes to mind first: It directly addresses the problem by checking all possible pairs of intervals.

```cpp
int intersectionSizeTwo(vector<vector<int>>& intervals) {
    int count = 0;
    for (int i = 0; i < intervals.size(); i++) {
        for (int j = i + 1; j < intervals.size(); j++) {
            set<int> intersection;
            for (int k : intervals[i]) {
                for (int l : intervals[j]) {
                    if (k == l) {
                        intersection.insert(k);
                    }
                }
            }
            if (intersection.size() >= 2) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m^2)$ where $n$ is the number of intervals and $m$ is the maximum number of elements in an interval, because for each pair of intervals, we compare each element.
> - **Space Complexity:** $O(m)$ for storing the intersection set in the worst case.
> - **Why these complexities occur:** The brute force approach involves nested loops for comparing intervals and their elements, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize a hash map to store the count of each number across all intervals, then calculate pairs with at least two common numbers efficiently.
- Detailed breakdown of the approach:
  1. Create a hash map `countMap` to store the count of each number across all intervals.
  2. Iterate through each interval and update the count in `countMap`.
  3. Calculate the number of pairs that can be formed with at least two common numbers using combinatorics.
- Proof of optimality: This approach reduces the time complexity by avoiding the need to compare each pair of intervals directly.

```cpp
int intersectionSizeTwo(vector<vector<int>>& intervals) {
    unordered_map<int, int> countMap;
    for (auto& interval : intervals) {
        for (int num : interval) {
            countMap[num]++;
        }
    }
    int count = 0;
    for (auto& [num, freq] : countMap) {
        if (freq >= 2) {
            count += (freq * (freq - 1)) / 2;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m + k)$ where $n$ is the number of intervals, $m$ is the average number of elements in an interval, and $k$ is the number of unique elements across all intervals, because we iterate through each interval and then through the unique elements.
> - **Space Complexity:** $O(k)$ for storing the count of each unique number.
> - **Optimality proof:** This approach is optimal because it avoids unnecessary comparisons and directly calculates the number of pairs with at least two common numbers.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash map usage, combinatorics for calculating pairs.
- Problem-solving patterns identified: Reducing time complexity by avoiding direct comparisons.
- Optimization techniques learned: Utilizing data structures like hash maps for efficient counting.
- Similar problems to practice: Problems involving set intersections, combinatorics.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect hash map usage, miscalculating pairs.
- Edge cases to watch for: Empty intervals, single-element intervals, intervals with no intersections.
- Performance pitfalls: Using brute force approaches for large inputs.
- Testing considerations: Thoroughly testing with various interval configurations and sizes.