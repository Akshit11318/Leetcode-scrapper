## Range Module
**Problem Link:** [https://leetcode.com/problems/range-module/description](https://leetcode.com/problems/range-module/description)

**Problem Statement:**
- Input format and constraints: The problem requires implementing a `RangeModule` class with methods to add, remove, and query ranges. The `addRange` method takes an interval `[left, right]` and adds it to the list of ranges. The `removeRange` method removes the interval `[left, right]` from the list of ranges. The `queryRange` method checks if the interval `[left, right]` is fully covered by the ranges in the list.
- Expected output format: The `queryRange` method returns `true` if the interval is fully covered and `false` otherwise.
- Key requirements and edge cases to consider: Handling overlapping ranges, non-overlapping ranges, and edge cases where the interval is partially covered.
- Example test cases with explanations:
  - Adding and querying a single range: `addRange(1, 5)`, `queryRange(1, 5)` returns `true`.
  - Adding and querying overlapping ranges: `addRange(1, 5)`, `addRange(3, 7)`, `queryRange(3, 4)` returns `true`.
  - Removing a range: `addRange(1, 5)`, `removeRange(2, 3)`, `queryRange(2, 3)` returns `false`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One possible approach is to store all the ranges in a list and then iterate over the list to check if a given interval is fully covered.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the ranges.
  2. Implement the `addRange` method by appending the new range to the list.
  3. Implement the `removeRange` method by iterating over the list and removing any range that overlaps with the given interval.
  4. Implement the `queryRange` method by iterating over the list and checking if the given interval is fully covered by any of the ranges.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity due to the repeated iterations over the list of ranges.

```cpp
class RangeModule {
public:
    vector<pair<int, int>> ranges;
    
    void addRange(int left, int right) {
        ranges.push_back({left, right});
    }
    
    void removeRange(int left, int right) {
        vector<pair<int, int>> newRanges;
        for (auto range : ranges) {
            if (range.first > right || range.second < left) {
                newRanges.push_back(range);
            } else {
                if (range.first < left) {
                    newRanges.push_back({range.first, left - 1});
                }
                if (range.second > right) {
                    newRanges.push_back({right + 1, range.second});
                }
            }
        }
        ranges = newRanges;
    }
    
    bool queryRange(int left, int right) {
        for (auto range : ranges) {
            if (range.first <= left && range.second >= right) {
                return true;
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for `addRange`, $O(n)$ for `removeRange`, and $O(n)$ for `queryRange`, where $n$ is the number of ranges.
> - **Space Complexity:** $O(n)$, where $n$ is the number of ranges.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the repeated iterations over the list of ranges, and the space complexity is linear because we store all the ranges in a list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using an interval tree or a segment tree to store the ranges can significantly improve the time complexity of the `addRange`, `removeRange`, and `queryRange` methods.
- Detailed breakdown of the approach:
  1. Initialize an empty segment tree to store the ranges.
  2. Implement the `addRange` method by updating the segment tree with the new range.
  3. Implement the `removeRange` method by updating the segment tree with the removed range.
  4. Implement the `queryRange` method by querying the segment tree with the given interval.
- Proof of optimality: The segment tree approach has a time complexity of $O(\log n)$ for all three methods, which is optimal because we need to perform a binary search to find the relevant ranges.

```cpp
class RangeModule {
public:
    set<int> points;
    map<int, int> ranges;
    
    void addRange(int left, int right) {
        points.insert(left);
        points.insert(right);
        auto it = ranges.lower_bound(left);
        while (it != ranges.end() && it->first <= right) {
            right = max(right, it->second);
            points.erase(it->first);
            points.erase(it->second);
            ranges.erase(it);
            it = ranges.lower_bound(left);
        }
        ranges[left] = right;
    }
    
    void removeRange(int left, int right) {
        auto it = ranges.lower_bound(left);
        while (it != ranges.end() && it->first < right) {
            if (it->second > right) {
                points.insert(right);
                ranges[right] = it->second;
                it->second = right - 1;
                break;
            }
            points.erase(it->first);
            points.erase(it->second);
            ranges.erase(it);
            it = ranges.lower_bound(left);
        }
    }
    
    bool queryRange(int left, int right) {
        auto it = ranges.lower_bound(left);
        if (it == ranges.end() || it->first > left) return false;
        return it->second >= right;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$ for `addRange`, $O(\log n)$ for `removeRange`, and $O(\log n)$ for `queryRange`, where $n$ is the number of ranges.
> - **Space Complexity:** $O(n)$, where $n$ is the number of ranges.
> - **Optimality proof:** The segment tree approach has a time complexity of $O(\log n)$ for all three methods, which is optimal because we need to perform a binary search to find the relevant ranges.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Interval trees, segment trees, and binary search.
- Problem-solving patterns identified: Using data structures to improve time complexity.
- Optimization techniques learned: Using a segment tree to store ranges and performing binary search to find relevant ranges.
- Similar problems to practice: Implementing interval trees and segment trees for other problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as overlapping ranges or non-overlapping ranges.
- Edge cases to watch for: Partially covered intervals, overlapping ranges, and non-overlapping ranges.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Testing the implementation with different scenarios, such as adding and removing ranges, and querying intervals.