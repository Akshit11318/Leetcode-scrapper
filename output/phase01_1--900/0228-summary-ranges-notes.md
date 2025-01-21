## Summary Ranges
**Problem Link:** [https://leetcode.com/problems/summary-ranges/description](https://leetcode.com/problems/summary-ranges/description)

**Problem Statement:**
- Input: A sorted list of unique integers `nums`.
- Constraints: `0 <= nums.length <= 10^4`, `0 <= nums[i] <= 10^9`.
- Expected output: A list of strings representing the summary of ranges in the input list. For example, if the input is `[0,1,2,4,5,7]`, the output should be `["0->2","4->5","7"]`.
- Key requirements and edge cases to consider:
  - Handle empty input lists.
  - Handle lists with a single element.
  - Ensure the output is correctly formatted for both single numbers and ranges.

Example test cases with explanations:
- Input: `[0,1,2,4,5,7]`, Output: `["0->2","4->5","7"]`
- Input: `[0,2,3,4,6,8,9]`, Output: `["0","2->4","6","8->9"]`
- Input: `[]`, Output: `[]`
- Input: `[0]`, Output: `["0"]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the list and compare each number with its next one to determine if they are consecutive.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the result.
  2. Iterate through the input list. For each number, check if it is the start of a new range or part of an existing range.
  3. If the current number is not consecutive to the previous one, start a new range.
  4. If the current number is the last in the list or not consecutive to the next one, end the current range and add it to the result list.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem by examining each number in relation to its neighbors.

```cpp
vector<string> summaryRanges(vector<int>& nums) {
    vector<string> result;
    if (nums.size() == 0) return result;
    
    int start = nums[0];
    int end = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] == end + 1) {
            end = nums[i];
        } else {
            // Add the current range to the result
            if (start == end) {
                result.push_back(to_string(start));
            } else {
                result.push_back(to_string(start) + "->" + to_string(end));
            }
            // Start a new range
            start = nums[i];
            end = nums[i];
        }
    }
    // Add the last range to the result
    if (start == end) {
        result.push_back(to_string(start));
    } else {
        result.push_back(to_string(start) + "->" + to_string(end));
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input list, because we make a single pass through the list.
> - **Space Complexity:** $O(n)$, because in the worst case (all numbers are non-consecutive), the size of the output list could be equal to the size of the input list.
> - **Why these complexities occur:** The time complexity is linear because we process each number once. The space complexity is linear because we store each range (which could be a single number) in the output list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach, but recognizing that the brute force is already optimal in terms of time complexity because we must examine each number at least once. The provided brute force solution is already optimal in terms of time complexity.
- Detailed breakdown of the approach: The approach remains the same as the brute force because it's already optimized for time complexity.
- Proof of optimality: The solution has a time complexity of $O(n)$, which is optimal because we must at least read the input once. The space complexity is also $O(n)$, which is necessary for storing the output.

```cpp
// The code provided in the brute force section is already optimal.
vector<string> summaryRanges(vector<int>& nums) {
    vector<string> result;
    if (nums.size() == 0) return result;
    
    int start = nums[0];
    int end = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] == end + 1) {
            end = nums[i];
        } else {
            // Add the current range to the result
            if (start == end) {
                result.push_back(to_string(start));
            } else {
                result.push_back(to_string(start) + "->" + to_string(end));
            }
            // Start a new range
            start = nums[i];
            end = nums[i];
        }
    }
    // Add the last range to the result
    if (start == end) {
        result.push_back(to_string(start));
    } else {
        result.push_back(to_string(start) + "->" + to_string(end));
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input list.
> - **Space Complexity:** $O(n)$, because in the worst case, the size of the output list could be equal to the size of the input list.
> - **Optimality proof:** The solution is optimal because it processes each number exactly once, resulting in a linear time complexity, and it stores each range in the output, resulting in a linear space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and string manipulation.
- Problem-solving patterns identified: Breaking down the problem into ranges and handling edge cases.
- Optimization techniques learned: Recognizing that a single pass through the data can be sufficient for solving the problem efficiently.
- Similar problems to practice: Other problems involving iterating through a list and making decisions based on the relationships between adjacent elements.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases like an empty input list or a list with a single element.
- Edge cases to watch for: Lists with all non-consecutive numbers, lists with all consecutive numbers, and lists with a mix of both.
- Performance pitfalls: Incorrectly assuming that a more complex data structure or algorithm is needed when a simple iteration will suffice.
- Testing considerations: Ensure to test with various inputs, including edge cases, to verify the correctness and efficiency of the solution.