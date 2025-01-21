## Find the Start and End Number of Continuous Ranges
**Problem Link:** https://leetcode.com/problems/find-the-start-and-end-number-of-continuous-ranges/description

**Problem Statement:**
- Input: A list of integers `nums` sorted in ascending order, possibly containing duplicates.
- Output: A list of lists, where each sublist contains the start and end numbers of continuous ranges.
- Key requirements:
  - Continuous ranges are defined as sequences of numbers where each number is one more than the previous.
  - The input list `nums` is sorted, but may contain duplicates.
- Edge cases:
  - An empty input list.
  - A list with a single element.
  - A list with all elements being the same.
- Example test cases:
  - Input: `nums = [0,1,2,4,5,7]`
    - Output: `[[0,2],[4,5],[7,7]]`
  - Input: `nums = [0,2,3,4,6,8,9]`
    - Output: `[[0,0],[2,4],[6,6],[8,9]]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through the list and checking for continuous ranges manually.
- For each element, we check if it's the start of a new range by comparing it with the previous element.
- If it's not continuous with the previous element, we start a new range.
- We keep track of the start and end of each range as we iterate through the list.

```cpp
vector<vector<int>> findContinuousRanges(vector<int>& nums) {
    vector<vector<int>> ranges;
    if (nums.empty()) return ranges;

    int start = nums[0];
    int end = nums[0];
    for (int i = 1; i < nums.size(); ++i) {
        if (nums[i] - nums[i-1] == 1) {
            end = nums[i];
        } else {
            ranges.push_back({start, end});
            start = nums[i];
            end = nums[i];
        }
    }
    ranges.push_back({start, end});
    return ranges;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input list, because we make a single pass through the list.
> - **Space Complexity:** $O(n)$, as in the worst case (all elements are in separate ranges), the size of the output list could be equal to the size of the input list.
> - **Why these complexities occur:** The time complexity is linear because we only iterate through the list once. The space complexity is also linear due to the potential size of the output list.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is essentially the same as the brute force approach because the problem requires checking each element at least once to determine the continuous ranges.
- The key insight is recognizing that a single pass through the sorted list is sufficient to identify all continuous ranges.
- We maintain the same logic of tracking the start and end of each range and updating them as we encounter continuous or non-continuous numbers.

```cpp
vector<vector<int>> findContinuousRanges(vector<int>& nums) {
    vector<vector<int>> ranges;
    if (nums.empty()) return ranges;

    int start = nums[0];
    int end = nums[0];
    for (int i = 1; i < nums.size(); ++i) {
        if (nums[i] - nums[i-1] == 1) {
            end = nums[i];
        } else {
            ranges.push_back({start, end});
            start = nums[i];
            end = nums[i];
        }
    }
    ranges.push_back({start, end});
    return ranges;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input list, because we make a single pass through the list.
> - **Space Complexity:** $O(n)$, as in the worst case, the size of the output list could be equal to the size of the input list.
> - **Optimality proof:** This is optimal because we must examine each element at least once to determine if it's part of a continuous range, making a single pass the minimum required to solve the problem.

---

### Final Notes

**Learning Points:**
- The importance of recognizing that some problems require at least a single pass through the data, making $O(n)$ the best possible time complexity.
- How to identify continuous ranges in a sorted list by comparing adjacent elements.
- Understanding that sometimes, the brute force approach is already optimal due to the inherent requirements of the problem.

**Mistakes to Avoid:**
- Assuming that a problem must have a more complex solution than it actually does.
- Not considering the implications of the input being sorted.
- Failing to handle edge cases such as an empty list or a list with a single element.