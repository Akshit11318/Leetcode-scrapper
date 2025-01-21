## Data Stream as Disjoint Intervals

**Problem Link:** https://leetcode.com/problems/data-stream-as-disjoint-intervals/description

**Problem Statement:**
- Input format and constraints: The problem involves a data stream where integers are added one by one. The task is to keep track of the disjoint intervals that cover all the numbers seen so far. 
- Expected output format: The solution should provide an efficient way to add new integers and return the disjoint intervals.
- Key requirements and edge cases to consider: Handling duplicate integers, negative numbers, and the ability to add numbers in any order.
- Example test cases with explanations: 
    - Adding numbers in ascending order: `[1, 2, 3, 4, 5]`.
    - Adding numbers in descending order: `[5, 4, 3, 2, 1]`.
    - Adding numbers in random order: `[3, 1, 5, 2, 4]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To keep track of all the numbers seen so far and merge any overlapping intervals.
- Step-by-step breakdown of the solution:
    1. Initialize an empty list to store the disjoint intervals.
    2. When a new integer is added, check if it can be merged with any existing interval.
    3. If it can be merged, update the corresponding interval. If not, add a new interval.
- Why this approach comes to mind first: It's straightforward to implement and easy to understand.

```cpp
class SummaryRanges {
public:
    vector<vector<int>> intervals;
    SummaryRanges() {}

    void addNum(int val) {
        vector<vector<int>> newIntervals;
        bool added = false;
        
        for (auto& interval : intervals) {
            if (val < interval[0] - 1) {
                newIntervals.push_back(interval);
            } else if (val > interval[1] + 1) {
                newIntervals.push_back(interval);
            } else {
                interval[0] = min(val, interval[0]);
                interval[1] = max(val, interval[1]);
                added = true;
            }
        }
        
        if (!added) {
            newIntervals.push_back({val, val});
        }
        
        intervals = newIntervals;
        
        // Merge overlapping intervals
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> merged;
        for (auto& interval : intervals) {
            if (merged.empty() || merged.back()[1] + 1 < interval[0]) {
                merged.push_back(interval);
            } else {
                merged.back()[1] = max(merged.back()[1], interval[1]);
            }
        }
        intervals = merged;
    }

    vector<vector<int>> getIntervals() {
        return intervals;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of intervals. This is because in the worst case, we might need to iterate through all intervals for each new number added.
> - **Space Complexity:** $O(n)$ for storing the intervals.
> - **Why these complexities occur:** The brute force approach involves iterating through all intervals for each new number, leading to quadratic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a `set` or a similar data structure to keep track of the numbers seen so far and then constructing the disjoint intervals from this set.
- Detailed breakdown of the approach:
    1. Initialize a `set` to store the numbers seen so far.
    2. When a new integer is added, insert it into the set.
    3. To get the disjoint intervals, iterate through the set and merge any consecutive numbers.
- Proof of optimality: This approach ensures that we only need to iterate through the set once to construct the disjoint intervals, leading to a significant improvement in time complexity.

```cpp
class SummaryRanges {
public:
    set<int> nums;
    vector<vector<int>> intervals;
    
    SummaryRanges() {}

    void addNum(int val) {
        nums.insert(val);
    }

    vector<vector<int>> getIntervals() {
        intervals.clear();
        if (nums.empty()) return intervals;
        
        set<int>::iterator it = nums.begin();
        int start = *it, end = *it;
        it++;
        
        while (it != nums.end()) {
            if (*it == end + 1) {
                end = *it;
            } else {
                intervals.push_back({start, end});
                start = *it;
                end = *it;
            }
            it++;
        }
        
        intervals.push_back({start, end});
        return intervals;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of unique integers. This is because we only need to iterate through the set once to construct the disjoint intervals.
> - **Space Complexity:** $O(n)$ for storing the set and the intervals.
> - **Optimality proof:** This approach ensures that we only need to iterate through the set once, leading to linear time complexity. This is optimal because we need to at least read the input once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `set` to keep track of unique elements and constructing disjoint intervals from this set.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (keeping track of numbers and constructing intervals) and using the right data structure to solve each sub-problem.
- Optimization techniques learned: Using a `set` to reduce the time complexity of inserting and searching for elements.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases (e.g., empty input) and not handling duplicate integers correctly.
- Edge cases to watch for: Handling negative numbers, zero, and large integers.
- Performance pitfalls: Using a brute force approach that leads to quadratic time complexity.
- Testing considerations: Testing the solution with different input scenarios, including ascending, descending, and random orders.